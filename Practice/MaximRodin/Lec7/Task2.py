from subprocess import Popen


def readfile(name):
    process = Popen(['type', name], shell=True)
    process.wait()
    res = process.communicate()
    if process.returncode:
        return res


readfile('task2.txt')
