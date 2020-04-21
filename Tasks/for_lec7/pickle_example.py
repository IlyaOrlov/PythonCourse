import pickle


class User:
    def __init__(self):
        self.name = 'name'
        self.age = 'age'
    def setName(self, value):
        self.name = value
    def getName(self):
        return self.name
    def setAge(self, value):
        self.age = value
    def getAge(self):
        return self.age

class Worker(User):
    def __init__(self):
        super().__init__()
        self.salary = 0
    def setSalary(self, number):
        self.salary = number
    def getSalary(self):
        return self.salary
    def __str__(self):
        return f"Worker: name={self.name}, age={self.age}, salary={self.salary}"


john = Worker()
john.setName('John')
john.setAge(25)
john.setSalary(1000)
jack = Worker()
jack.setName('Jack')
jack.setAge(26)
jack.setSalary(2000)

with open("dumpfile", "wb") as f:
    pickle.dump(john, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(jack, f, protocol=pickle.HIGHEST_PROTOCOL)

