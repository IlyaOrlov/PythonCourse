d = {'test': 'qwerty', 'python': 'abcd', 'new': 'old'}


def interstring(str):
    str = str.lower()
    for elem in d:
        str = str.replace(elem, d[elem])
    return str


print(interstring('This is my first testing on a python. '
                  'Python is a new programming language for me and this test for experience.'))
