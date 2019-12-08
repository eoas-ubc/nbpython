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
    the_file = Path(the_file)
    head = the_file.name
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
    return head.stem, the_date

def checkpoint_filter(item):
    return str(item).find("checkpoints") == -1


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
    pp = pprint.PrettyPrinter(indent=4)
    notebook_path = Path(notebook_path).resolve()
    root_dir = Path(notebook_path).parent.resolve()
    py_files = notebook_path.glob("**/*.py")
    py_files = [item for item in py_files if checkpoint_filter(item)]
    print(f"operating on {pp.pformat(py_files)}")
    ipynb_dir = root_dir / 'rendered'
    ipynb_dir.mkdir(parents=True, exist_ok = True)
    for item in py_files:
        source_ipynb = Path(item.name).with_suffix('.ipynb')
        source_path = notebook_path / source_ipynb
        print(f"working on {item}")
        dest_path = ipynb_dir / source_ipynb
        jupytext([str(item),'--to','notebook','--execute'])
        print(f"moving {source_path} to {dest_path}")
        shutil.move(source_path, dest_path)


if __name__ == "__main__":
    main()
