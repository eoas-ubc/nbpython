import pandas as pd
import click
import json
from pathlib import Path
import numpy as np
from fuzzywuzzy import fuzz
import pdb


def find_closest(the_id, good_ids):
    score_list = []
    for choice in good_ids:
        score_list.append(fuzz.ratio(the_id, choice))
    score_array = np.array(score_list)
    max_index = np.argmax(score_array)
    good_choice = good_ids[max_index]
    return good_choice


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

    calculate the mid-term grade

    Example: python grade_quizzes.py filenames.json

    """

    with open(filenames.name, "r") as infile:
        file_dict = json.load(infile)
    # pdb.set_trace()
    grade_file = list(Path().glob(file_dict["files"]["gradebook"]))[0]
    ind_file = list(Path().glob(file_dict["files"]["remark_ind"]))[0]
    group_file = list(Path().glob(file_dict["files"]["remark_group"]))[0]
    df_grades = pd.read_csv(grade_file)
    df_ind = pd.read_excel(ind_file)
    df_group = pd.read_excel(group_file)
    print(df_grades.columns)
    print(df_ind.columns)
    print(df_group.columns)
    student_ids = df_grades['Student Number'].to_numpy()
    student_ids = [int(item) for item in student_ids]
    group_ids = [
        "STUDENT ID #1",
        "STUDENT ID #2",
        "STUDENT ID #3",
        "STUDENT ID #4",
        "Total Score",
    ]
    group_scores = df_group[group_ids].to_numpy()
    nrows, ncols = group_scores.shape
    id_list = []
    group_list = []
    for i in range(nrows):
        row_ids = group_scores[i, :4]
        score = group_scores[i, 4]
        row_list = []
        for item in row_ids:
            the_id = int(item)
            id_list.append(the_id)
            row_list.append({"id": the_id, "score": score})
        group_list.append(row_list)

    print(id_list, group_list)
    ind_scores = df_ind[["STUDENT ID", "Total Score"]].to_numpy()
    nrows, ncols = ind_scores.shape


main()
