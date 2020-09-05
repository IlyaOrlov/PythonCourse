from pathlib import Path


def copy_file(source, destination):
    str = ""
    with open(source, 'r') as f:
        str = f.read()
    if Path(destination).is_file():
        print("file already exists")
        raise FileExistsError
    else:
        with open(destination, 'w') as f:
            f.write(str)
            print("copy is ready")


copy_file('source.txt', 'destination.txt')
copy_file('source.txt', 'existing_destination.txt')
copy_file('not_a_file.txt', 'destination.txt')