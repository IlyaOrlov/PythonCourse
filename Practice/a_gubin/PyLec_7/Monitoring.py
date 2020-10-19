import os
import shutil
import time
import sys
from datetime import datetime


def is_removable(obj):
    time_life = time.time() - obj.stat().st_ctime
    if obj.is_dir():
        return time_life > 120
    if obj.is_file():
        return time_life > 60
    return False


def remove_item(obj):
    if obj.is_dir():
        shutil.rmtree(obj.path)
        print(f"dir '{os.path.basename(obj.path)}' (full path to => {obj.path}) was deleted at {datetime.now().time()}")
    elif obj.is_file():
        os.remove(obj.path)
        print(f"file '{os.path.basename(obj.path)}' (full path to => {obj.path}) was deleted at {datetime.now().time()}")


def monitoring(root):
    for item in os.scandir(root):
        if is_removable(item):
            remove_item(item)
        else:
            if item.is_dir():
                monitoring(item.path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: the path to the directory not found")
    else:
        if os.path.exists(sys.argv[1]):
            while True:
                monitoring(sys.argv[1])
        else:
            print(f"Path '{sys.argv[1]}' doesn't exist")
