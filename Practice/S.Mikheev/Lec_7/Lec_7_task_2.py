from subprocess import Popen


def readfile(name_file):
    process = Popen(['type', name_file], shell=True)
    process.wait()
    res = process.communicate()
    if process.returncode:
        return res


readfile('Lec_7_task_1.py')
