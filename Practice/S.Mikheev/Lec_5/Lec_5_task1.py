class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        return "I'm not ready yet"


a = Man('Sergei')
print('{} says: {}'.format(a.name, a.solve_task()))