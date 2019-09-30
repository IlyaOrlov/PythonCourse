def my_range(start, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0

### CHECK
    if not isinstance(start, int):
        print('Start is not integer')
        return 'Start = ' + str(start)

    if not isinstance(step, int):
        print('Step is not integer')
        return 'Step = ' + str(step)
    if step == 0:
        return 'Zero step does not provide a range.'
    ### If an increasing range is needed.
    # if step < 0:
    #     start, stop = stop, start

    if not isinstance(stop,int):
        print('Stop is not integer')
        return 'Stop = ' + str(stop)

### BODY
    a = [start]
    if (stop-start) % step == 0:
        kmax = (stop-start)//step
    else:
        kmax = (stop - start) // step + 1

    # print('kmax = '+ str(kmax))
    for k in range(1, kmax):
        a.append(a[k-1] + step)

    return a


### TEST
rng = my_range(15, 3, -2)
print('')
print(rng)

rng = my_range(-4, 7)
print('')
print(rng)