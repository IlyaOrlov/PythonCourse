def my_reverse(lst):
    for i in range(len(lst) // 2):
        first = lst[i]
        lst[i] = lst[-i - 1]
        lst[-i - 1] = first
    return lst


testlst = [i for i in range(10)]
print(testlst)
print(my_reverse(testlst))
