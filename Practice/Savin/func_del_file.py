import os
import time

path_to_folder = r'C:\Users\днс\Desktop\test'


def func(path_to_folder):
    while True:
        for root, subfoldars, files in os.walk(path_to_folder):
            for file in files:
                path = os.path.join(root, file)
                delta = time.time() - os.path.getctime(path)
                if delta > 120:
                    os.remove(path)
            for folder in subfoldars:
                path = os.path.join(root, folder)
                delta = time.time() - os.path.getctime(path)
                if delta > 120 and len(os.listdir(path)) == 0:
                    os.rmdir(path)

func(path_to_folder)

