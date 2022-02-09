__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile


def clean_cache():
    parent_dir = os.getcwd()
    new_dir = "cache"
    path = os.path.join(parent_dir, new_dir)
    if not os.path.exists(path):
        os.mkdir(path)
    elif len(os.listdir(path)) != 0:
        for file in os.scandir(path):
            os.remove(file.path)


def cache_zip(zip_file_path, cache_dir_path):
    zip_file = zipfile.ZipFile(zip_file_path)
    zip_file.extractall(cache_dir_path)


def cached_files():
    parent_dir = os.getcwd()
    new_dir = "cache"
    path = os.path.join(parent_dir, new_dir)
    file_names = os.listdir(path)
    cached_file_list = []
    for name in file_names:
        cached_file_list.append(os.path.abspath(os.path.join(path, name)))
    return cached_file_list


def find_password(cached_file_list):
    for file in cached_file_list:
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            if "password" in line:
                line.replace("password: ", "")
                line.strip()
                return line
        f.close()
