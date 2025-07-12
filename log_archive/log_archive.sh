#!/bin/bash

read -rp "Enter the path to the directory you want to compress: " sources_dir

if [[ ! -d "$source_dir"]]; then
    echo "Error: '$source_dir' is not a valid directory."
    exit 1
fi

dir_name=$(basename "$source_dir")

read -rp "Enter archive name (without the extension) or press enter for default: " archive_name

if [[ -z "$archive_name"]]; then
    timestamp=$(date +%Y%m%d_%H%M%S)
    archive_name="${dir_name}_${timestamp}"
fi
