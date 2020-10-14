from multiprocessing import Process
import random

def sum_other_type(a, b):
    if type(a) == int and type(b) == int:
        return a+b
    elif type(a) == int and type(b) == str:
        return str(a) + b
    elif type(a) == str and type(b) == int:
        return a + str(b)
    elif type(a) == list and type(b) == str:
        a.append(b)
        return a
    elif type(a) == str and type(b) == list:
        b.append(a)
        return b
    elif type(a) == int and type(b) == list:
        b.append(a)
        return b
    elif type(a) == list and type(b) == int:
        a.append(b)
        return a
    else:
        return a + b


a1 = 5
b1 = 6
a2 = 'HaH'
b2 = 'Ha'
a3 = [1, 2, 3, 'fg', 'fh']
b3 = [4, 5, 6, 'hg', 'kl']

if __name__ == '__main__':
    ps = []
    my_args = [a1, b1, a2, b2, a3, b3]
    for i in range(10):
        proc = Process(target=sum_other_type, args=(random.choice(my_args), random.choice(my_args)))
        proc.start()
        ps.append(proc)

    for i in ps:
        i.join()

