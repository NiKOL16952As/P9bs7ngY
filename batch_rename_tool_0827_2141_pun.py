# 代码生成时间: 2025-08-27 21:41:50
import os
import requests
from pathlib import Path

"""
A batch file rename tool using Python and Requests framework.
This tool allows renaming multiple files in a directory with a given pattern.
"""

class BatchRenameTool:
    def __init__(self, source_dir, destination_dir):
        """
        Initializes the BatchRenameTool with source and destination directories.
        :param source_dir: The directory containing the files to be renamed.
        :param destination_dir: The directory where renamed files will be moved.
        """
        self.source_dir = Path(source_dir)
        self.destination_dir = Path(destination_dir)

        if not self.source_dir.exists():
            raise ValueError(f'Source directory {source_dir} does not exist.')
        if not self.destination_dir.exists():
            self.destination_dir.mkdir(parents=True)

    def rename_files(self, pattern):
        """
        Renames all files in the source directory according to the given pattern.
        :param pattern: A string pattern to rename files.
        """
        for file in self.source_dir.iterdir():
            if file.is_file():
                new_name = self._generate_new_name(file, pattern)
                self._rename_file(file, new_name)

    def _generate_new_name(self, file, pattern):
        """
        Generates a new file name based on the given pattern and file information.
        :param file: The file to be renamed.
        :param pattern: A string pattern to rename files.
        :return: The new file name.
        """
        return f"{pattern}_{file.stem}{file.suffix}"

    def _rename_file(self, file, new_name):
        """
        Renames a file and moves it to the destination directory.
        :param file: The file to be renamed.
        :param new_name: The new name for the file.
        """
        try:
            new_path = self.destination_dir / new_name
            file.rename(new_path)
            print(f'Renamed {file.name} to {new_name}')
        except OSError as e:
            print(f'Error renaming {file.name}: {e}')

# Example usage
if __name__ == '__main__':
    source_dir = 'path/to/source/directory'
    destination_dir = 'path/to/destination/directory'
    pattern = 'new_pattern'

    rename_tool = BatchRenameTool(source_dir, destination_dir)
    rename_tool.rename_files(pattern)