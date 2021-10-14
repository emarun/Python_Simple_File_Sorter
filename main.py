#!usr/bin/python3
# Script to classify files in a folder based on the file extensions.

# Importing all required libraries.
import os
import time
import shutil   # For moving and copying files
from tkinter import filedialog
from tkinter import *


def try_moving_file(file_path, file_path_without_extension, file_extension, new_path):
    try:
        shutil.move(file_path, new_path)
    except:
        # If same file name exists, then rename the file name.
        # Convert file name -> file name with current time at the end.
        # Eg: people.txt -> people21211235-2323.txt
        new_name = file_path_without_extension + str(time.time()).replace('.', '-') + "." + file_extension
        os.rename(file_path, new_name)
        shutil.move(new_name, new_path)


root = Tk()
root.withdraw()  # To cancel poping out of the tkinter window.

# Select the directory to classify the files.
dir_to_sort = filedialog.askdirectory(initialdir = os.getcwd(), title = 'Select the folder to classify')

# Select the directory to move classified files.
dir_to_move = filedialog.askdirectory(title = "Select folder to move")
dir_to_move = os.path.join(dir_to_move, 'Sorted_Files')
# Making a folder named "Sorted_Files"
try:
    os.makedirs(dir_to_move)
except:
    pass

file_extension_set = set()  # Set to store the file extensions.

# Looping through files and folder in the input folder.
# And getting the file extension, and move file to the corresponding output folder.
for root_dir, sub_dir, file_list in os.walk(dir_to_sort):
    if file_list != []:
        for file in file_list:
            file_path = os.path.join(root_dir, file)

            # Getting file extension.
            file_path_without_extension, file_extension = os.path.splitext(
                file_path)
            file_extension = file_extension.lower()
            if file_extension != '':
                file_extension = file_extension.replace('.', '')
                new_path = os.path.join(dir_to_move, file_extension)
                if file_extension in file_extension_set:
                    try_moving_file(
                        file_path, file_path_without_extension, file_extension, new_path)
                else:
                    os.mkdir(new_path)
                    file_extension_set.add(file_extension)
                    try_moving_file(
                        file_path, file_path_without_extension, file_extension, new_path)

print("Files classified successfully.")
