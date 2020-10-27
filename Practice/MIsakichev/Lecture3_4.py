#Лекция 3-4
#task one
def FizzBuzz(i):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i %  3 == 0:
        print("Fizz")
    else: print(i)

for i in range(1,101):
    FizzBuzz(i)

#task two
def number():
 num = input('Enter the number')
 j=0
 for i in num:
  if(len(num) > 5):
   print("Можно вводить только пятизначные цифры")
   break
  else:
   j+=1
   print(f'{j} цифра равна {i}')
number()

#task three
def selecting_sort(arr):
    for i in range(len(arr) - 1):
        k= i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[k]:
                k = j
            j +=  1
        arr[i], arr[k] = arr[k], arr[i]

arr = [0,3,24,2,3,7]
print('Before sorting')
print(arr)
selecting_sort(arr)
print('after sorting')
print(arr)

#task four

def str_deploy(str):
    ch='    '
    if '\t' in str:
     if ch in str:
      str = str.replace(ch, '\t')
     str = str.replace('\t','    ')
    return str

str1 = 'Privet\tmenya zovut    Vasya\tI live in    Moscow'
str3 = str_deploy(str1)
print(str1)


#task five
def templates(line):
    dict = {'Goodbye':'Hello','hate':'Love'}
    for key, v in dict.items():
        line = line.replace(key, v)
    return line

string = 'Goodbye I hate you '
print(templates(string))

#task six
import numpy as np
def deleting_column(list):
    k=0
    num = int(input('enter the number for deleting column consist of this number'))
    for i in list:
        for j in i:
            if j == num:
                list = np.delete(list,k,1)
            else:
                k+=1
        k=0
    return list
l =[[1,2,33,100],
    [44,5,6,245],
    [7,8,9,17]]
l = deleting_column(l)
print('Matrix after deleting')
print(l)

