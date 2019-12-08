"""
remove all answer cells and generate a new notebook

Usage:  python strip_answers.py python/assignment3_2019t1_solution.py python/assignment3_2019t1_student.py

will generate a new notebook python/assignment3_2019t1_student.py, with paired 
assignment3_2019t1_student.ipynb in the folder above, and run that ipynb file.
"""
from pathlib import Path
import context
import argparse
import sys
import e340lib.noteutils as nu
import jupytext as jp
from jupytext.cli import jupytext
import pandas as pd
import json
import click


@click.command()
@click.argument("pynotebook", type=click.File("r"), nargs=1)
@click.argument("keyout", type=click.File("w"), nargs=1)
def main(pynotebook, keyout):
    keypath = Path(keyout.name)
    nb_obj = jp.readf(pynotebook)
    b_dict = {}
    if keypath.suffix != ".json":
        raise ValueError(f"your output file {keyout} needs to end in .json")
    answers = nu.get_qorder(nb_obj)
    for item in answers:
        if item["qnumA"] in b_dict:
            raise ValueError(f"multiple A qnums for A question {item['qnumA']}")
        b_dict[item["qnumA"]] = item["qnumB"]

    json.dump(b_dict, keyout, indent=4)


if __name__ == "__main__":
    main()
