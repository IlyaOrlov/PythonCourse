arr = [4, 3, 7, 5, 89, 23, 6, 1, 0, 5, 2]
j = 0
for num1 in arr:
    i = 0
    min1 = arr[j]
    min_ind = j
    for num2 in arr:
        if i < j:
            pass
        elif num2 < min1:
            min1 = num2
            min_ind = i
        i += 1
    arr[j], arr[min_ind] = arr[min_ind], arr[j]
    j += 1
print(arr)