from pathlib import Path
import shutil
import json
import sys
import os
import time
from datetime import datetime
from tqdm import tqdm

def copy_bak_files(**kwargs):
    source_dir = Path(kwargs.get('source_dir'))
    destination_dir = Path(kwargs.get('destination_dir'))
    allowed_extensions = kwargs.get('allowed_extensions')

    files = os.listdir(source_dir)
    total_files = len(files)
    copied_files = 0  # Counter for copied files

    if total_files == 0:
        return copied_files

    progress_bar = tqdm(total=total_files, desc="Copying files", unit="file", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')

    for file in files:
        if file.endswith(tuple(allowed_extensions)):
            source_file_path = source_dir / file
            destination_file_path = destination_dir / file

            if destination_file_path.exists() and os.path.getsize(source_file_path) <= os.path.getsize(destination_file_path):
                print(f"Skipping file: {file} (already exists or smaller in size)")
                continue

            try:
                shutil.copy2(source_file_path, destination_file_path)
                copied_files += 1
            except shutil.SameFileError:
                print(f"Source and destination files are the same: {file}")
            except IOError as e:
                print(f"Error copying file: {file} - {e}")
            else:
                if os.path.getsize(source_file_path) != os.path.getsize(destination_file_path):
                    print(f"Warning: Copied file size doesn't match source file: {file}")
                else:
                    print(f"Copied file: {file}")

        progress_bar.update(1)  # Update progress bar

    progress_bar.close()

    return copied_files


def main():
    base_directory = Path(os.path.dirname(os.path.abspath(__file__)))
    config_file_path = base_directory / 'config.json'

    if not config_file_path.exists():
        sys.exit("config.json file does not exist")

    with open(config_file_path) as config_file:
        config = json.load(config_file)

    source_backup = config.get('source_dir_backup')
    destination_backup = config.get('destination_dir_backup')
    allowed_extensions = config.get('allowed_extensions')
    time_interval_in_minutes = config.get('time_interval_in_minutes')

    if not source_backup:
        sys.exit("source_dir_backup is invalid or empty")

    if not destination_backup:
        sys.exit("destination_dir_backup is invalid or empty")

    if not allowed_extensions:
        sys.exit("allowed_extensions is invalid or empty")

    is_copying = False  # Flag to track if copying is in progress

    while True:
        if not is_copying:
            kwargs = {
                'source_dir': source_backup,
                'destination_dir': destination_backup,
                'allowed_extensions': allowed_extensions
            }

            copied_files = copy_bak_files(**kwargs)
            current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")

            if copied_files == 0:
                print(f"\nNo backup performed at {current_time}.")
            else:
                print(f"\nBackup completed at {current_time}.")

            is_copying = True  # Set flag to indicate copying is in progress

        # Delay for 2 minutes
        time.sleep(time_interval_in_minutes)

        # Check if copying has finished
        is_copying = False


if __name__ == '__main__':
    main()
