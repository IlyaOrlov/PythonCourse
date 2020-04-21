import os
import shutil as sh
import datetime as dt


def search_and_delete(some_path):
    for root, dirs, files in os.walk(some_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            file_exist_time = dt.datetime.now() - dt.datetime.fromtimestamp(
                os.path.getctime(file_path))  # время существования файла
            diff_time = dt.datetime.fromtimestamp(os.path.getctime(file_path)) - dt.datetime.fromtimestamp(
                os.path.getctime(root))  # разница во времени существования папки и вложенных в неё файлов
            if file_exist_time > dt.timedelta(seconds=60):
                os.remove(file_path)
            elif diff_time > dt.timedelta(seconds=60) and file_path != some_path:
                upper_file = os.path.split(root)
                sh.move(file_path, upper_file[0])  # перемещение файла на уровень выше
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            dir_exist_time = dt.datetime.now() - dt.datetime.fromtimestamp(os.path.getctime(dir_path))
            diff_time = dt.datetime.fromtimestamp(os.path.getctime(dir_path)) - dt.datetime.fromtimestamp(
                os.path.getctime(root))  # разница во времени существования папки и вложенных в неё папок
            if dir_exist_time > dt.timedelta(seconds=120):
                os.rmdir(dir_path)
            elif diff_time > dt.timedelta(seconds=90) and dir_path != some_path:
                upper_dir = os.path.split(root)
                sh.move(dir_path, upper_dir[0])  # перемещение файла на уровень выше


if __name__ == '__main__':
    path = r'C:\\Users\Current\PycharmProjects\myproject\dir_to_delete'
    while True:
        search_and_delete(path)
