# 22.11 - [ИО]:  Проверено (OK) - 5 баллов из 5 (т.к. без re).
def my_format(instring, *args):
    if '{}' in instring:
        for i in args:
            ndx = instring.index('{}')
            instring = instring[: ndx] + i + instring[ndx+2:]
        return instring

    book = dict()
    for i in range(len(args)):
        book['{'+str(i)+'}'] = args[i]
    for key in book:
        instring = instring.replace(key, book[key])
    return instring


print(my_format('Hi! my name is {2}. I from {1}. I am {0}.', 'programmist',
                'NN', 'Alex'))
print(my_format('Hi! my name is {}. I from {}. I am {}.', 'Alex',
                'NN', 'programmist'))
