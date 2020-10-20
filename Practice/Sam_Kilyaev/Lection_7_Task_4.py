import os
import datetime
from pathlib import Path


def del_file(new_path):
    os.remove(new_path)
    return f'Delete {new_path}'


def del_dir(new_path):
    os.rmdir(new_path)
    return f'Delete {new_path}'


def del_all(path):
    if os.path.exists(path):
        while True:
            for i in os.listdir(path):
                new_path = os.path.join(path, i)
                time_of_create = datetime.datetime.fromtimestamp(os.path.getctime(new_path))
                min_of_live = (datetime.datetime.now() - time_of_create).seconds // 60
                if os.path.isfile(new_path):
                    if min_of_live >= 1:
                        print(del_file(new_path))
                    else:
                        continue
                elif os.path.isdir(new_path):
                    is_empty1 = not bool(sorted(Path(new_path).rglob('*')))
                    if not is_empty1:
                        if min_of_live >= 1:
                            print(del_file(new_path))
                        else:
                            continue
                    elif is_empty1:
                        if min_of_live >= 2:
                            print(del_dir(new_path))
                        else:
                            continue
            is_empty2 = not bool(sorted(Path(path).rglob('*')))
            if is_empty2:
                break
    else:
        print('Directory does not exist')


if __name__ == "__main__":
    del_all('D:\Python_NIIT\Test_Practic')
