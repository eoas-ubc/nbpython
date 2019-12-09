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

@click.group()
def main():
    """
    set of tools for manipulating notebooks
    """
    pass



@main.command()
@click.argument("notebook_path", type=str, nargs=1)
def nbinit(notebook_path):
    """
    \b 
    notebook_path: str
       folder with py versions of notebooks
    \b
    set the formats to "ipynb,py:percent" and
    the notebook_metadaa_filter to
         "all,-language_info,-toc,-latex_envs"

    example:
      python $sphinxlib/modify_notebooks.py nbinit .
    """
    py_files = Path(notebook_path).glob("*.py")
    format_string = r'{"jupytext":{"formats":"ipynb,py:percent"}}'
    text_string = (
        r'{"jupytext":{"notebook_metadata_filter": "all,-language_info,-toc,-latex_envs"}}'
    )
    header_string = r'{"latex_metadata": {"chead": "center head","lhead": "left head"} }'
    for item in py_files:
        jupytext([str(item), "--update-metadata", format_string])
        jupytext([str(item), "--update-metadata", text_string])
        jupytext([str(item), "--update-metadata", header_string])
        jupytext([str(item), "--sync"])


if __name__ == "__main__":
    main()
