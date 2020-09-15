from subprocess import Popen, PIPE


def read_file(file_name):
    proc = Popen(['cat', file_name], stdout=PIPE, stderr=PIPE)
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1])
    print(res[0])


read_file('text.txt')
