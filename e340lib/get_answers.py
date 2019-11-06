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
import json


def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip())
    parser.add_argument('pynotebook', type=str, help='full path to python notebook with answer cells')
    parser.add_argument('keyout', type=str, help='name of output json file')
    return parser

def main(args=None):
    parser = make_parser()
    args=parser.parse_args(args)
    pynotebook = Path(args.pynotebook)
    keyout = Path(args.keyout)
    if keyout.suffix != '.json':
        raise ValueError(f"your output file {keyout} needs to end in .json")
    nb_obj = jp.readf(pynotebook)
    answers = nu.get_key(nb_obj)
    with open(keyout,'w') as outfile:
        json.dump(answers,outfile,indent=4)
          
if __name__ == "__main__":
     main()
