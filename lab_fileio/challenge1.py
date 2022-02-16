import os
import sys

file_name = sys.argv[1]
file = open(file_name, 'r')

for line in file:
    parent_dir = "sea_creatures"
    # dir = line.rstrip("\r\n")
    dir = line
    os.makedirs(os.path.join(parent_dir, dir ), exist_ok= True)
file.close()
print('created directories')
