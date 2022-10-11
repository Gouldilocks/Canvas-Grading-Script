#!/bin/bash

# This script will unzip all the files in the ./Data directory and then remove the zip files
for file in ./Data/*.zip
do
    fileWithoutExtension="${file%.*}"
    unzip $file -d $fileWithoutExtension
    rm $file
done