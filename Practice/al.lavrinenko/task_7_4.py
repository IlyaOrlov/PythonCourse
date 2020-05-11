import os
import time
import shutil


target_dir = input()
if not os.path.isdir(target_dir):
    raise OSError('No such directory')
while True:
    for main_dir, sub_dirs, files in os.walk(target_dir):
        for dir_name in sub_dirs:
            path = os.path.join(main_dir, dir_name)
            if (time.time() - os.path.getctime(path)) >= 120:
                shutil.rmtree(path)
        for file_name in files:
            path = os.path.join(main_dir, file_name)
            if (time.time() - os.path.getctime(path)) >= 60:
                os.remove(path)
