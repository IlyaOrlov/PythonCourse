# Задание 9
class User:

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


class Worker(User):

    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value


w1 = Worker('John', 25, 1000)
w2 = Worker('Jack', 26, 2000)
print(f'name: {w1.name}, age: {w1.age}, salary: {w1.salary}')
print(f'name: {w2.name}, age: {w2.age}, salary: {w2.salary}')
print(f'sum salary: {w1.salary + w2.salary}')


