from pathlib import Path
import pandas as pd
import context
import numpy as np
import click
from matplotlib import pyplot as plt
import pdb
import re

# Quiz 2 Individual (417784)
quiz_re = re.compile(
    r".*quiz\s+(?P<quiznum>\d+)\s+(?P<quiztype>\w+)\s.*", re.IGNORECASE
)


def clean_grades(scores):
    clean_scores = []
    for item in scores:
        try:
            the_score = float(item)
        except ValueError:
            the_score = np.nan
        clean_scores.append(the_score)
    scores = np.array(clean_scores)
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
    col_dict = {}
    for col in all_cols:
        catch = quiz_re.match(col)
        if catch:
            print(f"{catch.group('quiznum')} -- {catch.group('quiztype')}")
            key = (int(catch.group("quiznum")), catch.group("quiztype").lower())
            col_dict[key] = {"colname": col}
    for quiznum in [1, 2, 3]:
        for quiztype in ["individual", "group", "total"]:
            key = (quiznum, quiztype)
            grades = df_grade[col_dict[key]["colname"]].to_numpy()
            grades = clean_grades(grades)
            col_dict[key]["scores"] = grades

    quiz1, quiz2, quiz3 = [], [], []
    for quiztype in ["individual", "group", "total"]:
        quiz1.append(col_dict[(1, quiztype)]["scores"])
        quiz2.append(col_dict[(2, quiztype)]["scores"])
        quiz3.append(col_dict[(3, quiztype)]["scores"])

    plt.close("all")
    fig, axes = plt.subplots(3, 2, figsize=(14, 14), constrained_layout=True)

    ax1 = axes[0, 0]
    ax1, median = calc_grades(ax1, quiz1[2])
    posted_title = f"Quiz 1 combined grades: median={median:4.2f}"
    ax1.set(title=posted_title, xlabel="total grade", ylabel="count")

    ax2 = axes[0, 1]
    ax2, median = calc_grades(ax2, quiz1[1])
    posted_title = f"Quiz 1 group grades: median={median:4.2f}"
    ax2.set(title=posted_title, xlabel="group grade", ylabel="count")

    ax3 = axes[1, 0]
    ax3, median = calc_grades(ax3, quiz2[2])
    posted_title = f"Quiz 2 combined grades: median={median:4.2f}"
    ax3.set(title=posted_title, xlabel="total grade", ylabel="count")

    ax4 = axes[1, 1]
    ax4, median = calc_grades(ax4, quiz2[1])
    posted_title = f"Quiz 2 group grades: median={median:4.2f}"
    ax4.set(title=posted_title, xlabel="group grade", ylabel="count")

    ax5 = axes[2, 0]
    ax5, median = calc_grades(ax5, quiz3[2])
    posted_title = f"Quiz 3 combined grades: median={median:4.2f}"
    ax5.set(title=posted_title, xlabel="total grade", ylabel="count")

    ax6 = axes[2, 1]
    ax6, median = calc_grades(ax6, quiz3[1])
    posted_title = f"Quiz 3 group grades: median={median:4.2f}"
    ax6.set(title=posted_title, xlabel="group grade", ylabel="count")

    fig.savefig("quiz3_marks.png")
    plt.show()


main()
