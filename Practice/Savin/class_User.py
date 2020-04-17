# Задание 9
class User:

    def __init__(self):
        self.name = None
        self.age = None

    def setName(self, name: str):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age: int):
        self.age = age

    def getAge(self):
        return self.age

class Worker(User):

    def __init__(self):
        super().__init__()
        self.salary = None

    def setSalary(self, salary: int):
        self.salary = salary

    def getSalary(self):
        return self.salary

w1 = Worker()
w1.setName('John')
w1.setAge(25)
w1.setSalary(1000)
w2 = Worker()
w2.setName('Jack')
w2.setAge(26)
w2.setSalary(2000)
print(f'name: {w1.getName()}, age: {w1.getAge()}, salary: {w1.getSalary()}')
print(f'name: {w2.getName()}, age: {w2.getAge()}, salary: {w2.getSalary()}')
print(f'sum salary: {w1.getSalary() + w2.getSalary()}')


