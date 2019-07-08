class User:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name 
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age   

class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def setSalary(self, salary):
        self.salary = salary
    def getSalary(self):
        return self.salary  

    
User1 = Worker('John', 25, 1000 )   
User2 = Worker('Jack', 26, 2000 )   

User2.setAge(13)
print (User2.getAge())

print (User1.salary + User2.salary)