d = {'test': 'qwerty', 'python': 'abcd', 'new': 'old'}


def interstring(str):
    str = str.lower()
    lst = str.split()
    for elem in lst:
        if elem in d:
            str = str.replace(elem, d[elem])
    return str


print(interstring('This is my first test on a python. '
                  'Python is a new programming language for me and this test for experience.'))
