class User:
    __name = None
    __age = -1

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = int(age)

    def get_age(self):
        return self.__age

    def __init__(self, name, age):
        self.__name = name
        self.__age = int(age)

class Worker(User):
    __salary = -1

    def __init__(self, name, age, salary):
        super(Worker, self).__init__(name, age)
        self.__salary = int(salary)

    def get_salary(self):
        return self.__salary


john = Worker("John", 25, "1000")
jack = Worker("Jack", 26, "2000")

print("Summary of salaries {} and {} is {}".format(john.get_name(), jack.get_name(), john.get_salary() + jack.get_salary()))