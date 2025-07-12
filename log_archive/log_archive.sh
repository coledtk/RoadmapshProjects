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


# Final output file
archive_path="/tmp/${archive_name}.tar.gz"
final_path="/home/${archive_name}.tar.gz"

# Compress
echo "🗜️  Compressing '$source_dir' to '$archive_path'..."
tar -czf "$archive_path" -C "$(dirname "$source_dir")" "$dir_name"

# Check for success
if [[ $? -ne 0 ]]; then
    echo "❌ Compression failed."
    exit 1
fi

# Move to /home
echo "🚚 Moving archive to /home..."
mv "$archive_path" "$final_path"

# Final check
if [[ $? -eq 0 ]]; then
    echo "✅ Success! Archive saved at: $final_path"
else
    echo "❌ Failed to move archive to /home."
fi