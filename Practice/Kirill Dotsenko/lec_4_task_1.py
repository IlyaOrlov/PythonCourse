from random import randint
import time 

class Man():
	def __init__(self,name):
		self.name=name
	def solve_task(self):
		return self.name+", I'm not ready yet"
a=Man('Kirill')
print(a.solve_task())

class Pupil(Man):
	def __init__(self,name):
		super().__init__(name)
	def solve_task(self):
		a=randint(3,6)
		time.sleep(a)
		return self.name+", I'm not ready yet"
b=Pupil('Kirill')
print(b.solve_task())
		
