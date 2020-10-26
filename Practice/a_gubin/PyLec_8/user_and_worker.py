class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary


if __name__ == "__main__":
    john = Worker("John", 25, 1000)
    jack = Worker("Jack", 26, 2000)
    print(f"Their summary salary : {john.getSalary() + jack.getSalary()}")
