class User:

    def __init__(self, first_name, last_name, age, auto, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.auto = auto
        self.profession = profession

    def __repr__(self):
        return f'This is {self.first_name} {self.last_name}, he is {self.age} years old. ' \
               f'He has a {self.auto} car and his profession is a {self.profession}.'
