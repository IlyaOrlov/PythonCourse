def my_reversed(lst):
    for i in range(len(lst)//2):
        lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
    return lst


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_reversed(a))