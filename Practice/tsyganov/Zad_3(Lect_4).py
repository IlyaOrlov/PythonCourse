arr = [7,3,24,2,3,0] # [7,3,24,2,3,0]
x=0
y=0
while x<len(arr):
        a=min(arr[x:])
        y=x
        while a!=arr[y]:
            y+=1
        else:
                arr[y] = arr[x]
                arr[x] = a
                print(arr)
        x+=1
