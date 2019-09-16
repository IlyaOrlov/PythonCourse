# NUM 1
for i in range(1, 101):
    #print(i, end = ',')
    if i % 15 == 0:
        i = 'FizzBuzz'
    elif i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    print(i)


# NUM 2
x = int(input())
n = 1
if len(str(x)) == 5:
    for i in str(x):
        print(n, 'цифра равна ', i)
        n += 1
else:
    print('Число не 5-ти значное')


#NUM 3
arr = [0,3,24,2,3,7]
for i in range(len(arr)-1):
    minimum = arr[i]
    for j in range(i + 1, len(arr)):
        if arr[j] < minimum:
            minimum = arr[j]
            index_of_min = j
            arr[i], arr[index_of_min] = arr[index_of_min], arr[i]
print(arr)



