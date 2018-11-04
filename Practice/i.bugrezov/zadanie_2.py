number = input ("Введите число: ")
p=1
k=0
for k in range(0, len(number)):
	print (p, " цифра: ", number[k])
	k +=1
	p +=1
