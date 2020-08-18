import random


N = 5
def new_line(array):
    for i in range(N):
        print(f'{i} цифра равна {array[i]}')

Line = [random.randint(0, 9) for j in range(N)]
print(Line)
new_line(Line)
