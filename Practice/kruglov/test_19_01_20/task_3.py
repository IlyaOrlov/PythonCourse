# 3 function Myrange


def MyRange(start, end=None, step=1):
    buf = []
    i = 0
    if end is None:
        end, start = start, 0
    if step > 0:
        i = start
        while i < end:
            buf.append(start + i * step)
            i += 1
    elif step < 0:
        if start > end:
            i = end
            while i < start and (start + i * step) > 0:
                buf.append(start + i * step)
                i += 1
        else:
            return "Error: Please reverse arguments 'start' and 'end'"
    else:
        raise ValueError
    return buf


print(MyRange(1, 10, 2))
print(MyRange(0, 0, -2))
print(MyRange(0, 10, 0))
print(MyRange(10, 0, -2))
