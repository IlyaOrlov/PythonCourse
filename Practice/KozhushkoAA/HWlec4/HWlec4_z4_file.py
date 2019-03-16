# Замена пробелов на табы в файле
with open("SpcOnTab.txt", 'w') as f:
    f.write('    Кожушко    Андрей    Андреевич    ')
with open("SpcOnTab.txt", 'r+') as f:
    a = f.readline()


def space_and_tab(a):
    a = list(a)
    i = 0
    while i < len(a):
        if a[i] == '\t':
            a[i] = '    '
        elif a[i:(i+4)] == [' ', ' ', ' ', ' ']:
            del a[(i+1):(i+4)]
            a[i] = '\t'
        i += 1
    x = ''
    a = x.join(a)
    print(a)


space_and_tab(a)

#Замена табов на прбелы в файле
with open("TabOnSpc.txt", 'w') as f:
    f.write('\tКожушко\tАндрей\tАндреевич\t')
with open("TabOnSpc.txt", 'r+') as f:
    a = f.readline()


space_and_tab(a)
# Переписал программу:
# 1) a = f.readlines() исправлено на a = f.readline(), теперь
#    "a" получается списком из нескольких элементов;
# 2) Согласен, два раза определять функцию незачем, поэтому для
#    второго случая функция просто вызывается.