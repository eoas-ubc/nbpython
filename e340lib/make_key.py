"""
generate a and b keys
"""
from pathlib import Path
import context
import argparse
import sys
import e340lib.noteutils as nu
import jupytext as jp
from jupytext.cli import jupytext
import pandas as pd
import json
import click


@click.command()
@click.argument("akey", type=click.File("r"), nargs=1)
@click.argument("border", type=click.File("r"), nargs=1)
@click.argument("keyout", type=click.File("w"), nargs=1)
def main(akey, border, keyout):
    """
    merge two sets of keys
    """
    akey_json = Path(akey.name)
    Border_json = Path(border.name)
    keyout_csv = Path(keyout.name)
    if akey_json.suffix != ".json":
        raise ValueError(f"your akey file {akey_json} needs to end in .json")
    if Border_json.suffix != ".json":
        raise ValueError(f"your Border file {Border_json} needs to end in .json")
    if keyout_csv.suffix != ".csv":
        raise ValueError(f"your keyout file {keyout_csv} needs to end in .csv")
    akey_dict = json.load(akey)
    Border_dict = json.load(border)

    key_lines = []
    for Anum in akey_dict.keys():
        Bnum = str(Border_dict[Anum])
        b_ans = akey_dict[Bnum]
        a_ans = akey_dict[Anum]
        line = {"Aorder": Anum, "A": a_ans, "B": b_ans, "Border": Bnum}
        key_lines.append(line)

    df = pd.DataFrame.from_records(key_lines)
    df.to_csv(keyout, index=False)


if __name__ == "__main__":
    main()
