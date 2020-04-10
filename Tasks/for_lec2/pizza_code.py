class Pizza:
    status = "не готова"

    def make_base(self):
        print("тесто готово")

    def add_ingr(self):
        print("ингрелиенты по умолчанию")

    def bake(self):
        print("пицца готова")
        self.status = "готова"


class VegPizza(Pizza):
    # методы make_base и bake наследуются
    # а add_ingr переопределен
    def add_ingr(self):
        print("добавлены овощи")


class MeatPizza(Pizza):
    def add_ingr(self):
        print("добавлено мясо")


class MashPizza(Pizza):
    def add_ingr(self):
        print("добавлены грибы")


# Один алгоритм для приготовки любой пиццы
def pizza_maker(p):
    p.make_base()
    p.add_ingr()
    p.bake()


print("Готовим овощную пиццу:")
pizza_maker(VegPizza())
print("Готовим мясную пиццу:")
pizza_maker(MeatPizza())
print("Готовим грибную пиццу:")
pizza_maker(MashPizza())


