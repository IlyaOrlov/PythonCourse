import subprocess


def read_file(filename):
    subprocess.run(['type', filename], shell=True)


read_file(r"C:\test.txt")
