import re


def to_title(string):
    s = set(x for x in re.findall(r" \w", string))
    if string[0].isalpha():
        string = string[0].upper() + string[1:]
    for mo in s:
        string = string.replace(mo, mo.upper())
    return string


if __name__ == "__main__":
    a = "   aaaa  caa raa s"
    b = "bbb b bbbb bb    "
    c = "   ccc   c  c   cc    "
    print(a.title() == to_title(a))
    print(b.title() == to_title(b))
    print(c.title() == to_title(c))
    print(to_title(a))
    print(to_title(b))
    print(to_title(c))
