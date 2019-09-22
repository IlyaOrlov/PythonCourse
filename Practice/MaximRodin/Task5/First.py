class Man:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.login = (name + surname)
    def solve_task(self):
        print("I am not ready yet")
Worker = Man("Max", "Rodin")
print(Worker.login)
Worker.solve_task()



