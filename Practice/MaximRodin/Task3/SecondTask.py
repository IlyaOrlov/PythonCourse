s = (input('Введите пятизначное число: '))
i=0
if (len(s)) == 5:
   for num in str(s):
      i += 1
      print(i,  " цифра равна ",  num)
else:
   print('введено не пятизначное число')