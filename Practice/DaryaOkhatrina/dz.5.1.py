class Man:
    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print(self.name, "I'm not ready yet")
x = Man('Ivan')
x.solve_task()