import datetime
def days(a,b,c,d,e,f):
	d1=datetime.datetime(a,b,c)
	d2=datetime.datetime(d,e,f)
	diff=d1-d2
	print(int(diff.days*5/7))
mes="Data kotoraya byla ranee vvodyat posledney!"
while True:
	print(mes)
	a=int(input("Vvedite god:"))
	b=int(input("Vvedite mesyats:"))
	c=int(input("Vvedite den:"))
	d=int(input("Vvedite god:"))
	e=int(input("Vvedite mesyats:"))
	f=int(input("Vvedite den:"))
	if d>a:
		print("Vy ne pravilno vveli datu!")
		continue
	else:
		g=days(a,b,c,d,e,f)
		break

