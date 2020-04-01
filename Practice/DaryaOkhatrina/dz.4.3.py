arr = [0, 3, 24, 2, 3, 7]
def sort_func(arr):
    N = len(arr)
    i = 0
    while i < N - 1:
        m = i
        j = i + 1
        while j < N:
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    return arr

print(sort_func(arr))




