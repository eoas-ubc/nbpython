from pathlib import Path
import pandas as pd
import context
import numpy as np
import click
from matplotlib import pyplot as plt
import pdb
import re

quiz_re = re.compile(r".*quiz\s+(\d+).*", re.IGNORECASE)


def clean_grades(scores):
    hit = scores > 1
    scores = scores[hit]
    return scores


def calc_grades(ax, scores, nbins=10):
    median = np.nanmedian(scores)
    ax.hist(scores, nbins)
    return ax, median


@click.command()
@click.argument(
    "grade_dir",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    nargs=1,
)
@click.argument("filename", type=str, nargs=1)
def main(grade_dir, filename):
    """
    example:  plot_hist graded_files *1136*csv
    """
    grade_file = list(Path(grade_dir).glob(filename))[0]
    plt.close("all")
    df_grade = pd.read_csv(grade_file)
    all_cols = df_grade.columns
    for col in all_cols:
        catch = quiz_re.match(col)
        if catch:
            print(catch.group(1))
    pdb.set_trace()
    q2_ind_score = df_grade["Quiz 2 Individual (417784)"].values
    q2_group_score = df_grade["Quiz 2 Group (417785)"].values
    q2_total_score = df_grade["Quiz 2 Total (417786)"].values

    q1_ind_score = df_grade["Quiz 1 Individual (369344)"].values
    q1_group_score = df_grade["Quiz 1 Group (369343)"].values
    q1_total_score = df_grade["Quiz 1 Total (369345)"].values

    vectors = [q1_ind_score, q1_group_score, q1_total_score]
    vectors = [clean_grades(item) for item in vectors]
    q1_ind_score, q1_group_score, q1_total_score = vectors

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    ax1, ax2, ax3, ax4 = axes.flatten()

    ax1, median = calc_grades(ax1, q2_total_score)
    posted_title = f"Quiz 2 combined grades: median={median:4.2f}"
    ax1.set(title=posted_title, xlabel="total grade", ylabel="count")

    ax2, median = calc_grades(ax2, q2_group_score)
    posted_title = f"Quiz 2 group grades: median={median:4.2f}"
    ax2.set(title=posted_title, xlabel="group grade", ylabel="count")

    ax3, median = calc_grades(ax3, q1_total_score)
    posted_title = f"Quiz 1 combined grades: median={median:4.2f}"
    ax3.set(title=posted_title, xlabel="total grade", ylabel="count")

    ax4, median = calc_grades(ax4, q1_group_score)
    posted_title = f"Quiz 1 group grades: median={median:4.2f}"
    ax4.set(title=posted_title, xlabel="group grade", ylabel="count")
    fig.savefig("quiz2_marks.png")
    plt.show()


main()
