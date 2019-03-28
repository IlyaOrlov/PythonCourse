#Вариант с super()
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self):
        return self.name

    def set_age(self):
        return self.age

    def get_age(self):
        return self.age


class Worker(User):
    def __init__(self, name, age, salary):
        super(Worker, self).__init__(name, age)
        self.salary = salary

    def set_salary(self):
        return self.salary

    def get_salary(self):
        return self.salary


a1 = Worker('John', 25, 1000)
a2 = Worker('Jack', 26, 2000)
asum = a1.get_salary() + a2.get_salary()
print(asum)



