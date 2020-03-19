# первое задание
i = 1
while i <= 100:
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    print(i)
    i += 1

# второе задание
number = input('Введите пятизначное число :')
print('Число :'+ number)
lst = list(number)
print('1 цифра равна '+ lst[0])
print('2 цифра равна '+ lst[1])
print('3 цифра равна '+ lst[2])
print('4 цифра равна '+ lst[3])
print('5 цифра равна '+ lst[4])

# Третье задание
arr = [0, 3, 24, 2, 3, 7]
i = 0
while i <= len(arr):
    m = i
    j = i + 1
    while j <= len(arr):
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(arr)