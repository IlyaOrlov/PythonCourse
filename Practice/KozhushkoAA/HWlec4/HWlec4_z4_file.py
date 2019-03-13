# Замена пробелов на табы в файле
# f = open("SpcOnTab.txt", 'w')
# f.write('    Кожушко    Андрей    Андреевич    ')
# f.close()
# f = open("SpcOnTab.txt", 'r+')
# a = f.readlines()
# Согласен, что менеджер контекста удобнее,
# но это задание к 4 лекции, где менеджер контекста ещё не был изучен.
with open("SpcOnTab.txt", 'w') as f:
    f.write('    Кожушко    Андрей    Андреевич    ')
with open("SpcOnTab.txt", 'r+') as f:
    a = f.readlines()


def space_and_tab(a):
    a = list(a)
    i = 0
    while i < len(a):
        if a[i] == '\t':
            a[i] = '    '
        elif a[i:(i+4)] == [' ', ' ', ' ', ' ']:
            del a[(i+1):(i+4)]
            a[i] = '\t'
        i+= 1
    x = ''
    a = x.join(a)
    print(a)


space_and_tab(a)
# f.close()


#Замена табов на прбелы в файле
#f = open("TabOnSpc.txt", 'w')
#f.write('\tКожушко\tАндрей\tАндреевич\t')
#f.close()
#f = open("TabOnSpc.txt", 'r+')
#a = f.readline()
with open("TabOnSpc.txt", 'w') as f:
    f.write('\tКожушко\tАндрей\tАндреевич\t')
with open("TabOnSpc.txt", 'r+') as f:
    a = f.readlines()


def space_and_tab(a):
    a = list(a)
    i = 0
    while i < len(a):
        if a[i] == '\t':
            a[i] = '    '
        elif a[i:(i+4)] == [' ', ' ', ' ', ' ']:
# Да, сработает, если имеется ввиду именно 4 пробела
# "    Иванов    Иван    Иванович    ".
# С одним пробелом работать и не должно.
            del a[(i+1):(i+4)]
            a[i] = '\t'
        i+= 1
    x = ''
    a = x.join(a)
    print(a)


space_and_tab(a)
# f.close()

# Также нашел ошибку: Имя файла открытого для 'w'
# не соответствовало имени файла открытого для 'r+'
# Исправил