
class User:
    name = "name"
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name='{self.name}', age='{self.age}')"

