#!/bin/bash -v
mkdir -p _build
rsync media* _build/.
cp *html _build/.


