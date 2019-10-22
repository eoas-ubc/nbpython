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


def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip())
    parser.add_argument('old_pynotebook', type=str, help='full path to python notebook with answer cells')
    parser.add_argument('new_pynotebook', type=str, help='full path to new python notebook to be written')
    return parser

def main(args=None):
    parser = make_parser()
    args=parser.parse_args(args)
    nb_obj = jp.readf(args.old_pynotebook)
    new_nb = nu.strip_answers(nb_obj)
    jp.writef(new_nb,args.new_pynotebook,)
    jupytext(args=[args.new_pynotebook,'--to','ipynb','--execute'])
    Path(args.new_pynotebook).touch()

if __name__ == "__main__":
     main()
