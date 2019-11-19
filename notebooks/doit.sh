#!/bin/bash -v
jupyter nbconvert --to pdf quiz2_2019t1.ipynb
mkdir -p _build
rsync media* _build/.
cp *html _build/.


