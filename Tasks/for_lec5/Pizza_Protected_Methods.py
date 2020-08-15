# Защищенные методы (как и обычные) наследуются
class Pizza:
    def make_pizza(self):
        print("making pizza")
        self._add_base()
        self._add_ingr()

    def _add_ingr(self):
        print("adding pizza ingridients")

    def _add_base(self):
        print("adding pizza base")

class VegPizza(Pizza):
    def _add_ingr(self):
        print("adding veg pizza ingridients")


p = VegPizza()
p.make_pizza()

# Вывод на экран:
# making pizza
# adding pizza base
# adding veg pizza ingridients