class User:
    def __init__(self):
        self.name = 'Ivan'
        self.age = 25
    def __repr__(self):
        return 'User: name={}, age={}'.format(self.name, self.age)
