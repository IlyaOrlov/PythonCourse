lst = [0, 3, 24, 2, 3, 7]
# вместо готового списка можно использоваь пользовательский ввод списка:
# lst = [int(a) for a in input().split()]

def sorting(lst):
    for i in range(len(lst) - 1):
        mn = i
        j = i + 1
        while j < len(lst):
            if lst[j] < lst[mn]:
                mn = j
            j = j + 1
        lst[i], lst[mn] = lst[mn], lst[i]
    print(lst)

sorting(lst)