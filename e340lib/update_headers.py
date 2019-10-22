"""

"""
from pathlib import Path
import context
import argparse
import sys
from e340lib import noteutils as nu
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
    parser.add_argument('lhead', type=str, help='left header')
    parser.add_argument('chead', type=str, help='center header')
    return parser

def main(args=None):
    parser = make_parser()
    args=parser.parse_args(args)
    nb_obj = jp.readf(args.pynotebook)
    new_nb = nu.update_headers(nb_obj,lhead=args.lhead,
                                   chead=args.chead)
    jp.writef(new_nb,args.pynotebook)
    jupytext(args=[args.pynotebook,'--to','..//ipynb','--execute'])
    Path(args.pynotebook).touch()

if __name__ == "__main__":
     main()
