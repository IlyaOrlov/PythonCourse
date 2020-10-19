from abc import ABC, abstractmethod


class Action():
    def do_action(self, atrtibute):
        print("base action")


class Run(Action):
    def do_action(self, atribute):
        self._atribute = atribute
        print("running with speed {}".format(atribute))


class Fly(Action):
    def do_action(self, atribute):
        self._atribute = atribute
        print("flying with speed {}".format(atribute))


class ComputerGame(ABC):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
        print("Hello my name {}".format(name))

    @abstractmethod
    def coolecting(self, obj):
        pass


class standart_Charachter(ComputerGame):

    def __init__(self, name, gender, speed, shoots, new_action, dict={}):
        super().__init__(name, gender)
        self._speed = speed
        self._shoots = shoots
        self._new_action = new_action
        self.dict = dict

    def __str__(self):
        return "name - {} gender - {} speed - {} shoots - {} loot - {}" \
            .format(self._name, self._gender, self._speed, self._shoots, self.dict.items())

    @property
    def action(self):
        return self._action

    @property
    def speed(self):
        return self._speed

    @property
    def shoots(self):
        return self._shoots

    @action.setter
    def action(self, new_action):
        if isinstance(new_action, Action):
            self._action = new_action
        else:
            print("Incorrect action")

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed

    @shoots.setter
    def shoots(self, new_shoots):
        self._shoots = new_shoots

    def coolecting(self, obj):
        if (obj in self.dict):
            count = self.dict.get(obj)
            self.dict.update({obj, count + 1})
        else:
            self.dict.setdefault(obj, 1)

    def getLoot(self, name):
        for key in self.dict:
            if name == key:
                return_key = key
                if (self.dict.get(key) > 1):
                    count = self.dict.get(key)
                    self.dict.update({key, count - 1})
                else:
                    self.dict.pop(key)
                return return_key


class fly_Charachter(standart_Charachter):

    def __init__(self, flight_altitude, flying_speed, name, gender, speed, shoots, new_action, dict={}):
        super().__init__(name, gender, speed, shoots, new_action, dict)
        self._flight_altitude = flight_altitude
        self._flying_speed = flying_speed

    def __str__(self):
        return "name - {} gender - {} speed - {} shoots - {} flying speed - {} flying altitude - {} loot - {}" \
            .format(self._name, self._gender, self._speed, self._shoots, self._flying_speed, self._flight_altitude,
                    self.dict.items())

    @property
    def action(self):
        return self._action

    @property
    def flying_speed(self):
        return self._flying_speed

    @property
    def flight_altitude(self):
        return self._flight_altitude

    @action.setter
    def action(self, new_action):
        if isinstance(new_action, Action):
            self._action = new_action
        else:
            print("Incorrect action")

    @flying_speed.setter
    def flying_speed(self, new_speed):
        self._flying_speed = new_speed

    @flight_altitude.setter
    def flight_altitude(self, new_speed):
        self._flight_altitude = new_speed


class Loot(ABC):
    @abstractmethod
    def use(self, atributes):
        pass


class LootUp(Loot):
    def __init__(self, name, obj):
        if hasattr(obj, 'speed') or hasattr(obj, 'shoots') \
                or hasattr(obj, 'flying_speed') or hasattr(obj, 'flight_altitude'):
            self.name = name
            self.obj = obj

    def __str__(self):
        return self.name

    def use(self, atributes):
        if (atributes == "speed"):
            self.obj.speed *= 2
        elif (atributes == "shoots"):
            self.obj.shoots *= 2
        elif (atributes == "fly_altitude"):
            self.obj.flight_altitude *= 2
        elif (atributes == "fly_speed"):
            self.obj.flying_speed *= 2


class LootDown(Loot):
    def __init__(self, name, obj):
        if hasattr(obj, 'speed') or hasattr(obj, 'shoots') \
                or hasattr(obj, 'flying_speed') or hasattr(obj, 'flight_altitude'):
            self.name = name
            self.obj = obj

    def __str__(self):
        return self.name

    def use(self, atributes):
        if (atributes == "speed"):
            self.obj.speed /= 2
        elif (atributes == "shoots"):
            self.obj.shoots = round(self.obj.shoots / 2)
        elif (atributes == "fly_altitude"):
            self.obj.flight_altitude /= 2
        elif (atributes == "fly_speed"):
            self.obj.flying_speed /= 2


if __name__ == "__main__":
    hero1 = standart_Charachter("Mike", "male", 10, 10, Action())
    print(hero1)

    loot1 = LootUp('Upgrade1', hero1)
    loot2 = LootDown('Degradation2', hero1)
    loot3 = LootDown('Degradation3', hero1)

    hero1.coolecting(loot1)
    hero1.coolecting(loot2)
    hero1.coolecting(loot3)

    print(hero1)

    hero1.getLoot(loot1).use("speed")
    hero1.getLoot(loot3).use("shoots")

    print(hero1)

    hero1.action = Run()
    hero1.action.do_action(hero1.speed)

    hero2 = fly_Charachter(1000, 100, "Alla", "femal", 10, 10, Action())
    print(hero2)

    loot1 = LootUp('Upgrade1', hero2)
    loot2 = LootDown('Degradation2', hero2)
    loot3 = LootDown('Degradation3', hero2)

    hero2.coolecting(loot1)
    hero2.coolecting(loot2)
    hero2.coolecting(loot3)

    print(hero2)

    hero2.getLoot(loot1).use("fly_altitude")
    hero2.getLoot(loot3).use("fly_speed")

    print(hero2)

    hero2.action = Fly()
    hero2.action.do_action(hero2.flying_speed)

