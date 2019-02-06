from os import listdir,makedirs,rename
from os.path import isfile,exists,join,abspath

currentPath = "."
name_jpg_dir = "JPG"
name_cr_dir = "CR2"

full_jpg_path = join(abspath(currentPath),name_jpg_dir)
full_cr_path = join(abspath(currentPath),name_cr_dir)

if not exists(full_jpg_path):
        makedirs(full_jpg_path)
if not exists(full_cr_path):
        makedirs(full_cr_path)

for i in listdir(currentPath):
        if isfile(i) == True:
                if i.endswith("JPG"):
                        rename(abspath(i),join(full_jpg_path,i))
                elif i.endswith("CR2"):
                        rename(abspath(i),join(full_cr_path,i))
