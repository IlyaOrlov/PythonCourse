# 5 Interpolation


def inter(str1, dict1):
    str2 = str1.split()
    for key in dict1.keys():
        if key in str2:
            el = str2.index(key)
            str2[el] = dict1[key]
    str1 = " ".join(str2)
    return str1


s2 = "This is t"
d2 = {"sss": "Sparta", "t": "Troy", "a": "Athens"}


print(inter(s2, d2))
