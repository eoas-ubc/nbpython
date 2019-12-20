"""
remove all answer cells and generate a new notebook

Usage:  python strip_answers.py python/assignment3_2019t1_solution.py python/assignment3_2019t1_student.py

will generate a new notebook python/assignment3_2019t1_student.py, with paired 
assignment3_2019t1_student.ipynb in the folder above, and run that ipynb file.
"""
from pathlib import Path
import e340lib.noteutils as nu
import jupytext as jp
from jupytext.cli import jupytext
import json
import click


@click.command()
@click.argument("pynotebook", type=click.File("r"), nargs=1)
@click.argument("keyout", type=click.File("w"), nargs=1)
def main(pynotebook, keyout):
    keypath = Path(keyout.name)
    if keypath.suffix != ".json":
        raise ValueError(f"your output file {keyout} needs to end in .json")
    nb_obj = jp.readf(pynotebook)
    answers = nu.get_key(nb_obj)
    json.dump(answers, keyout, indent=4)


if __name__ == "__main__":
    main()
