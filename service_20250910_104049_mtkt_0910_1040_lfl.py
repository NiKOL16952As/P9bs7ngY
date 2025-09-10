# 代码生成时间: 2025-09-10 10:40:49
import os
import shutil
from datetime import datetime

"""
A Python script to organize the folder structure by moving files into subfolders based on their creation date.

Attributes:
    None

Methods:
    organize_folder(directory): Organizes the given directory by moving files into subfolders by creation date.
"""

class FolderStructureOrganizer:
    def __init__(self, directory):
        """
        Initializes the FolderStructureOrganizer with the specified directory.
        :param directory: The path to the directory that needs to be organized.
        """
        self.directory = directory

    def organize_folder(self):
        """
        Organizes the specified directory by moving files into subfolders based on their creation date.
        """
        try:
            # Get a list of all files in the directory
            files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]

            # Iterate over each file and move it to the corresponding subfolder
            for file in files:
                file_path = os.path.join(self.directory, file)
                # Get the creation date of the file
                creation_date = os.path.getctime(file_path)
                # Convert the creation date to a datetime object
                date = datetime.fromtimestamp(creation_date)
                # Format the date as YYYY-MM
                date_folder = date.strftime('%Y-%m')
                # Create the subfolder if it doesn't exist
                subfolder_path = os.path.join(self.directory, date_folder)
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                # Move the file to the subfolder
                shutil.move(file_path, os.path.join(subfolder_path, file))

            print("Folder structure organized successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    directory_path = input("Enter the path to the directory you want to organize: ")
    organizer = FolderStructureOrganizer(directory_path)
    organizer.organize_folder()