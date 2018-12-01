class Money():
	def __init__(self,rub,kop,baksy):
		self.rub=rub
		self.kop=kop
		self.baksy=float(baksy)
	def __add__(self,rub1=0,kop1=0):
		a=self.rub+rub1
		b=self.kop+kop1
		if b>=100:
			a=a+b//100
			b=b%100
		return str(a)+','+str(b)
	def __sub__(self,rub1=0,kop1=0):
		a=self.rub-rub1
		b=self.kop-kop1
		if b<0:
			a=a-1
			print(a)
			b=(self.kop-kop1)+100
		if a<0:
			print("Po hodu u vas ipoteka")
		return str(a)+','+str(b)
	def __truediv__(self,rub1=0,kop1=0):
		a=self.rub//rub1
		b=self.kop//kop1
		if b<10:
			b='0'+str(b)
		return str(a)+','+str(b)
		#тут можно измудриться с условиями просто я постановку задачи
		#не оч понимаю
	def __eq__(self,rub1=0,kop1=0):
		if self.rub==rub1 and self.kop==kop1:
			return str(self.rub)+','+str(self.kop)+'='+str(rub1)+','+str(kop1)
		if self.rub==rub1 and self.kop>kop1:
			return str(self.rub)+','+str(self.kop)+'>'+str(rub1)+','+str(kop1)
		if self.rub==rub1 and self.kop<kop1:
			return str(self.rub)+','+str(self.kop)+'<'+str(rub1)+','+str(kop1)
		if self.rub>rub1:
			return str(self.rub)+','+str(self.kop)+'>'+str(rub1)+','+str(kop1)
		if self.rub<rub1:
			return str(self.rub)+','+str(self.kop)+'<'+str(rub1)+','+str(kop1)
	def dollar(self):
		c=float(str(self.rub)+'.'+str(self.kop))
		s=c/self.baksy
		return s
a=Money(16,15,'67.09')
print(a.__add__(13,95))
print(a.__sub__(12,72))	
print(a.__truediv__(4,5))
print(a.__eq__(17,16))
print(a.dollar())
