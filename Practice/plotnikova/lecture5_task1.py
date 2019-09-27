class Man():

    def __init__(self, name="Вася"):
        self.name=name
        # self.solve_task()

    def solve_task(self):
        return print ("{}: I'm not ready yet".format(self.name))


#C self.solve_task() в конструторе
a=Man("Вася")

#Или без self.solve_task() в конструторе
b=Man()
b.solve_task()