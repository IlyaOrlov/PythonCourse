import re


def to_title(string):
    return re.sub(r"(^| )\w", lambda mo: mo[0].upper(), string, flags=re.M)


if __name__ == "__main__":
    a = "   aaaa  caa raa s r"
    b = "bbb b bbbb bb    "
    c = "   ccc   c  c   cc    "
    print(a.title() == to_title(a))
    print(b.title() == to_title(b))
    print(c.title() == to_title(c))
    print(to_title(a))
    print(to_title(b))
    print(to_title(c))
