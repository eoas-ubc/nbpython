"""
parse a python notebook and write out
a jason file
"""
import re
import argparse
from pathlib import Path
import context
import json
from e340lib.img_to_md import shrinkit


def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip())
    parser.add_argument('infile', type=str, help='path to input notebook')
    parser.add_argument('--outjson', type=str, default= "fig_list.json",
                        help='path to json file')
    return parser

def find_figs(the_file):
    filename = Path(filename).resolve()
    root_dir = the_file.parent
    media_out_path = root_dir / "media_resize"
    media_out_path.mkdir(parents=True,exist_ok=True)
    #  <img src="media_quiz3_2019t1/image2.png" width="25%" />
    re_imgtag = re.compile(r".*<img\s*src=\"(.*?)\"\s+width=\"(.*?)\%\".*/>")
    image_list=[]
    with open(the_file,'r') as infile:
        the_lines = infile.readlines()
        for a_line in the_lines:
            the_match=re_imgtag.match(a_line)
            if the_match:
                print(the_match.groups())
                image_list.append({'filename':the_match.group(1),'size':int(the_match.group(2))})
    return image_list

for item in image_list:
    shrinkit(item['filename'],media_out_path,item['size']*0.01)

with open('fig_list.json','w') as outfile:
    json.dump(image_list,outfile,indent=4)
# run_shrink set1/media/cloud_lift.png set1/media_resize 0.5
# python /Users/phil/repos/nbpython/e340lib/add_cellmeta.py quiz3_2019t1.py  ctype question
