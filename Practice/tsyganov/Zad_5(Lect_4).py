def funk(my_str, my_typle):
    my_str = my_str.split(' ')
    i = 0
    while i < len(my_str):
        if my_str[i] in my_typle:
            my_str[i] = my_typle.get(my_str[i])
            i += 1

    my_str = ' '.join(my_str)
    print(my_str)

my_str = 'Я учусь писать на языке Пайтон'
my_typle = {'Пайчарм': 'Pycharm', 'Пайтон':'Python'}

funk(my_str, my_typle)