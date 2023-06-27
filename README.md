
# File Copy Script

This script allows you to copy files from one folder to another. It was initially designed for local file copying, but it also has planned features for copying files via FTP, SSH, and rsync in the future.

## Features

The current version of the script supports the following features:

-   Copying files from a source directory to a destination directory.
-   Specifying the time interval for the script to run.

### Planned Features

The script will have the following features in future versions:

-   Copying files via FTP.
-   Copying files via SSH.
-   Copying files via rsync.

## Configuration

To use the script, you need to set the following parameters in the `config.json` file:

-   `time_interval_in_minutes`: Set the interval for the script to run in minutes. For example, if `time_interval_in_minutes` is set to 60, the script will run every 1 minute.
-   `source_dir_backup`: Specify the source directory of the files you want to copy.
-   `destination_dir_backup`: Specify the destination directory where you want to copy the files.

### Examples

jsonCopy code

`{
  "time_interval_in_minutes": 60,
  "source_dir_backup": "C:/source_folder",
  "destination_dir_backup": "Z:/destination_folder"
}` 

The `destination_dir_backup` can be one of the following:

-   An external drive.
-   A file storage from a cloud service that is mapped to the local system.
-   A local file server.

## File Filtering

You can specify the allowed file extensions that you want to copy within the `source_dir_backup` folder. By default, the script will copy all files.

## Usage

1.  Set the necessary values in the `config.json` file.
2.  Run the script.

### Note

This script has been compiled into an executable using cx_Freeze for easy use. You only need to set the necessary values in the `config.json` file.

For any further assistance or issues, please refer to the documentation or contact the developer.
