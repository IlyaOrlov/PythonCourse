import os
from pathlib import Path
from Practice.o_komissarova.for_lec8.task7 import copy_file


def copy_dir(source, destination):
    if not Path(source).is_dir():
        raise NotADirectoryError
    if Path(destination).is_dir():
        raise IsADirectoryError
    full_path = str(source).split("/")
    name_of_source_dir = full_path[len(full_path) - 1]
    copy_dir_path = Path(destination).joinpath(name_of_source_dir)
    try:
        os.mkdir(destination)
    except OSError:
        print("Создать директорию %s не удалось" % copy_dir_path)

    for root, dirs, files in os.walk(source):
        for _file in files:
            file_path = Path(source).joinpath(_file)
            file_copy_path = Path(destination).joinpath(_file)
            copy_file(file_path, file_copy_path)
        for _dir in dirs:
            dir_path = Path(source).joinpath(_dir)
            dir_copy_path = Path(destination).joinpath(_dir)
            copy_dir(dir_path, dir_copy_path)


copy_dir('/home/olesya/temporary', '/home/olesya/temporary2')
