def zamena():
    lst = []
    f = open(r'C:\downlods\Пример_1.txt', 'r+')
    for i in f:
        if g == 1:
            i = i.replace('\\t', '    ')
            lst.append(i)
            print(lst)
        elif g == 2:
            i = i.replace('\\t', '    ')
            lst.append(i)
            print(lst)
    f.close()

g = input('Введите число 1 (замена табуляции) или 2 (замена пробелов): ')  # строка в файле'\tspa\t\tmg    hdfdf fgfg\t'
zamena()