#!/usr/bin/env python
"""
code to find notebooks

and try another line
"""
from pathlib import Path
import pprint
import click
from jupytext.cli import jupytext


def print_files(file_glob):
    good_files = [
        item
        for item in file_glob
        if ((str(item).find("Book") > -1) & (str(item).find("checkpoints") == -1))
    ]
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(good_files)
    return good_files


@click.command()
@click.argument("notebook_path", type=str, nargs=1)
def main(notebook_path):
    py_files = Path(notebook_path).glob("*.py")
    format_string = r'{"jupytext":{"formats":"ipynb,py:percent"}}'
    text_string = (
        r'{"jupytext":{"notebook_metadata_filter": "all,-language_info,-toc,-latex_envs"}}'
    )
    for item in py_files:
        jupytext([str(item), "--update-metadata", format_string])
        jupytext([str(item), "--update-metadata", text_string])
        jupytext([str(item), "--sync"])


if __name__ == "__main__":
    main()
