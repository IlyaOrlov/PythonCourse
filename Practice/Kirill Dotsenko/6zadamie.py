mes="Enter 'q' if u want to stop"
st=int(input("How many strings in your matrix:"))
stol=int(input("How many stolbec:"))
num=list(range(1,st+1))
c=[]
for a in num:
	a=[]
	i=1
	while i<=stol:
		b=int(input(mes+"\nVvedite chislo:"))
		#if b=='q':
			#break
		#b=int(b)
		a.append(b)
		i+=1
	#print(a)
	c.append(a)

print(c)
print(c[1])

def delete(c,chislo):
	udal=[]
	for sp in c:
		i=0
		for sm in sp:
			if sm==chislo:
				if i in udal:
					continue
				else:
				    udal.append(i)
			i+=1
	udal.sort(reverse=True)
	print(udal)
	for k in udal:
		for v in c:
			del v[k]
chislo=int(input("Which num:"))
delete(c,chislo)
print(c)
