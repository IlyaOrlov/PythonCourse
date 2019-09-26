a = {'first': 'Hello', 'second': 'big', 'third': 'world!'}


def string(str):

    for words in a:
        str = str.replace(words, a[words])
    return str


print(string('first second third'))