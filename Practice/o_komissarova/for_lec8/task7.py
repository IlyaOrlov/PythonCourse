from pathlib import Path


def copy_file(source, destination):
    content = ""
    with open(source, 'r') as f:
        content = f.read()
    with open(destination, 'x') as f:
        f.write(content)
