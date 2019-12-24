# 5 Interpolation


def inter(str1, dict1):
    if str1[-1:] in dict1:
        return print("{}{}".format(str1[:-1], dict1[str1[-1:]]))
    else:
        return print("None")


s2 = "This is s"
d2 = {"s": "Sparta", "t": "Troy", "a": "Athens"}

inter(s2, d2)
