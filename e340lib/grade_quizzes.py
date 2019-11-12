import pandas as pd
import click
import json
from pathlib import Path


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

    print(file_dict)


main()
