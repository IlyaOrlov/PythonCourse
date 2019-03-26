def mylen(list_arg):
    res = 0
    for i in list_arg:
        res += 1
    return res

def myrange(start=0, stop=None, step=1):
     if not stop:
         stop = start
         start = 0
     if step == 0:
         f = lambda a, b: False
     elif step > 0:
         f = lambda a, b: a < b
     else:
         f = lambda a, b: a > b
     i = start
     l = []
     while f(i, stop):
         l.append(i)
         i += step
     return l