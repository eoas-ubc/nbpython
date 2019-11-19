"""
remove all answer cells and generate a new notebook

Usage:  python strip_answers.py python/assignment3_2019t1_solution.py python/assignment3_2019t1_student.py

will generate a new notebook python/assignment3_2019t1_student.py, with paired 
assignment3_2019t1_student.ipynb in the folder above, and run that ipynb file.
"""
from pathlib import Path
import context
import click
import sys
import e340lib.noteutils as nu
import jupytext as jp
from jupytext.cli import jupytext


@click.command()
@click.argument("old_pynotebook", type=click.File("r"), nargs=1)
@click.argument("new_pynotebook", type=click.File("w"), nargs=1)
def main(old_pynotebook, new_pynotebook):
    """
    Usage:  python strip_answers.py assignment3_2019t1_solution.py assignment3_2019t1_student.py
    """
    old_pynotebook = Path(old_pynotebook.name)
    new_pynotebook = Path(new_pynotebook.name)
    nb_obj = jp.readf(old_pynotebook)
    new_nb = nu.strip_answers(nb_obj)
    jp.writef(new_nb, str(new_pynotebook))
    jupytext(args=[str(new_pynotebook), "--sync"])
    Path(new_pynotebook).touch()


if __name__ == "__main__":
    main()
