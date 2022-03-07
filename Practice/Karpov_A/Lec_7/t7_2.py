import subprocess


def read(file):
    subprocess.run(['type', file], shell=True)


read(r"E:\Работы по программированию\Python\DZ_6_lec7\text.txt")