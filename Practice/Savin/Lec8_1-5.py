# Задание 1
def my_len(stroka):
    counter = 0
    for i in stroka:
        counter += 1
    return counter
a = [1, 2, 3, 4]
print(len(a))

# Задание 2
def my_reversed(stroka):
    return stroka[::-1]

a = [1, 2, 3]
b = 'ABCD'
print((my_reversed(a)))
print((my_reversed(b)))

# Задание 3
def my_range(a=None, b=None, c=None):
    if a == None and b == None and c == None:
        raise TypeError('range expected 1 arguments, got 0')
    elif b == None and c == None:
        start, stop, step = 0, a, 1
    elif c == None:
        start, stop, step = a, b, 1
    else:
        start, stop, step = a, b, c
    if type(start) != int or type(stop) != int or type(step) != int:
        raise TypeError('Object cannot be interpreted as an integer')
    if step == 0:
        raise ValueError('range() arg 3 must not be zero')
    elif start < stop and step > 0:
        current_value  = start
        while current_value < stop:
            yield current_value
            current_value += step
    elif start > stop and step < 0:
        current_value = start
        while current_value > stop:
            yield current_value
            current_value += step

for i in my_range(5):
    print(i, end=' ')
print()
# Задание 4
def to_title(stroka):
    new_stroka = []
    i = 0
    if stroka[0].isalpha():
        new_stroka.append(stroka[0].upper())
        i = 1
    while i < len(stroka):
        if stroka[i] == ' ' and stroka[i+1].isalpha():
            new_stroka.append(stroka[i])
            new_stroka.append(stroka[i+1].upper())
            i += 2
            continue
        else:
            new_stroka.append(stroka[i])
            i += 1
    return ''.join(new_stroka)

stroka = to_title('orlov ilya evgenyevich')
print(stroka)

# Задание 5
def count_symbol(stroka, symbol):
    counter = 0
    for i in stroka:
        if i == symbol:
            counter += 1
    return counter

print(count_symbol('Hi, Elvis, I am here', 'i'))