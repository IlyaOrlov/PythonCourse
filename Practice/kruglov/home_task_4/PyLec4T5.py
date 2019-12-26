# 5 Interpolation


def inter(str1, dict1):
    str2 = ""
    for el in str1.split():
        if el in dict1:
            str2 += dict1[el]
        else:
            str2 += el + " "
    return str2


s2 = "This is r"
d2 = {"sss": "Sparta", "t": "Troy", "a": "Athens"}


print(inter(s2, d2))
