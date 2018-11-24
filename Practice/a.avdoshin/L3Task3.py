# 22.11 - [ИО]:  Проверено (ОК).
def sort(mass):
    for i in range(len(mass) - 1):
        first = mass[i]
        minimum = min(mass[i + 1:])
        if minimum < first:
            mass[mass[i + 1:].index(minimum) + i + 1] = first
            mass[i] = minimum
    return mass


arr = [0, 3, 24, 2, 3, 7]
print(sort(arr))
