i=0
a="Fizz"
b="Buzz"
while i !=100:
	i +=1
	if (i%5)==0 and (i%3)==0:
		print (a+b)
	else:
		if i%5==0:
			print (a)
		else:
			if i%3==0:
				print (b)
			else:
				print (i)
		
