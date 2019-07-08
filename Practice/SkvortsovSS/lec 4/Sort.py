def sort():
    arr = [0, 3, 24, 2, 3, 7]
    i = 0
    while i < len(arr):
        j = arr.index(min(arr[i:]),i)
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
    print(arr)

sort() 