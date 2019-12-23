import pandas as pd
import click
import json
from pathlib import Path
import numpy as np
from fuzzywuzzy import fuzz
import pdb


def find_closest(the_id, good_ids):
    """
    search through a list of good_ids and return the
    member of good_ids that is closest to the_id

    Parameters
    ----------

    the_id: string
      id to tesg

    good_ids: list of strings
      the gradebook ids to test against

    Returns
    -------

    good_choice: string
       best fit string
    """
    score_list = []
    for choice in good_ids:
        score_list.append(fuzz.ratio(the_id, choice))
    score_array = np.array(score_list)
    max_index = np.argmax(score_array)
    good_choice = good_ids[max_index]
    return good_choice


def string_index(float_vec):
    nan_counter = -1
    string_vec = []
    for item in float_vec:
        if np.isnan(item):
            string_vec.append(str(nan_counter))
            nan_counter -= 1
        else:
            string_vec.append(str(int(item)))
    return string_vec


def make_dfs(filename):
    with open(filename, "r") as infile:
        file_dict = json.load(infile)
    grade_file = list(Path().glob(file_dict["files"]["gradebook"]))[0]
    ind_file = list(Path().glob(file_dict["files"]["remark_ind"]))[0]
    group_file = list(Path().glob(file_dict["files"]["remark_group"]))[0]
    df_canvas = pd.read_csv(grade_file)
    the_ids = string_index(df_canvas["Student Number"].values)
    df_canvas.loc[:,'Student Number'] = the_ids
    df_canvas.set_index("Student Number",inplace=True, drop=False)
    print(f"canvas: {the_ids}")
    if ind_file.suffix == ".xlsx":
        df_ind = pd.read_excel(ind_file)
        df_group = pd.read_excel(group_file)
    else:
        df_ind = pd.read_csv(ind_file)
        df_group=pd.read_csv(group_file)
    
    group_ids = [
        "STUDENT ID #1",
        "STUDENT ID #2",
        "STUDENT ID #3",
        "STUDENT ID #4",
        "Percent Score",
    ]
    group_scores = df_group[group_ids].to_numpy()
    nrows, ncols = group_scores.shape
    group_id_list = []
    group_list = []
    for i in range(nrows):
        row_ids = group_scores[i, :4]
        the_score = group_scores[i, 4]
        row_list = []
        for item in row_ids:
            try:
                the_id = str(int(item))
            except:
                print((f"trouble reading {group_file}\n"
                       f"sudent number {item} set to '-1'"))
                the_id = str(-1)
            group_id_list.append(the_id)
            row_list.append({"id": the_id, "group_score": the_score})
        group_list.append(row_list)
    group_scores = []
    for a_row in group_list:
        group_scores.extend(a_row)

    ind_id_list = []
    ind_list = []
    ind_scores = df_ind[["STUDENT ID", "Percent Score"]].to_numpy()
    nrows, ncols = ind_scores.shape
    for i in range(nrows):
        the_id = str(int(ind_scores[i, 0]))
        the_score = ind_scores[i, 1]
        ind_id_list.append(the_id)
        ind_list.append({"id": the_id, "ind_score": the_score})

    df_group = pd.DataFrame.from_records(group_scores)
    df_ind = pd.DataFrame.from_records(ind_list)
    df_ind.set_index("id", inplace=True, drop=True)
    df_group.set_index("id", inplace=True, drop=True)
    return df_group, df_ind, df_canvas


def merge_two(df_left, df_right):
    df_return = pd.merge(
        df_left, df_right, how="left", left_index=True, right_index=True, sort=False
    )
    return pd.DataFrame(df_return, copy=True)


def mark_combined(row):
    try:
        group = row["group_score"]
        if group < row["ind_score"]:
            group = row["ind_score"]
        mark = 0.85 * row["ind_score"] + 0.15 * group
    except NameError:
        print(f"trouble: {row}")
    return mark


def check_ids(df, good_ids):
    print(f"checking ids")
    for the_id in df.index.to_numpy():
        nearest_id = find_closest(the_id, good_ids)
        if nearest_id != the_id:
            print(f"miss bad id -- {the_id},closest id -- {nearest_id}")

@click.command()
@click.argument("filenames", type=click.File("r"), nargs=1)
def main(filenames):
    """
    Given the name of a json file with the following format:

    \b
    {
        "history": "2019t1",
        "files": {
            "gradebook": "*EOSC_340_101.csv",
            "remark_ind": "*Q3*Grades.xlsx",
            "remark_group": "*Q3*Group.xlsx"
        }
    }

    calculate the quiz grade

    Example: python grade_quizzes.py filenames.json

    """
    df_group, df_ind, df_canvas = make_dfs(filenames.name)
    student_ids = df_canvas["Student Number"].to_numpy()
    good_ids = string_index(student_ids)
    int_ids = [int(item) for item in good_ids]
    df_canvas.index = int_ids
    check_ids(df_ind, good_ids)
    check_ids(df_group, good_ids)

    df_out = merge_two(df_ind, df_group)
    new_index = [int(item) for item in df_out.index]
    df_out.index = new_index
    print(df_out.head())

    total_score = df_out.apply(mark_combined, axis=1)
    df_out["total_score"] = total_score

    #
    # save points possible then drop it
    #
    possible_row = df_canvas.loc[df_canvas["Student"].str.find("Points Possible") > -1]
    if possible_row.index < -1:
        df_canvas.drop([-1], inplace=True)
        print(possible_row.index)
    can_grade_cols = list(df_canvas.columns.to_list())
    can_mandatory_columns = list(can_grade_cols[:5])
    df_upload = pd.DataFrame(df_canvas[can_mandatory_columns], copy=True)
    can_col = np.linspace(
        -1, len(df_upload), num=len(df_upload), dtype=np.int, endpoint=False
    ).astype(np.int)
    df_upload["sort_order"] = can_col
    df_doit = merge_two(df_upload, df_out)
    df_doit.sort_values("sort_order", ascending=True, inplace=True)
    keep_columns = [
        "Student",
        "ID",
        "SIS User ID",
        "SIS Login ID",
        "Section",
        "ind_score",
        "group_score",
        "total_score",
    ]

    df_doit = df_doit[keep_columns]
    possible_row = df_doit.loc[df_doit["Student"].str.find("Points Possible") > -1]
    points_possible = df_canvas.loc[possible_row.index]
    points_possible = points_possible.iloc[0, :5]
    points_possible[1:5] = " "
    extent = pd.Series(
        [100, 100, 100], index=["ind_score", "group_score", "total_score"]
    )
    points_possible = points_possible.append(extent)
    df_doit.loc[possible_row.index, :] = points_possible.values
    print(df_doit.columns)
    df_doit.rename(
        columns=dict(
            ind_score="Quiz 4 Individual",
            group_score="Quiz 4 Group",
            total_score="Quiz 4 Total",
        ),
        inplace=True,
    )
    df_doit.to_csv("testme.csv", index=False)

if __name__ == "__main__":
    main()
