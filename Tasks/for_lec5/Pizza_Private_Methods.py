# Закрытые методы не наследуются
class Pizza:
    def make_pizza(self):
        print("making pizza")
        self.__add_base()
        self.__add_ingr()

    def __add_base(self):
        print("adding pizza base")

    def __add_ingr(self):
        print("adding pizza ingredients")

class VegPizza(Pizza):
    # не переопределяет закрытый метод базового класса
    def __add_ingr(self): 
        print("adding veg pizza ingredients")


p = VegPizza()
p.make_pizza()

# Вывод на экран:
# making pizza
# adding pizza base
# adding pizza ingredients


