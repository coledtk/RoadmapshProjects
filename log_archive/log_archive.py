import os
import tarfile
import shutil
import datetime

def compress_directory(source_dir, output_name):
    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is not a valid directory.")
        return None

    # Ensure proper extension
    if not output_name.endswith('.tar.gz'):
        output_name += '.tar.gz'

    # Store temp archive in /tmp
    archive_path = os.path.join('/tmp', output_name)

    try:
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        print(f"Compressed to: {archive_path}")
        return archive_path
    except Exception as e:
        print(f"Compression failed: {e}")
        return None

def move_to_home(archive_path):
    if not os.path.isfile(archive_path):
        print("Archive file does not exist.")
        return

    dest_path = os.path.join('/home', os.path.basename(archive_path))

    try:
        shutil.move(archive_path, dest_path)
        print(f"Moved archive to: {dest_path}")
    except Exception as e:
        print(f"Move failed: {e}")

if __name__ == '__main__':
    # Prompt user for input
    source_dir = input("Enter the directory to compress: ").strip()

    if not os.path.isdir(source_dir):
        print(f"'{source_dir}' is not a valid directory. Exiting.")
        exit(1)

    custom_name = input("Enter archive name (or leave blank for auto): ").strip()

    if not custom_name:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        custom_name = f"{os.path.basename(source_dir)}_{timestamp}"

    archive_path = compress_directory(source_dir, custom_name)

    if archive_path:
        move_to_home(archive_path)