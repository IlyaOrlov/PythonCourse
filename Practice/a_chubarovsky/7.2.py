import subprocess as sp


def file_reader(file_name):
    sp.run(['type', file_name], shell=True)


if __name__ == '__main__':
    file_reader('My_file.txt')
