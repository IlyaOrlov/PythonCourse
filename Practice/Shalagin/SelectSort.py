arr=[0,3,24,2,3,7]
leng=len(arr)
print(leng)
i=0
while i < leng:
    minElement = min(arr[i:])
    minIndex = arr[i:].index(minElement) + i
    temp=arr[i]
    arr[i]=minElement
    arr[minIndex]=temp
    i+=1
print(arr)
