"""
take the filelist.json produced by find_notebooks.py
and render the notebooks

python $sphinxlib/check_rendered.py filelist.json
"""
from pathlib import Path
import json
import click
import shutil
from jupytext.cli import jupytext
import datetime
import os
import tzlocal
import stat
import pytz
import prettyprint as pp


def find_modtime(the_file):
    """
       remove the .py or .ipynb extenstion from the file name
       to get the head, and return that name, plus the modification
       date in UTC.  
    """
    the_file = str(Path(the_file).resolve())
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
    out_pairs = list(zip(pylist, outlist))
    return out_pairs


@click.group()
def main():
    """
    set of tools transforming jupytext iles
    """
    pass


@main.command()
@click.argument("json_filelist", type=click.File("r"), nargs=1)
def ipynb2py(json_filelist):
    file_dict = json.load(json_filelist)
    file_list = file_dict["file_list"]
    file_list = [(item['py_file'],item['new_file']) for item in file_list]
    dest_dir = Path(file_dict["rendered_path"])
    need_build = [changed_filter(file1, file2) for file1, file2 in file_list]
    build_list = []
    for count, the_pair in enumerate(file_list):
        if need_build[count]:
            build_list.append(the_pair)
    print(f"do any files need building {pp.pformat(build_list)}")
    dest_dir.mkdir(parents=True, exist_ok=True)
    for origin, dest_path in build_list:
        jupytext([str(origin), "--to", "notebook", "--execute"])
        source_path = origin.with_suffix(".ipynb")
        print(f"moving {source_path} to {dest_path}")
        shutil.move(source_path, dest_path)


@main.command()
@click.argument("json_filelist", type=click.File("r"), nargs=1)
def py2ipynb(json_filelist):

    file_dict = json.load(json_filelist)
    file_list = file_dict["file_list"]
    file_list = [(item['py_file'],item['new_file']) for item in file_list]
    dest_dir = Path(file_dict["rendered_path"])
    need_build = [changed_filter(file1, file2) for file1, file2 in file_list]
    build_list = []
    for count, the_pair in enumerate(file_list):
        if need_build[count]:
            build_list.append(the_pair)
    print(f"do any files need building {pp.pformat(build_list)}")
    dest_dir.mkdir(parents=True, exist_ok=True)
    for origin, dest_path in build_list:
        jupytext([str(origin), "--to", "py:percent"])
        source_path = origin.with_suffix(".ipynb")
        print(f"moving {source_path} to {dest_path}")
        shutil.move(source_path, dest_path)


if __name__ == "__main__":
    main()
