#!/usr/bin/python3
import glob
import os
from pathlib import Path, PurePosixPath

files = glob.glob('/home/bkk/Pictures' + '/**/*.*', recursive=True)
filesToDelete = []

# detect files for deletion
for f in files:
    if (PurePosixPath(f).suffix == '.jpg') and str(PurePosixPath(f).with_suffix('.HEIC')) in files:
        print(f + '\n')
        filesToDelete.append(f)
    if (PurePosixPath(f).suffix == '.MOV') and str(PurePosixPath(f).with_stem(PurePosixPath(f).stem + '_HEVC')) in files:
        print(f + '\n')
        filesToDelete.append(f)

print(str(len(filesToDelete)) + ' files to delete in total\n')

# delete files
for f in filesToDelete:
    print('deleting' + f + '\n')
    os.remove(f)
