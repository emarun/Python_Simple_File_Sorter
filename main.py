#!usr/bin/python3
# Script to classify files in a folder based on the file extensions.

# Importing all required libraries.
import os
import time
import shutil   # For moving and copying files
from tkinter import filedialog
from tkinter import *


def try_moving_file(filePath, filePathWithoutExtension, fileExtension, newPath):
    try:
        shutil.move(filePath, newPath)
    except:
        # Convert file name -> file name with current time at the end.
        # Eg: people.txt -> people21211235-2323.txt
        newName = filePathWithoutExtension + \
            str(time.time()).replace('.', '-') + \
            "." + fileExtension
        os.rename(filePath, newName)
        shutil.move(newName, newPath)


root = Tk()
root.withdraw()  # To cancel poping out of the tkinter window.

# Select the directory to classify the files.
dirToSort = filedialog.askdirectory(
    initialdir = os.getcwd(), title = 'Select the folder to classify')

# Select the directory to move classified files.
dirToMove = filedialog.askdirectory(title = "Select folder to move")
dirToMove = os.path.join(dirToMove, 'Sorted_Files')
# Making a folder named "Sorted_Files"
try:
    os.makedirs(dirToMove)
except:
    pass

fileExtensionSet = set()  # Set to store the file extensions.

# Looping through files and folder in the input folder.
# And getting the file extension, and move file to the corresponding output folder.
for rootDir, subDir, fileList in os.walk(dirToSort):
    if fileList != []:
        for file in fileList:
            filePath = os.path.join(rootDir, file)

            # Getting file extension.
            filePathWithoutExtension, fileExtension = os.path.splitext(
                filePath)
            fileExtension = fileExtension.lower()
            if fileExtension != '':
                fileExtension = fileExtension.replace('.', '')
                newPath = os.path.join(dirToMove, fileExtension)
                if fileExtension in fileExtensionSet:
                    try_moving_file(
                        filePath, filePathWithoutExtension, fileExtension, newPath)
                else:
                    os.mkdir(newPath)
                    fileExtensionSet.add(fileExtension)
                    try_moving_file(
                        filePath, filePathWithoutExtension, fileExtension, newPath)

print("Files classified successfully.")
