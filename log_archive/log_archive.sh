#!/bin/bash

# prompts user for input
read -rp "Enter the path to the directory you want to compress: " sources_dir

# catch cases where user doesnt enter a valid directory
if [[ ! -d "$source_dir"]]; then
    echo "Error: '$source_dir' is not a valid directory."
    exit 1
fi

# gets base name of user inputted path
dir_name=$(basename "$source_dir")

# prompt for new archive name
read -rp "Enter archive name (without the extension) or press enter for default: " archive_name

# checks if archive name is empty, then sets it to default with timestamp if user didnt specify a name.
if [[ -z "$archive_name" ]]; then
    timestamp=$(date +%Y%m%d_%H%M%S)
    archive_name="${dir_name}_${timestamp}"
fi


# sets final path with the new file
archive_path="/tmp/${archive_name}.tar.gz"
final_path="/home/${archive_name}.tar.gz"

# actual compressing of the directory -c = create, -z compress using gzip, -f comes before specifying filename
# -C is changes the directory to the directory name that follows it.
echo "Compressing '$source_dir' to '$archive_path'..."
tar -czf "$archive_path" -C "$(dirname "$source_dir")" "$dir_name"

# $? holds the exit code of the last command ran. 0 is success.
if [[ $? -ne 0 ]]; then
    echo "Compression failed."
    exit 1
fi

# Move to /home
echo "Moving archive to /home..."
mv "$archive_path" "$final_path"

# $? holds the exit code of the last command ran. 0 is success.
if [[ $? -eq 0 ]]; then
    echo "Success! Archive saved at: $final_path"
else
    echo "Failed to move archive to /home."
fi