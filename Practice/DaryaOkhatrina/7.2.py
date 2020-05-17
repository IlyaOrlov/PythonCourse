import subprocess



file = 'test2.txt'

def func(file):
    subprocess.call(['type', 'test2.txt'], shell=True)

func(file)

