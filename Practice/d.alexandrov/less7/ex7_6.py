import re


def my_format(st, *args):
    if re.search(r"\{\d+\}", st) is not None and re.search(r"\{\}", st) is not None:
        raise ValueError
    if re.search(r"\{\d+\}", st) is None and re.search(r"\{\}", st) is None:
        raise ValueError
    if re.search(r"\{\d+\}", st) is None:
        st_splitted = re.split(r"\{\}", st)
        st = ""
        for i in range(0, len(st_splitted) - 1):
            st += st_splitted[i] + args[i]
        st += st_splitted[len(st_splitted) - 1]
    else:
        for i in range(0, len(args)):
            st = re.sub(r"\{"+str(i)+"\}", args[i], st)
    return st


print(my_format('{1}, {0}, {2}, {0}', 'a', 'b', 'c'))
print(my_format('{1}, {0}', 'a', 'b', 'c'))
print(my_format('{1}, {0}, {2}, {3}', 'a', 'b', 'c'))
print(my_format('{} is {}.', '1', 'digit', '2'))
#print(my_format('{} is {}.', '1'))
#print(my_format(' is ', "1"))
#print(my_format('{0} is {}', '1', 'digit'))
