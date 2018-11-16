def my_len(lst):
    lenght = 0
    for i in lst:
        lenght += 1
    return lenght


test = [x for x in range(10)]
print(my_len(test), len(test))
