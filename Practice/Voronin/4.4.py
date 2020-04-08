def fun(i):
    print(i.replace('\t', '   '))


def fun2(i):
    print(i.replace('    ', '\t'))


f = open('myFile.txt')
cmd = int(input('Введите 1 - для замены табуляции на пробел, 2 - для замены пробела на табуляцию: '))
if cmd == 1:
    for line in f:
        fun(line)
elif cmd == 2:
    for line in f:
        fun2(line)
else:
    print('Неизвестная команда')
f.close()


t = input('Введите текст:')
fun(t)
fun2(t)
