import os
import shutil
import time


def remover(path):
    while True:
        for current_dir, dirs, files in os.walk(path):
            for file in files:
                delta = time.time() - os.path.getmtime(current_dir + '\\' + file)
                if delta > 60:
                    os.remove(current_dir + '\\' + file)
            for direct in dirs:
                delta2 = time.time() - os.path.getmtime(current_dir + '\\' + direct)
                if delta2 > 120:
                    shutil.rmtree(current_dir + '\\' + direct)


remover("test")
