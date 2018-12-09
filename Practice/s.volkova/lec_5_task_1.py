#for Python 3.6
#lecture 5 task 1

def chargen():
    while True:
        for c in '0123456789':
            yield c
#words = [c+c for c in chargen()][: 10 ]

#Ошибка: в функции не предусмотрен выход из цикла

def chargen(arg):
    ''' Функция генерирует по одному символу из строки. 
    Дойдя до конца строки, функция начинает с начала.
    Аргумент задает, сколько символов необходимо сгенерировать.
    '''
    n = 0
    for i in range (0, arg):
        if n == 10:
            n = 0
        yield '0123456789'[n]
        n += 1
        
if __name__ == '__main__':
    words = [c+c for c in chargen(10)]
    print(words)


