arr=[0,3,24,2,3,7]
i=0
while i < len(arr):
    minElement = min(arr[i:])
    minIndex = arr[i:].index(minElement) + i
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
    i+=1
print(arr)
