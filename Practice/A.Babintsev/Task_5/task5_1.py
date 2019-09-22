"""
Написать класс Man, который принимает имя в конструкторе. Имеет
метод solve_task, который просто выводит "I'm not ready yet".
"""


class Man:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login = (first_name[0] + last_name).lower()

    def solve_task(self):
        print("I'm not ready yet")
        
Person1 = Man("Ivan", "Oleynikov") 
print(Person1.login +": ")
Person1.solve_task()
