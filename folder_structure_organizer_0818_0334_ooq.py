# 代码生成时间: 2025-08-18 03:34:49
import os
import shutil
from pathlib import Path
import logging

"""
Folder Structure Organizer

This script organizes the contents of a specified folder into subfolders based on file extensions.
It's designed to maintain the folder structure, making it easier to manage large volumes of files.
"""

class FolderStructureOrganizer:
    def __init__(self, source_folder, destination_folder):
        """
        Initialize the FolderStructureOrganizer with source and destination folders.
        :param source_folder: The path to the folder containing files to organize.
        :param destination_folder: The path to the folder where organized files will be placed.
        """
        self.source_folder = Path(source_folder)
        self.destination_folder = Path(destination_folder)
        self.extensions = {}

    def _create_folder_for_extension(self, extension):
        """
        Creates a folder for a specific file extension if it doesn't exist.
        :param extension: The file extension (e.g., '.txt', '.jpg')
        """
        folder_path = self.destination_folder / extension[1:]  # exclude the dot
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            self.extensions[extension] = folder_path
        return folder_path

    def _move_file(self, file_path):
        """
        Moves a file to the corresponding folder based on its extension.
        :param file_path: The path to the file to be moved.
        """
        extension = file_path.suffix
        if extension in self.extensions:
            dest_folder = self.extensions[extension]
        else:
            dest_folder = self._create_folder_for_extension(extension)
        dest_path = dest_folder / file_path.name
        try:
            shutil.move(str(file_path), str(dest_path))
        except Exception as e:
            logging.error(f"Failed to move file {file_path} to {dest_path}: {e}")

    def organize(self):
        """
        Organizes all files in the source folder into subfolders based on their extensions.
        """
        if not self.source_folder.exists():
            logging.error(f"Source folder {self.source_folder} does not exist.")
            return

        if not self.destination_folder.exists():
            self.destination_folder.mkdir(parents=True)

        for file_path in self.source_folder.iterdir():
            if file_path.is_file():
                self._move_file(file_path)


def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Define source and destination folders
    source_folder = 'path/to/source_folder'
    destination_folder = 'path/to/destination_folder'

    # Create an instance of the FolderStructureOrganizer
    organizer = FolderStructureOrganizer(source_folder, destination_folder)

    # Start the organization process
    organizer.organize()
    logging.info('Folder organization completed.')

if __name__ == '__main__':
    main()