"""
Add a key, value metadata pair to every cell in a notebook

Usage:  python add_cellmeta.py python/assignment3_2019t1_solution.py ctype question

adds {'ctype' : 'question'}

for every cell


"""
from pathlib import Path
import context
import argparse
import sys
from  e340lib import noteutils as nu
import jupytext as jp
from jupytext.cli import jupytext


def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip())
    parser.add_argument('pynotebook', type=str, help='full path to python notebook file to modify')
    parser.add_argument('cell_key', type=str, help='key for cell metadata')
    parser.add_argument('cell_value', type=str, help='value for key')
    return parser

def main(args=None):
    parser = make_parser()
    args=parser.parse_args(args)
    nb_obj = jp.readf(args.pynotebook)
    new_nb = nu.update_cell_meta(nb_obj,args.cell_key,args.cell_value)
    jp.writef(new_nb,args.pynotebook)
    jupytext(args=[args.pynotebook,'--to','..//ipynb','--execute'])
    Path(args.pynotebook).touch()

if __name__ == "__main__":
     main()
