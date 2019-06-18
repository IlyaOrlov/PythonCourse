def r(*data):
    if len(data) == 1:
        start = 0
        stop = data[0]
        step = 1
    elif len(data) == 2:
        start = data[0]
        stop = data[1]
        step = 1
    else:
        start = data[0]
        stop = data[1]
        step = data[2]
        if step == 0:
            print ('step input error')
            return 
        
        
    a = []
    i=0
    if step >=1:
        while (start + i * step) < stop:
            a.append(start + i * step)
            i += 1
    elif step <= -1:
        while (start + i * step) > stop:
            a.append(start + i * step)
            i += 1
    print (a)

r(10)
r(2, 10, 2)
r(20, 10, -3)
r(0, 10, 0)