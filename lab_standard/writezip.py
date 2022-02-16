import os
import zipfile
with zipfile.ZipFile('myFiles.zip', 'w') as zipped_files:
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        if file.endswith('.txt'):
            zipped_files.write(file, compress_type = zipfile.ZIP_DEFLATED)