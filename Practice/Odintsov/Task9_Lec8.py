class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self):     #Я не очень понял зачем setName, поэтому написал его для изменения имени юзера
        self.name = input("Enter a new name")

    def getName(self):
        print(self.name)

class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def setSalary(self):   #То же, что и с setName
        self.salary = int(input("Enter a new salary"))

    def getSalary(self):
        return(self.salary)

John = Worker("John", 25, 1000)
Jack = Worker("Jake", 26, 2000)

Total_Salary = John.getSalary() + Jack.getSalary()
print("John's and Jack's total salary is {}".format(Total_Salary))



