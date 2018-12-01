import re
def frmt(st,*args):
	fi=re.findall(r'\d',st)
	c=[]
	for k in fi:
		k=int(k)
		c.append(k)
	mes=''
	res1=re.search(r'{',st)
	r1=res1.group(0)
	res2=re.search(r'}',st)
	r2=res2.group(0)
	i=0
	for a in st:
		if a==r1:
			mes+=args[c[i]]
			i+=1
			continue
		if a==r2 or a in fi:
			continue
		mes+=a
	return mes
c=frmt('kek:{2},{0},{1}','a','b','c')
print(c)
