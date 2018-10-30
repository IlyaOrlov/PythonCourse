b=[]
c=[]
mes="If u want to stop press `q`"
while True:
	a=input(mes+"\nEnter the number:")
	
	if a=='q':
		break
	else:
		a=int(a)
		b.append(a)
		continue	
print(b)
while b:
	d=min(b)
	c.append(d)
	b.remove(d)
print(c)
