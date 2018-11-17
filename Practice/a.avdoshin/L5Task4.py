import itertools

for i in itertools.combinations('password', 4):
    print(i)


def check(*val):
    if len(val) > 4:
        res = ''
        for i in val:
            res += i
        print(res, end=' ')


mass = ['hello', 'i', 'write', 'cool', 'code']
for i in itertools.starmap(check, mass):
    pass

mass = [[1, 2, 3], [4, 5], [6, 7]]
for i in itertools.accumulate(mass):
    result = i
print(result)
