#!/bin/bash

cd $1
lng=$2

for file in *.tif; do
  filename="${file%.*}"
  if ! [ -f "${filename}.box" ]; then
    base=`basename $file .tif`
    tesseract $file $base -l $lng --psm 6 wordstrbox
  fi
done

