# Написать функцию to_title принимает строку ищет пробелы первые
# буквы после них и после начала строки делает заглавными


def to_title(t):
    d=""
    for i in t.split(" "):
        d = d + " "
        if len(i) != 0:
            d = d + i.capitalize()
    return d[1:] #вырезается лишний пробел в начале строки


text=" dddd  ffff                 "
a= to_title(text)
print(a)

