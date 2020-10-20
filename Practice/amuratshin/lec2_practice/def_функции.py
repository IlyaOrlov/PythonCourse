def test(a: int, b=3, c=98):
    """ а - позиционный аргумент с явно указанным типом
    b и c является аргументом со значением по умолчанию """
    print('\n', "a: {}".format(a), "b: {}".format(b), "c: {}".format(c), '\n')


test(1, 4)   # a = 1   b присваивается 4 вместо 3 по молчанию
test(64)     # a = 64  b = 3 т.к второй аргумент не указан при вызове функции
test(1, c=2, b=0)   # а=1 для позиционного аргумента значение передается по его позиции,
# с=2 и b=0 можно передавать не учитывая их позиции


def test_args(a, b=1+3, *args):
    """ *args - формальный позиционный аргумент способный
    принимать любые данные/типы неопределенного количества"""
    print('\n', "a: {}".format(a), "b: {}".format(b), "*args: {}".format(args))


test_args(8, 0, [2, 6, 100])    # а=8, b=0, в *args передан список [2, 6, 100]


def test_kwargs(a: int, c=True, *args, **kwargs):
    """ ***kwargs - аргумент примимающий несколько аргументов в виде словаря
    где аргументы это ключевые слова словаря,
    а их значения - соответствующие значения в словаре"""
    print('\n', "a: {}".format(a), "с: {}".format(c), "*args: {}".format(args))


test_kwargs(33, False, ('start tuple', 3, True, 'end tuple'), {'one': 1, 'two': 2})


def menu(wine, entree='beef', dessert='bagel'):
    print('\n', {'wine': wine, 'entree': entree, 'dessert': dessert})


menu('chardonnay', 'chicken', 'cake')


def nonboggy(arg, result=[]):
    #if result is None:
        result = dict(arg)
        return result
    #else:
    #    print("result is not None")


add = [('wine', 'chardonnay'), ('entree', 'chicken'), ('dessert', 'cake')]
print(nonboggy(add))
print(nonboggy(add))

