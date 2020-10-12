from multiprocessing import Process


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
p1 = Process(name='p1', target=sum_other_type, args=(a1, b1))
p2 = Process(name='p2', target=sum_other_type, args=(a2, b2))
p3 = Process(name='p3', target=sum_other_type, args=(a3, b3))
p4 = Process(name='p4', target=sum_other_type, args=(a1, b2))
p5 = Process(name='p5', target=sum_other_type, args=(a2, b3))
p6 = Process(name='p6', target=sum_other_type, args=(a3, b1))

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()

