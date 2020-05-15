class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'User with name {} and age {}'.format(self.name, self.age)