class User:
    name = None
    age = None

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Worker(User):
    salary = None

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


obj1 = Worker()
obj1.set_name('John')
obj1.set_age(25)
obj1.set_salary(1000)

obj2 = Worker()
obj2.set_name('Jack')
obj2.set_age(26)
obj2.set_salary(2000)



print(f'total salaries of {obj1.get_name()} and {obj2.get_name()} {obj1.get_salary() + obj2.get_salary()} units')
