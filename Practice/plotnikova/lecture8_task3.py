#Написать реализацию функции range она может принимать от одного
# до трех аргументов при этом аргументами должны быть целые числа
# int range старт стоп шаг так выглядит стандартный вызов
# функции range в Python По умолчанию старт равняется нулю, шаг
# единице Возвращает список целых чисел в форме старт старт шаг
# старт шаг 2 Если шаг положительное число, последним
# элементом списка будет наибольшее старт i шаг меньшее числа
# стоп Если шаг отрицательное число, то последний элемент будет
# наименьшее старт i шаг большее числа стоп Предусмотреть
# случаи ошибочных аргументов ( шаг 0


def my_range(start, stop = None, step=1):
    if stop == None:
        stop = start
        start=0
    if  isinstance(start, int) and isinstance(step, int) and isinstance(stop, int):
        res = []
        i = 0
        while True:
            d=start + i * step
            if (step < 0 and d <= stop) or (step > 0 and d >= stop):
                break
            res.append(d)
            i+=1
    else:
        res="Ошибка! Stop, star, step - должны быть целыми числами."
    return res


a=my_range(-10,10,1)
print(a)


