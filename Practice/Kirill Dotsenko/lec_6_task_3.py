from random import randint
import pickle
class Human():
	def __init__(self,name,surname,age,height,eyes):
		self.name=name
		self.surname=surname
		self.age=age
		self.height=height
		self.eyes=eyes
	def __str__(self):
		a=self.name+' '+self.surname+' '+self.age+' '+self.height+' '+self.eyes
		return a
def seria(kol):
	spisok=[]
	i=0
	while i<kol:
		a=input("Enter name:")
		b=input("Enter surname:")
		c=input("Enter age:")
		d=input("Enter height:")
		e=input("Enter eyes:")
		clss=Human(a,b,c,d,e)
		spisok.append(clss.__str__())
		i+=1
	with open('humandata.txt','wb') as f:
		pickle.dump(spisok,f)
	
def deseria():
	with open('humandata.txt','rb') as f:
		data_new=pickle.load(f)
	for i in data_new:
		print(i)
c=int(input())
b=seria(c)
e=deseria()

