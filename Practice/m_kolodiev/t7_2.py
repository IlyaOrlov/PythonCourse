import subprocess


def reader(filename):
    file = subprocess.run(['type', filename], shell=True)
    return file


print(reader("test.txt"))
