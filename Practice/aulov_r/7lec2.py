import subprocess


def read(file):
    subprocess.run(['type', file], shell=True)


read(r"C:\text.txt")