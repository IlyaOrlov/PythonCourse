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


#Num 4
def tab_on_space(s):
    s = s.expandtabs(4)
    return s


def space_on_tab(s):
    s = s.replace('    ','\t')
    return s


s = '343\t4    9\t8  0-9 0\t98 8      8  0\t9  '

if '    ' in s:
    print(space_on_tab(s))
else:
    print('В строке нет 4-х пробелов')
if '\t' in s:
    print(tab_on_space(s))
else:
    print('В строке нет символа "\t"')


# Num 5
s = 'В лесу родилась ёлочка, В лесу она росла. Зимой и летом стройная, Зелёная была.'
# s = '4464688969'
d = {'лесу': 1,
     'она': 2,
     'летом': 3
     }
for i in d.keys():
    s = s.replace(i, str(d[i]))
print(s)



#Num 6

