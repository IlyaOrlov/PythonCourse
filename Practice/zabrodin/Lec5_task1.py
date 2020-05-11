class Man:
    def __init__(self, n, s):
        self.name = n
        self.surname = s
        self.full_name = n + ' ' + s

    def solve_task(self):
        print("I'm not ready yet, {}!".format(self.full_name))


m = Man('Igor', 'Zabrodin')
m.solve_task()
