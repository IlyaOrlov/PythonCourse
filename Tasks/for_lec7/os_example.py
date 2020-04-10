import os
import shutil


from subprocess import Popen, PIPE

proc = Popen(['ipconfig'], stdout=PIPE, stderr=PIPE)
proc.wait() # дождаться выполнения
res = proc.communicate() # получить tuple('stdout', 'stderr')
if proc.returncode:
    print(res[1])
print('result:', res[0])
