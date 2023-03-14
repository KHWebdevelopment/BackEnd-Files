__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import shutil

parent_dir = os.path.abspath("files")
dir = "cache"
path = os.path.join(parent_dir, dir)

def clean_cache():
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def cache_zip(zip_path_file: str, dir_path: str):
    zip_path_file = os.path.join(parent_dir,"data.zip")
    dir_path = path
    with zipfile.ZipFile(zip_path_file, "r") as zip_ref:
            zip_ref.extractall(dir_path)

def cached_files():
    absolute_path = os.path.abspath(path)
    list_full_path = []
    for file in os.listdir(absolute_path):
        full_path = os.path.join(absolute_path, file)
        list_full_path.append(full_path)
    return list_full_path                 

def find_password(list_full_path):
    for x in list_full_path:
        with open(x, "r") as file:
            text = file.read()
            if "password" in text:
                list_full_path = text.split("\n")
                for i in list_full_path:
                    if "password" in i:
                        print(i)
                        return i[i.find(" ")+1:]