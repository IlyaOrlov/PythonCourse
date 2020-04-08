def zamena(self,number):
    self.number=number
    lst = []
    f = open(r'C:\downlods\Пример_1.txt', 'r+')
    for i in f:
        if  self.number == 1:
            i = i.replace('\\t', '    ')
            lst.append(i)
            print(lst)
        elif  self.number == 2:
            i = i.replace('\\t', '    ')
            lst.append(i)
            print(lst)
    f.close()

number = input('Введите число 1 (замена табуляции) или 2 (замена пробелов): ')  # строка в файле'\tspa\t\tmg    hdfdf fgfg\t'
zamena(number)