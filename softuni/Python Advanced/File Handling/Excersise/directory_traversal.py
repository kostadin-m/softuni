from os import walk 
import os

files_ext = {}
dir_path = os.path.dirname(os.path.realpath(__file__))

for _, _, files in walk(dir_path):
    break
for file in files:
    file, ext = file.split('.')
    if ext not in files_ext:
        files_ext[ext] = []
    files_ext[ext].append(file)

for key, value in sorted(files_ext.items()):
    print(f'.{key}')
    print("\n".join([f'- - -{x}.{key}' for x in value]))