import os
import sys


def my_copyfile(src, dst):
    if not os.path.exists(src):
        raise OSError
    if os.path.exists(dst):
        raise OSError
    with open(src, 'rb') as file:
        content = file.read()
    with open(dst, 'wb') as file:
        file.write(content)


if __name__ == "__main__":
    my_copyfile(*sys.argv[1:])
