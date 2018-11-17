# 04.11 - [ИО]:  Проверено (есть замечания).
mes="Enter 'q' if u want to stop"
# 04.11 - [ИО]:  Таким образом очень неудобно тестировать программу:
# каждый раз приходится заново вводить всю матрицу. Лучше либо использовать
# фиксированную матрицу, либо считывать ее из файла.
st=int(input("How many strings in your matrix:"))
stol=int(input("How many stolbec:"))
# 04.11 - [ИО]:  Зачем нужен вызов range(1,st+1)?
num=list(range(1,st+1))
c=[]
# 04.11 - [ИО]:  "a", как параметр цикла, здесь не имеет смысла
for a in num:
	# т.к. здесь вы ее переопределяете.
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
                # 04.11 - [ИО]:  проще udal сделать множеством
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
