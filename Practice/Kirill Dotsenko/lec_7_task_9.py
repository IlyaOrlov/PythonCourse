class User():
	@property
	def name(self):
		pass
	@name.setter
	def name(self, value):
		self._name = value
	@name.getter
	def name(self):
		return self._name
	@property
	def age(self):
		pass
	@age.setter
	def age(self,value):
		self._age=value
	@age.getter
	def age(self):
		return self._age
class Worker(User):
	@property
	def salary(self):
		pass
	@salary.setter
	def salary(self,value):
		self._salary=value
	@salary.getter
	def salary(self):
		return self._salary
worker = Worker()
worker.age = 25
worker.name = 'John'
worker.salary = 1000
worker2 = Worker()
worker2.age = 26
worker2.name = 'Jack'
worker2.salary = 2000
print(worker.salary+worker2.salary)
