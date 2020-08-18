arr = [0,1,68,3,101,1]

def sort (arr,length):
    j = 0
    while j<length-1:
        i = j
        while i<length-1:
            if (arr[i+1]<arr[i]):
                tmp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp
            i+=1
        j+=1
    return arr

print(sort(arr, len(arr)))
