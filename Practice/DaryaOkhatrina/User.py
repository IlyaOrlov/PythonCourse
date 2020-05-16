class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self, value):
        self._name = value

    def get_name(self, name):
        return self._name

    def set_age(self, value):
        self._age = value

    def get_age(self, age):
        return self._age

class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    def set_salary(self, value):
        self._salary = value

    def get_salary(self):
        return self._salary


e1 = Worker('John', 25, 3000)
e2 = Worker('Jack', 30, 2000)
print(e1.get_salary())
print(e2.get_salary())
print(e1.get_salary() + e2.get_salary())
