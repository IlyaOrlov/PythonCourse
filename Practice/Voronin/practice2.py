# первое задание
i = 1
while i <= 100:
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    print(i)
    i += 1

# второе задание
number = input('Введите пятизначное число :')
print('Число :'+ number)
lst = list(number)
i = 0
while i < len(lst):
    print("{} цифра равна : {}".format((i + 1), lst[i]))
    i += 1


# # Третье задание
arr = [0, 3, 24, 2, 3, 7]
i = 0
while i < (len(arr)-1):
    m = i
    j = i + 1
    while j < len(arr):
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(arr)

