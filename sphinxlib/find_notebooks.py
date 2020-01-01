#!/usr/bin/env python
"""
find all notebooks and write a json file
that that gives the notebooks and their rendered
destination

example:  python $sphinxlib/find_notebooks.py 
"""
from pathlib import Path
import click
import json


def print_files(file_glob):
    good_files = [item for item in file_glob if str(item).find("checkpoints") == -1]
    return good_files


@click.command()
@click.argument("notebook_path", type=str, nargs=1)
@click.argument("pyfile_path", type=str, nargs=1)
@click.argument("json_file", type=click.File("w"), nargs=1)
def main(notebook_path, pyfile_path, json_file):
    """
    \b
    notebook_path is folder containing notebooks
    pyfile_path is folder to place pyfile jupytext ipynb
    json_file is the path to a json_file to write info to
    """
    notebook_path = Path(notebook_path).resolve()
    print(f"looking for notebooks in {notebook_path}")
    ipynb_files = [
        item
        for item in notebook_path.glob("**/*.ipynb")
        if str(item).find("checkpoints") == -1
    ]
    py_files = [item.with_suffix(".py") for item in ipynb_files]
    relative_files = [item.relative_to(notebook_path) for item in ipynb_files]
    file_list = []
    pyfile_path = Path(pyfile_path).resolve()
    for the_py, the_rel in zip(py_files, relative_files):
        new_file = str((pyfile_path / the_rel))
        py_file = str(the_py)
        dict_item = dict(new_file=new_file, py_file=py_file)
        file_list.append(dict_item)
    the_dict = dict(
        notebook_path=str(notebook_path),
        pyfile_path=str(pyfile_path),
        file_list=file_list,
    )
    json.dump(the_dict, json_file, indent=4)


if __name__ == "__main__":
    main()
