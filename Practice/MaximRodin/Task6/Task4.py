from itertools import combinations

pas = 'password'

com = list(combinations(pas,4))
print(com)


from itertools import chain
def massiv(fir, sec, thr):
    new_mass = list(chain(fir, sec, thr))
    return new_mass

print(massiv([1,2,3],[4,5],[6,7]))


from itertools import filterfalse

mass = ['hello', 'i', 'write', 'cool', 'code']

def func(a):
    return len(a)<5


new_mass = list(filterfalse(func, mass))
print(new_mass)



