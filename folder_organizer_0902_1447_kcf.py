# 代码生成时间: 2025-09-02 14:47:35
import os
import shutil
from pathlib import Path

"""
Folder Organizer is a Python script that organizes files in a specified directory.
It moves all files to their respective folders based on file extensions.
"""


class FolderOrganizer:
    def __init__(self, root_directory):
        """
        Initializes the FolderOrganizer with the root directory.
        :param root_directory: The path to the directory to organize.
        """
        self.root_directory = Path(root_directory)
        if not self.root_directory.exists():
            raise FileNotFoundError(f"The directory {root_directory} does not exist.")
        if not self.root_directory.is_dir():
            raise NotADirectoryError(f"The path {root_directory} is not a directory.")

    def create_folders(self):
        """
        Creates folders for each file extension in the root directory.
        """
        for file in self.root_directory.glob('*.*'):
            file_extension = file.suffix[1:]
            if file_extension:
                folder_path = self.root_directory / file_extension
                folder_path.mkdir(exist_ok=True)

    def organize_files(self):
        """
        Organizes files by moving them to their respective folders.
        """
        for file in self.root_directory.glob('*.*'):
            try:
                file_extension = file.suffix[1:]
                if file_extension:
                    folder_path = self.root_directory / file_extension
                    shutil.move(str(file), str(folder_path / file.name))
            except Exception as e:
                print(f"Error moving file {file}: {e}")

    def run(self):
        """
        Runs the folder organizer by creating folders and organizing files.
        """
        self.create_folders()
        self.organize_files()

if __name__ == '__main__':
    # Specify the root directory to organize
    root_dir = '/path/to/your/directory'
    
    # Create an instance of FolderOrganizer
    organizer = FolderOrganizer(root_dir)
    
    # Run the folder organizer
    organizer.run()