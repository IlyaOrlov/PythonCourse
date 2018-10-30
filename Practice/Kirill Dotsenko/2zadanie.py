a=int(input("Vvedite chislo:"))
c=[]
while a%10!=0:
	b=int(a%10)
	c.append(b)
	#print(str(b)+"цифра равна"+str(b))
	a=(a-b)/10
c.reverse()
for e in c:
	print(str(e)+" цифра равна "+str(e))
