# С помощью библиотеки subprocess прочитать содержимое произвольного файла с использованием утилиты cat в Linux
# или type в Windows (имя файла должно передаваться как параметр в вашу функцию).

from subprocess import Popen, PIPE
import sys

def myProg(pathFile):
    proc = Popen(['type', pathFile], stdout=PIPE, stderr=PIPE, shell=True)
    proc.wait() # дождаться выполнения
    text = proc.communicate() # получить tuple('stdout', 'stderr')
    if proc.returncode:
        print(text[1])
    print(text[0])

myProg(sys.argv[1])
