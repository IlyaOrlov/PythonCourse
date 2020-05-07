class User:
    name = ''
    age = 0

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Worker(User):
    salary = 0

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


w1 = Worker()
w1.set_name('John')
w1.set_age(25)
w1.set_salary(1000)
w2 = Worker()
w2.set_name('Jack')
w2.set_age(26)
w2.set_salary(2000)
print(w1.get_salary() + w2.get_salary())
