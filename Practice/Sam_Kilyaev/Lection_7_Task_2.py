import sys
import subprocess

file = ''


def read_type(file):
    proc = subprocess.Popen(['type', file], shell=True)
    proc.wait()
    result = proc.communicate()
    if proc.returncode:
        print(result[1])
    return 'result', result[0]


if __name__ == '__main__':
    count = 0
    for param in sys.argv:
        if count == 1:
            file = param
        elif count >= 2:
            print('Extra file')
        count += 1
read_type(file)
