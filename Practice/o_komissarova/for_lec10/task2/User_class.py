class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self, name):
        self._name = str(name)

    def set_age(self, age):
        if str(age).isdigit():
            self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
