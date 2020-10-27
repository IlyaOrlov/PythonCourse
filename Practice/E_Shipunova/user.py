class User:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return "User: name={}, age={}, position={}.".format(self.name, self.age, self.position)
