numbers = list(map(int, input(' Введите список чисел через пробел: ').split(' ')))
index_min = None
for i in range(len(numbers)-1):
    index_min = numbers.index(min(numbers[i:]), i)
    numbers[i], numbers[index_min] = numbers[index_min], numbers[i]
print(numbers)
