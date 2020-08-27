import random


N = 10
def sorting(array):

    for i in range(len(array) - 1):
        min = i
        next_min = i + 1
        while next_min < len(array):
            if array[next_min] < array[min]:
                min = next_min
            next_min += 1
        array[i], array[min] = array[min], array[i]

Line = [random.randint(0, 9) for j in range(N)]
print(Line)
sorting(Line)
print(Line)
