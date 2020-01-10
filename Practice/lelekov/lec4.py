


# задание 1
def task1():
  for i in range(1,101):
    if i % 3 == 0:
        print(" {} результат {} ".format(i,"Fizz"))
    elif i % 5 == 0:
        print(" {} результат {} ".format(i, "Bizz"))
    elif (i % 5 == 0) and (i % 3 == 0) :
        print(" {} результат {} ".format(i, "Bizz"))
    else:
        print(" {} результат {} ".format(i, i))


# задание 2
def task2():
  ch = input('Введите 5 значное число ' )
  while not ch.isdigit() or len(ch) != 5:
    ch = input('Введите 5 значное число ')
    s = 1
  for i in ch:
    print('{} первая цифра равнв {}' .format(s, i))
    s = s + 1

# задание 3
def task3():
 # arr = [2, 3, 1, 4, 3]
 arr = [0, 3, 24, 2, 3, 7]
 i = 0

 while i < len(arr)-1:
      n = arr.index(min(arr[i:]), i)
      arr[i], arr[n] = arr[n], arr[i]
      i = i + 1
 print(arr)


# задание 4
def task4():
 fo = open("str.txt","w")
 str = input('Введите строку:')
 fo.write(str)
 fo.close()
 # чтение и вывод файл
 fo = open("str.txt","r")
 #data = fo.readlines()
 data = fo.read()
 print("строка из файла:", data)
 list = []
 i = 0
 # for i in randge(len(data)):
 print('Результат')
 while i != len(data):
     if data[i] == "\t":
         list.append(" ")
     elif data[i] == " ":
         list.append("\t")
     else:
         list.append(data[i])
     i = i + 1
 print(''.join(list))
 fo.close()


# проверка на число
def vvod(ch):
  while not ch.isdigit():
       ch=input('Введите количество ключей(число) ')
  return ch

def task5():
 str = input('Введите строку_')
 ak = []
 keynum = input('Введите количество ключей')
 vvod(keynum)
 keynum = int(keynum)
 for i in range(keynum):
    ak.append((input('Введите ключ')))
 print(ak)
 A = {item: input('Введите знаечение') for item in ak}
 print(A)
 for key in A:
      str = str.replace(key, A[key])
 print(str)


def prnmatrix(X):
    for i in range(len(X)):
        for j in range(len(X[i])):
            print(X[i][j], end=' ')
        print()

def task6():
 mtrx = [[5, 3, 4], [6, 7, 9], [2, 6, 3]]
 sp = []
 prnmatrix(mtrx)
 p = int(input("Введите число, столбец с которым хотите удалить: "))
 for i in range(len(mtrx)):
     for j in range(len(mtrx[i])):
         if mtrx[i][j] == p:
             sp.append(j)
 sp.sort(reverse=True)
 for q in range(len(mtrx)):
     for x in sp:
         del mtrx[q][x]
 prnmatrix(mtrx)


print(
    'Задание 1 - Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем, \n '
    'программа должна выводить слово Fizz,а вместо чисел, кратных пяти —слово Buzz. Если число кратно пятнадцати, то\n'
    'программа должна выводить слово FizzBuzz.\n')
print(
    'Задание 2 - Составить программу, которая будет считывать введённое пятизначное число. После чего, каждую цифру этого\n'
    'числа необходимо вывести в новой строке:\n'
    'Число: 10819\n'
    '1 цифра равна 1\n'
    '2 цифра равна 0\n'
    '3 цифра равна 8\n'
    '4 цифра равна 1\n'
    '5 цифра равна 9\n')
print('Задание 3 - Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов:\n'
      '1. найти наименьший элемент в массиве\n'
      '2. поменять местами его и первый элемент в массиве\n'
      '3. найти следующий наименьший элемент в массиве\n'
      '4. и поменять местами его и второй элемент массива\n'
      '5. продолжать это пока весь массив не будет отсортирован\n'
      'arr = [0,3,24,2,3,7]  на выходе должен получиться список, содержащий [0, 2, 3, 3, 7, 24]\n')
print(
    'Задание 4 - Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле или строке.\n'
    'То есть, передается на вход файл или строка, необходимо заменить все символы табуляции на четыре пробела, либо же заменить\n'
    'все комбинации из четырех символов пробела на символ табуляции.\n')
print(
    'Задание 5 - Интерполировать некие шаблоны в строке. Есть строка с определенного вида форматированием. необходимо заменить\n'
    'в этой строке все вхождения шаблонов на их значение из словаря.\n')
print(
    'Задание 6 - Есть список списков (матрица mtrx = [[5, 3, 4], [6, 7, 9], [2, 6, 3]]). Каждый внутренний список - это строка матрицы. Необходимо реализовать функцию,\n'
    'которая удаляет столбец, который содержит заданную цифру.\n')

vib = input('Введите номер задания: ')
vib = int(vvod(vib))
if vib == 1:
    task1()
elif vib == 2:
    task2()
elif vib == 3:
    task3()
elif vib == 4:
    task4()
elif vib == 5:
    task5()
elif vib == 6:
    task6()
else:
    print("номер задания некорректен")
c = input()
