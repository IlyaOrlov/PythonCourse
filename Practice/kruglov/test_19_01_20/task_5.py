# 5 function count_symbol


def count_symbol(str1, char1):
    count = 0
    for el in str1:
        if el == char1:
            count += 1
    print(count)


count_symbol("Hi Elvis, I am here!", "i")
