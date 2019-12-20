"""
Add a key, value metadata pair to every cell in a notebook
Usage:  python add_cellmeta.py python/assignment3_2019t1_solution.py ctype question
adds {'ctype' : 'question'}
for every cell
"""

from pathlib import Path
import context
import click
from e340lib import noteutils as nu
import jupytext as jp
from jupytext.cli import jupytext


@click.command()
@click.argument("notebook_file", type=click.File("r"), nargs=1)
@click.argument("cell_key", type=str, nargs=1)
@click.argument("cell_value", type=str, nargs=1)
def main(notebook_file, cell_key, cell_value):
    """
    python add_cellmeta.py python/assignment3_2019t1_solution.py ctype question
    """
    nb_file = Path(notebook_file.name)
    nb_obj = jp.readf(nb_file)
    new_nb = nu.update_cell_meta(nb_obj, cell_key, cell_value)
    jp.writef(new_nb, str(nb_file))
    jupytext(args=[str(nb_file), "--sync"])
    nb_file.touch()


if __name__ == "__main__":
    main()
