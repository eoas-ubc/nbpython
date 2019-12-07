#!/usr/bin/env python
"""
code to find notebooks

and try another line
"""
from pathlib import Path
from pyutils.table import make_table
from collections import OrderedDict
import argparse
import pdb
import textwrap
import importlib_resources as ir
import context
import json
import pprint
import click
import shutil
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
    format_string = r'{"jupytext":{"formats":"ipynb,py:percent"}}'
    root_dir = Path(notebook_path)
    ipynb_files = root_dir.glob("**/*.ipynb")
    ipynb_files = print_files(ipynb_files)
    rst_files = root_dir.glob("**/*.rst")
    rst_files = print_files(rst_files)
    notebook_dir = root_dir / Path("notebooks")
    notebook_dir.mkdir(parents=True, exist_ok=True)
    print(f"created {notebook_dir}")
    for item in ipynb_files:
        outfile = notebook_dir / item.name
        print(f"copy {item} to {outfile}")
        shutil.copy(str(item), str(outfile))
        jupytext([str(outfile), "--to", "py:percent"])
        pyfile = outfile.with_suffix(".py")
        jupytext([str(pyfile), "--update-metadata", format_string])


if __name__ == "__main__":
    main()