def max_numb(a, b):
  if a > b:
     print(a)
  elif a == b:
     print('числа равны')
  else:
     print(b)
x = int(input('введите первое число: '))
y = int(input('введите второе число: '))
max_numb(x, y)
