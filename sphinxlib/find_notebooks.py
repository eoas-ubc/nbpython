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
    head = head.split("/")[-1]
    return head, the_date


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
