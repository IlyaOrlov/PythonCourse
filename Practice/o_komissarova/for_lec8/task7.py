from pathlib import Path


def copy_file(source, destination):
    str = ""
    with open(source, 'r') as f:
        str = f.read()
    with open(destination, 'x') as f:
        f.write(str)
        print("copy is ready")
