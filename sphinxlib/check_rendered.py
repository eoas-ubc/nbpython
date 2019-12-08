#!/usr/bin/env python
"""
code to find notebooks

and try another line
"""
from pathlib import Path
import pprint
import click
import shutil
from jupytext.cli import jupytext
import datetime
import os
import tzlocal
import stat
import pytz


def find_modtime(the_file):
    """
       remove the .py or .ipynb extenstion from the file name
       to get the head, and return that name, plus the modification
       date in UTC.  
    """
    the_file = str(Path(the_file).resolved())
    #
    #  see os.stat docs for the format of the stat function.  It returns
    #  multiple fields (owner, date created, size, etc.) that are indexed by the stat object
    #
    the_date = datetime.datetime.fromtimestamp(os.stat(the_file)[stat.ST_MTIME])
    #
    # finding the local timezone is suprisingly hard -- need to install a
    # special module called tzlocal using pip install tzlocal
    #
    local_tz = tzlocal.get_localzone()
    the_date = local_tz.localize(the_date)
    #
    # convert every date to UTC
    #
    the_date = the_date.astimezone(pytz.utc)
    #
    # remove everything but the root filename
    #
    return the_date


def checkpoint_filter(item):
    """
    return True if checkpoints is not in name
    """
    return str(item).find("checkpoints") == -1


def changed_filter(file1, file2):
    """
    return True if file1 is newer than file2
    or if file2 doesn't exist
    """
    if not file2.is_file():
        return True
    file1 = Path(file1)
    file2 = Path(file2)
    file1_date = find_modtime(file1)
    file2_date = find_modtime(file2)
    return file1_date > file2_date


def make_dest(pylist, dest_dir):
    """
    transform a list of py files into a list of ipynb files
    """
    outlist = []
    for item in pylist:
        source_ipynb = Path(item.name).with_suffix(".ipynb")
        dest_path = dest_dir / source_ipynb
        outlist.append(dest_path)
    out_pairs = zip(pylist, outlist)
    return out_pairs


@click.command()
@click.argument("notebook_path", type=str, nargs=1)
def main(notebook_path):
    pp = pprint.PrettyPrinter(indent=4)
    notebook_path = Path(notebook_path).resolve()
    root_dir = Path(notebook_path).parent.resolve()
    py_files = list(notebook_path.glob("**/*.py"))
    py_files = [item for item in py_files if checkpoint_filter(item)]
    dest_dir = root_dir / "rendered"
    file_pairs = make_dest(py_files, dest_dir)
    print(f"operating on {pp.pformat(py_files)}")
    dest_dir.mkdir(parents=True, exist_ok=True)
    for origin, dest_path in file_pairs:
        jupytext([str(origin), "--to", "notebook", "--execute"])
        source_path = origin.with_suffix(".ipynb")
        print(f"moving {source_path} to {dest_path}")
        shutil.move(source_path, dest_path)


if __name__ == "__main__":
    main()
