# Задание1:
for x in range(1, 101):
    if x % 15 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)

a = list(range(1, 101))
for n, i in enumerate(a):
    if i % 15 == 0:
        a[n] = 'FizzBuzz'
    elif i % 5 == 0:
        a[n] = 'Buzz'
    elif i % 3 == 0:
        a[n] = 'Fizz'
print(a)

# Задание2:
b = input('Введи пятизначное число:')
for i, n in enumerate(b, 1):
    print(i, 'цифра равна', n)

c = input('Введи пятизначное число:')
j = 0
while j < len(b):
    print(j+1, 'цифра равна', [j])
    j += 1

# Задание 3 (здесь я изменила первое знчение, чтобы проверить, перемещается ли первый объект массива):
arr = [0, 3, 24, 2, 3, 7]

for k in range(len(arr) - 1):
    for m in range(k + 1, len(arr)):
        if arr[k] > arr[m]:
            arr[k], arr[m] = arr[m], arr[k]

print(arr)


for j in range(len(arr)):
    min_n = min(arr[j:])
    min_ind = arr.index(min_n, j)
    arr[j], arr[min_ind] = arr[min_ind], arr[j]

print(arr)
