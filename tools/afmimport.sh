#!/usr/bin/env bash

i=$1

mkdir $i
# TODO fix the instrument name in the file
cp bass/_index.md $i/
pushd $i
mv ~/Downloads/afmlocal500.wordpress.2018-06-15.xml data.xml
afmparse.py
ls
popd

echo "" >> _index.md
echo "[$i]($i/)" >> _index.md
