def interp_func(s: str, d: dict):  # функция интерполяции
    for k, v in d.items():
        s = s.replace(k, v)
    print(s)


# проверка функции
s = 'Phone: 11 - 22 - 33'
d = {'11': 'double-one',
     '22': 'double-two',
     '33': 'double-three'
     }
interp_func(s, d)