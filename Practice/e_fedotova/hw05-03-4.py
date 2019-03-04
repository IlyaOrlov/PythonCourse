# лекция 4 задание 4

import os.path
def fun(a):
    if os.path.isfile(a):
        fo = open(a)
        f = fo.read()
        print(f)
        fnew = f.replace('    ', '\t')
        print(fnew)
    else:
        print('Вы не указали имя файла')

a = input('Укажите имя файла: ')
fun(a)

