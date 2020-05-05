import os
import shutil
import time


def cleaner(path):
    while True:
        for working_dir, dirs, files in os.walk(path):
            for f in files:
                if (time.time() - os.path.getctime(os.path.join(working_dir, f))) > 60:
                    os.remove(os.path.join(working_dir, f))
            for d in dirs:
                if (time.time() - os.path.getctime(os.path.join(working_dir, d))) > 120:
                    shutil.rmtree(os.path.join(working_dir, d))


cleaner('dir')
