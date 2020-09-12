class NotANumberException(Exception):
    pass


class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def setName(self, name):
        self._name = str(name)

    def setAge(self, age):
        if str(age).isdigit():
            self._age = age
        else:
            raise NotANumberException

    def getName(self):
        return self._name

    def getAge(self):
        return self._age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def setSalary(self, salary):
        if str(salary).isdigit():
            self.salary = salary
        else:
            raise NotANumberException

    def getSalary(self):
        return self.salary


worker_John = Worker("John", 25, 1000)
print(worker_John.getName(), worker_John.getAge(), worker_John.getSalary())
worker_Jack = Worker("Jack", 26, 2000)
print(worker_Jack.getName(), worker_Jack.getAge(), worker_Jack.getSalary())
