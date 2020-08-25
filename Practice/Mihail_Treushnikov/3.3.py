arr = [40,1,68,100,1,90,5,1034,44]

def select_sort (arr,length):
    i = 0
    while i<length-1:
        j = i+1
        pos = j
        while j<length-1:
            if (arr[j+1]<arr[pos]):
                pos = j+1
            j+=1
        if (arr[pos]<arr[i]):
            arr[i],arr[pos] = arr[pos], arr[i]
        i+=1
    return arr

print(select_sort(arr, len(arr)))
