class User:
    name = None
    age = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


class Worker(User):
    salary = None

    def setSalary(self, salary):
        self.salary = int(salary)

    def getSalary(self):
        return self.salary


john = Worker()
john.setName('John')
john.setAge('25')
john.setSalary('1000')
jack = Worker()
jack.setName('Jack')
jack.setAge('26')
jack.setSalary('2000')

print(john.getName(), john.getAge(), john.getSalary())
print(jack.getName(), jack.getAge(), jack.getSalary())
print('The sum of salaries of {} and {}: {}$'.format(john.getName(), jack.getName(),
                                                     john.getSalary() + jack.getSalary()))
