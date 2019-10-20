class Man:
    def __init__(self, name='Василек'):
        self.name = name

    def solve_task(self):
        print('{}, I \'m not ready yet'.format(self.name))


# проверка
obj = Man('Вася')
obj.solve_task()

obj2 = Man()
obj2.solve_task()