#Замена пробелов на табы в файле
f = open("SpcOnTab.txt", 'w')
f.write('Кожушко    Андрей    Андреевич')
f.close()
f = open("tab&str.txt", 'r+')
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
f.close()


#Замена табов на прбелы в файле
f = open("TabOnSpc.txt", 'w')
f.write('Кожушко\tАндрей\tАндреевич')
f.close()
f = open("tab&str.txt", 'r+')
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
        i+= 1
    x = ''
    a = x.join(a)
    print(a)

space_and_tab(a)
f.close()