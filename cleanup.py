
import os
from pyunpack import Archive

dirs = ['.']
exts = ['.zip', '.rar']

for item in os.listdir(dirs[0]):
    if item.endswith(tuple(exts)):
        file_name = os.path.abspath(item)
        print("extracting " + str(file_name))
        Archive(file_name).extractall(dirs[0])
        os.remove(file_name)
