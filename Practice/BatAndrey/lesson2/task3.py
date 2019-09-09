class Person:
    """Общий класс персонажей, которые умеют бегать, стрелять и собирать предметы"""
    def __init__(self, name, start_speed, start_accuracy, start_quatity):
        self.name = name
        self.start_speed = start_speed
        self.start_accuracy = start_accuracy
        self.start_quantity = start_quatity

    def run(self, speed):
        """Персонаж бежит"""
       pass

    def shoot(self, accuracy, speed_shoot):
        """Персонаж стреляет"""
        pass

    def pick_up(self, quantity):
        """Персовнаж поднимает вещи"""
        pass


class PersonFly(Person):
    """Класс персонажей которые умеют летать"""
    def fly(self, speed_fly, skill_fly):
        pass


class Animations:
    """Класс, который отвечает за анимацию"""
    def __init__(self, *args):
        self.ani_shoot = args
        self.ani_run = args
        self.ani_fly = args
        self.pick_up = args
    def ani_shoot(self):
        """Показывает анимацию стрельбы при стрельбе"""
        pass
    def ani_run(self):
        """Показывает анимацию бега при беге"""
        pass
    def ani_pick_up(self):
        """Показывает анимацию подбора предметов"""
        pass