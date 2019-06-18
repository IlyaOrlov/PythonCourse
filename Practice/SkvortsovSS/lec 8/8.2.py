def func(list):
    i = 0
    j = len(list) - 1
    while i <= len(list)/2:
        list[i], list[j] = list[j], list[i]
        i += 1
        j = j- 1
    print(list)


func(['1', '2', '3', '4', '5'])


