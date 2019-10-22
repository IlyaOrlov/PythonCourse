# Вариант 1
class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def setName(self):
        pass

    def getName(self):
        pass

    def setAge(self):
        pass

    def getAge(self):
        pass


class Worker(User):
    def __init__(self, salary, name, age):
        super().__init__(self, salary)
        self.salary = salary

    def getSalary(self):
        pass

    def setSalary(self):
        pass


a=Worker(name='John', age= 25, salary= 1000)
b=Worker(name='Jack', age= 25, salary= 2000)

print(a.salary+b.salary)

# Вариант 2
class User1:

    def __init__(self):
        self.name = None
        self.age = None

    def setName(self, name):
         self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


class Worker1(User1):
    def __init__(self):
        super().__init__()
        self.salary = None

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary

c=Worker1()
c.setName('John')
c.setAge=(25)
c.setSalary(1000)

d=Worker1()
d.setName('Jack')
d.setAge=(26)
d.setSalary(2000)

print(c.getSalary()+d.getSalary())