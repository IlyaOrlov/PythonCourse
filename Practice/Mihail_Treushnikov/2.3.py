from abc import ABC, abstractmethod

class ComputerGame(ABC):

    @abstractmethod
    def running(self):
        pass

    @abstractmethod
    def shooting(self):
        pass

    @abstractmethod
    def coolecting(self, obj):
        pass


class standart_Charachter(ComputerGame):

    def __init__(self, name, gender, speed, shoots, list=[]):
        self._name = name
        self._gender = gender
        self._speed = speed
        self._shoots = shoots
        self.list = list
        print("Hello my name {}".format(name))

    @property
    def speed(self):
        return self._speed

    @speed.deleter
    def speed(self):
        self._speed = 'No more'

    @speed.setter
    def speed(self, value):
        self._speed = value

    def running(self):
        print("I am running with speed {}".format(self._speed))

    def shooting(self):
        self._shoots -= 1
        print("I am shooted and i have {}".format(self._shoots))

    def coolecting(self, obj):
        if (obj != object):
            return 0
        else:
            self.list.append(obj)


class fly_Charachter(standart_Charachter):

    def __init__(self, flight_altitude, flying_speed, name, gender, speed, shoots, list=[]):
        super().__init__(name, gender, speed, shoots, list)
        self._flight_altitude = flight_altitude
        self._flying_speed = flying_speed
        print("Hello my name {}".format(name))

    @property
    def speed(self):
        return self._speed

    @speed.deleter
    def speed(self):
        self._speed = 'No more'

    @speed.setter
    def speed(self, value):
        self._speed = value

    def running(self):
        print("I am running with speed {}".format(self._speed))

    def shooting(self):
        self._shoots -= 1
        print("I am shooted and i have {}".format(self._shoots))

    def coolecting(self, obj):
        if (obj != object):
            return 0
        else:
            self.list.append(obj)

    def Flyinh(self):
        print("I am flying with on height {} and speed {}"
              .format(self._flight_altitude, self._flying_speed))


# there are two class which imitate items
class LootUp:
    def __init__(self, name, obj):
        if hasattr(obj, 'speed'):
            self.name = name
            self.obj = obj

    def upgrade(self):
        self.obj.speed *= 2


class LootDown:
    def __init__(self, name, obj):
        if hasattr(obj, 'speed'):
            self.name = name
            self.obj = obj

    def upgrade(self):
        self.obj.speed /= 2



# Create two characters
Person1 = standart_Charachter('Mike', 'male', 10, 5)
Person2 = fly_Charachter(10000, 20, 'Alina', 'femal', 5, 10)

# Create two items
Loot1 = LootUp('speedUpgrade', Person1)
Loot2 = LootDown('speedDegradation',Person1)

# Put items in Object1 list
Person1.list.append(Loot1)
Person1.list.append(Loot2)


# Use item
Person1.list[0].upgrade()

# Just demonstrate
Person1.running()
