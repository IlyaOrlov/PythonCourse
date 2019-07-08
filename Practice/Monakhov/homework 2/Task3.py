def choice_sort(arr):
    i = 0
    while i < len(arr):
        min_num = min(arr[i:])
        if min_num == arr[i]:
            pass
        else:
            temp = arr[i]
            arr[arr[i:].index(min_num) + i] = temp
            arr[i] = min_num
        i += 1
    print(arr)


s = [0, 3, 24, 23, 10, 3, 18]
choice_sort(s)
