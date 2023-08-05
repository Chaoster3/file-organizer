import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".heif"],
    "Videos": [".mov", ".mp4", ".avi"],
    "PDFs": [".pdf"],
    "Excel Spreadsheets": [".xlsm"],
    "Word Documents": [".docx"],
    "PowerPoint Presentations": [".pptx"],
    "CSVs": [".csv"],
    "Zip Files": [".zip"]
}

FILETYPES = {ext: folder
             for folder, exts in CATEGORIES.items()
             for ext in exts
             }


def organize_files(directory):
    os.chdir(directory)
    for file in os.listdir():
        if os.path.isdir(file):
            continue
        _, extension = os.path.splitext(file)
        extension = extension.lower()
        if extension in FILETYPES:
            folder = FILETYPES[extension]
        else:
            folder = "Others"
        if not os.path.exists(os.path.join(directory, folder)):
            os.makedirs(os.path.join(directory, folder))
        shutil.move(file, os.path.join(directory, folder))


print("Please select a folder")
Tk().withdraw()
filepath = askdirectory()
organize_files(filepath)
print("Your folder has been organized!")