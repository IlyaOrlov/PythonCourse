class PizzaMaker:
    def __init__(self):
        self.__recipe = None

    def __prepare_dough(self):
        print('...dough is ready')

    def __make_filling(self):
        print(f'...{self.__recipe.name} filling is ready')

    def __cooking_pizza(self):
        print(f'...cooking at a temperature of {self.__recipe.temperature} C, for {self.__recipe.cooking_time} minutes')

    def __give_order(self):
        print(f'Your {self.__recipe.name} pizza is ready\n')

    def make_pizza(self, pizza_type):
        self.__find_recipe(pizza_type)
        if self.__recipe is None:
            print('I have no a recipe for that pizza')
            return
        print('\nCooking:')
        self.__prepare_dough()
        self.__make_filling()
        self.__cooking_pizza()
        self.__give_order()

    def __find_recipe(self, pizza_type):
        if pizza_type == 1:
            self.__recipe = PizzaRecipe('mushroom', 180, 15)
        elif pizza_type == 2:
            self.__recipe = PizzaRecipe('meat', 220, 25)
        elif pizza_type == 3:
            self.__recipe = PizzaRecipe('vegetable', 150, 10)


class PizzaRecipe:
    def __init__(self, name, temperature, cooking_time):
        self.name = name
        self.temperature = temperature
        self.cooking_time = cooking_time


def make_order():
    menu = ['Mushroom', 'Meat', 'Vegetable']
    print('Which pizza do you want?')
    while True:
        print('Please, choose one option:')
        for i, name in enumerate(menu, start=1):
            print(f'{i}) {name}')
        print('0) exit')
        try:
            order = input('Enter a number, please => ')
            order = int(order)
            if 0 <= order <= 3:
                return order
        except ValueError:
            pass
        print(f"\n'{order}' is an invalid option!\n")


while True:
    order = make_order()
    if order:
        PizzaMaker().make_pizza(order)
    else:
        break
print('Good buy')
