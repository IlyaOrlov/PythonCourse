def my_range(start=0, stop=None, step=1):
    if step > 0:
        if start < stop:

        #a = [start]

            while start < stop:
                #a.append(start + step)
                a = start + step
                start += step
                yield a
        else:
            return 'Error!!!'
    elif step < 0:
        #a = [start]
        while start > stop:
            #a.append(start + step)
            a = start + step
            start += step
            yield a
    elif step == 0:
        return 'Error, step = 0!'

    return a


# print(my_range(1, 10, 1))


# print(my_range(2, -6, -2))

# print(my_range(0, 10, 0))
print(range(10))
for i in my_range(2, -6, 2):
    print(i)
