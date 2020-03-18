class Hero_1:
    x = 1

    def draw(self):  # имя
        print("I'm Hero_1")

    def run(self):
        print('бежать')

    def shoot(self):
        print('выстрел')

    def collect(self):
        print('взять предмет')

    def speed(self):
        print('скорость')


class Hero_2(Hero_1):
    def draw(self):
        print("I'm Hero_2")

    def run(self):
        print('полет')


class Hero_3(Hero_1):
    def draw(self):
        print("I'm Hero_3")

    def run(self):
        print('полет')

heroes = [Hero_1(), Hero_2(), Hero_3()]  # все герои
a = int(input())  # ввести цифру от 0 до 2, выбрать героя    В чем ошибка в этом месте?????
heroes[a].draw()  # привествие героя
