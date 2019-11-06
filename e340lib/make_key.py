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

def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip())
    parser.add_argument('Akey', type=str, help='full path Aanswer json file with dictionary')
    parser.add_argument('Border', type=str, help='full path to Border json file with dictionary')
    parser.add_argument('keyout', type=str, help='full path to output csv file for merged key')
    return parser

def main(args=None):o
    parser = make_parser()
    args=parser.parse_args(args)
    akey_json = Path(args.Akey)
    Border_json = Path(args.Border)
    keyout_csv = Path(args.keyout)
    if akey_json.suffix != '.json':
        raise ValueError(f"your akey file {akey_json} needs to end in .json")
    if Border_json.suffix != '.json':
        raise ValueError(f"your Border file {Border_json} needs to end in .json")
    if keyout_csv.suffix != '.csv':
        raise ValueError(f"your keyout file {keyout_csv} needs to end in .csv")
    with open(akey_json,'r') as akey:
        akey_dict = json.load(akey)
    with open(Border_json,'r') as border:
        Border_dict = json.load(border)

    key_lines=[]
    for Anum in akey_dict.keys():
        Bnum = str(Border_dict[Anum])
        b_ans = akey_dict[Bnum]
        a_ans = akey_dict[Anum]
        line = {'Aorder' : Anum,'A': a_ans, 'B': b_ans,'Border':Bnum}
        key_lines.append(line)

    df = pd.DataFrame.from_records(key_lines)
    df.to_csv(keyout_csv,index=False)
          
if __name__ == "__main__":
     main()
