class User:
    def __init__(self):
        self._name = None
        self.age = None

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value

    @name.getter
    def name(self):
        return self._name


us = User()
us.name = 19
print(us.name)
