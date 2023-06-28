import sys
from cx_Freeze import setup, Executable

# Replace 'backup_script.py' with the name of your script
script = 'backup_script.py'

# Create an executable
executables = [Executable(script)]

# Build options
build_options = {
    'build_exe': {
        'include_files': [],  # Add any additional files or directories required by your script
    }
}

# Set up the configuration
setup(
    name='Backup Script',
    version='1.0',
    description='Backup script',
    options=build_options,
    executables=executables
)
