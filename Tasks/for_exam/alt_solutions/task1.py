def remake_fun(lst):
    lst2 = list(set(lst))
    i = 0
    while i < len(lst2) - 1:
        j = i + 1
        while j < len(lst2):
            if lst.count(lst2[j]) < lst.count(lst2[i]):
                lst2[j], lst2[i] = lst2[i], lst2[j]
            j += 1
        i += 1
    return lst2


def remake_fun2(lst):
    return sorted(list(set(lst)), key=lst.count, reverse=True)


if __name__ == "__main__":
    lst = [3, 3, 2, 5, 5, 5, 4]
    res = remake_fun(lst)
    print(res)
    res = remake_fun2(lst)
    print(res)
