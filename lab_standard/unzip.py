import zipfile

with zipfile.ZipFile('myFiles.zip') as zipped_files:
    zipped_files.extractall('myFiles')