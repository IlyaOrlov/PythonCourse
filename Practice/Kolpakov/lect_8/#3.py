def my_range(start, stop, step):
    cnt = stop - start
    if start < stop and step > 0:
        while start < stop:
            yield start
            start += step
    elif start > stop and step < 0:
        while start < stop:
            yield start
            start -= step
    elif step == 0:
        yield '!!!step must not be zero!!!'
    else:
        yield None


for i in (my_range(-10, 0, 2)):
    print(i)
