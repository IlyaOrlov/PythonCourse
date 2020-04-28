import os
import shutil as sh
import time


def walker(const_path, temp_path, file_or_dir):
    file_or_dir_path = os.path.join(temp_path, file_or_dir)
    file_or_dir_exist_time = time.time() - os.path.getctime(file_or_dir_path)
    diff_time = os.path.getctime(file_or_dir_path) - os.path.getctime(temp_path)  # разница во времени существования
    # папки и вложенных в неё файлов
    if os.path.isfile(file_or_dir):
        if file_or_dir_exist_time > 60:
            os.remove(file_or_dir_path)
        elif diff_time > 60 and file_or_dir_path != const_path:
            upper_file = os.path.split(temp_path)
            sh.move(file_or_dir_path, upper_file[0])  # перемещение файла на уровень выше
    elif os.path.isdir(file_or_dir):
        if file_or_dir_exist_time > 120:
            os.rmdir(file_or_dir_path)
        elif diff_time > 90 and file_or_dir_path != const_path:
            upper_dir = os.path.split(temp_path)
            sh.move(file_or_dir_path, upper_dir[0])  # перемещение папки на уровень выше


def search_and_delete(some_path):
    for root, dirs, files in os.walk(some_path, topdown=False):
        for file in files:
            walker(some_path, root, file)
        for directory in dirs:
            walker(some_path, root, directory)


if __name__ == '__main__':
    path = r'C:\\Users\Current\PycharmProjects\myproject\dir_to_delete'
    while True:
        try:
            search_and_delete(path)
        except KeyboardInterrupt:
            print('Stopped by User.')
