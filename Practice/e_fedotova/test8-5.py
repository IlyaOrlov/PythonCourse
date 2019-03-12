def count_symbol(a, b):
    t = tuple(a)
    res = t.count(b)
    return res

a = 'моя длинная строка'
b = 'я'

print(count_symbol(a, b))