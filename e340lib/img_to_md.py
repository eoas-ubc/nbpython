import re
from pathlib import Path
from PIL import Image
import PIL

#I have exactly the problem of @amueller on the image size issue. I end up in writing a 
#simple script with the following functions to convert between ![](){width=..} and <img></img> syntax.
# https://github.com/jupyter/notebook/issues/1095

re_mdimg = re.compile(r"(!\[([^\]]*)\]\(([^\)]*)\)\{(.+?)\})")
re_imgtag = re.compile(r"(<img ([^>]*?)(?:/>|>(.*?)</img>))")


def imgtag_to_mdimg(para):
    """
    convert  # <img src="./media/image1.png" style="width:5.27in;height:4.0in" />

    to:

    

    Parameters
    ----------

    para: string
 
    """
    for (match, opts, tag) in re_imgtag.findall(para):
        tag = tag if tag else ""
        l = re.search(r"""src\s*=\s*["'](\S*?)["']""", opts)
        w = re.search(r"""width\s*[=:]\s*["']?(\S+?)["'; ]""", opts)
        h = re.search(r"""height\s*[=:]\s*["']?(\S+?)["'; ]""", opts)
        style_opts = ""
        style_opts = "width=%s" % w.group(1) if w else ""
        if h:
            if style_opts:
                style_opts = style_opts + " "
            style_opts = style_opts + "height=%s" % h.group(1)
        para = para.replace(
            match,
            "![%s](%s){%s}" % (tag, l.group(1), style_opts))
    return para

def dump_image_data(para):
    for (match, opts, tag) in re_imgtag.findall(para):
        tag = tag if tag else ""
        l = re.search(r"""src\s*=\s*["'](\S*?)["']""", opts)
        w = re.search(r"""width\s*[=:]\s*["']?(\S+?)["'; ]""", opts)
        h = re.search(r"""height\s*[=:]\s*["']?(\S+?)["'; ]""", opts)
    if l:
        print(l.group(1))
    if h:
        print(h.group(1))
    if w:
        print(w.group(1))
        
 
def shrinkit(in_fig_file,out_fig_path,scale_factor):
    in_fig_file = Path(in_fig_file)
    out_fig_path = Path(out_fig_path)
    with Image.open(in_fig_file) as im:
        old_width,old_height=im.size
        new_width = int(old_width*scale_factor)
        new_height = int(old_height*scale_factor)
        new_img = im.resize((new_width,new_height),resample = PIL.Image.LANCZOS)
        percent=int(100*scale_factor)
        new_name = f"{in_fig_file.stem}.png"
        full_path = out_fig_path / new_name
        new_img.save(full_path,'PNG')
    with Image.open(full_path) as im:
        width, height = im.size

    print((f"wrote new file {full_path}\n"
           f"scaled by {scale_factor}\n"
           f"orig dimensions {old_width} x {old_height}\n"
           f"new dimensions {width} x {height}"))

