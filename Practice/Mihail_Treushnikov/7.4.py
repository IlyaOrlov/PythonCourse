import os
import datetime
import shutil

def delete_file(path):
    while True:
        for root, dirs, files in os.walk(path):
            for _file in files:
                path_to_current_file = os.path.join(root, _file)
                creation_time = datetime.datetime.fromtimestamp(os.path.getctime(path_to_current_file))
                difference = datetime.datetime.now() - creation_time
                if difference > datetime.timedelta(seconds=60):
                    os.remove(path_to_current_file)

            for _dir in dirs:
                path_to_current_dir = os.path.join(root, _dir)
                creation_time = datetime.datetime.fromtimestamp(os.path.getctime(path_to_current_dir))
                difference = datetime.datetime.now() - creation_time
                if difference > datetime.timedelta(seconds=120):
                    shutil.rmtree(path_to_current_dir)

delete_file('/Users/mihailtreushnikov/Desktop/forPython')