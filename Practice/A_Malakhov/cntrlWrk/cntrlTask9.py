class User:
    name = None
    age = None

    def setName(self, name):
        self.setName = name


    def getName(self):
        return self.setName

    def setAge(self, age):
        self.setAge = age

    def getAge(self):
        return self.setAge


class Worker(User):
    salary = None

    def setSalary(self, salary):
        self.setSalary = salary

    def getSalary(self):
        return self.setSalary

w1 = Worker()
w1.setName('John')
w1.setAge('26')
w1.setSalary(15000)
w2 = Worker()
w2.setName('Jack')
w2.setAge(25)
w2.setSalary(60000)
print(w1.getName())
print(w1.getAge())
print(w1.getSalary())
print(w2.getName())
print(w2.getAge())
print(w2.getSalary())
print('The sum of salary:', w1.getSalary() + w2.getSalary())
