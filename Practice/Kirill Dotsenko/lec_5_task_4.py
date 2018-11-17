import itertools
def gen(n):
	c=list(itertools.chain.from_iterable(n))
	print(c)
a=([1,2,3],[4,5],[6,7])
v=gen(a)

def stri(d):
	data = list(itertools.combinations(d, 4))#на самом деле я тут не совсем понял задание. Есть .combinations_with_replacement и permutations разницу между ними вижу но не знаю правильно ли выполнил задание
	print(data)
b=stri('password')

def kek(m):
	data=m
	bools=[True,False,False,False,False,True]
	data2=list(itertools.compress(data,bools))
	print(data2)
def kek2(g):
	h=[]
	for i in g:
		if len(i)==5 and i!='write':
			h.append(i)
	print(h)
c=kek((['hello','i','write','cool','code','world']))
p=kek2((['hello','i','write','cool','code','world']))
#Ну тут я просто решил двумя способами

