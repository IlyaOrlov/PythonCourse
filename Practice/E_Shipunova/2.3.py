class Character:
    speed = 40       # km/h standard
    shots = 5        # standard
    collection = []  # list with items
    # in this classes item=fast_item.value == 2 or item=slowly_item.value == 0.5(look at the class Item)
    # for all methods standard version if item==1, else we used item = collection[index] (value 2 or 0.5)
    # when using the item must pass in methods fast_item.value or slowly_item.value

    def __init__(self):
        print("I was born.")
        print(f"My standard speed = {self.speed} km/h")
        print(f"My standard shots = {self.shots}")
        print("My collection is empty")

    def run(self, item=1):
        speed_run = self.speed*item  # for fast or slowly speed
        print(f"I'm running, my speed = {speed_run} km/h!")
        if item != 1:
            self.collection.remove(item)  # we used this item

    def shoot(self, item=1):
        shots_shoot = self.shots*item  # for increase or decrease number of shots
        print("I shoot ", int(shots_shoot), "time!")  # int( may be float)
        if item != 1:
            self.collection.remove(item)  # we used this item

    def collect(self, item):
        print("I took the new item!")
        self.collection.append(item)  # add item
        print("My collection is ", self.collection)


class Person(Character):

    def __init__(self):
        super()
        print("I am Person")


class Dracula(Character):

    def __init__(self):
        super()
        self.speed *= 7
        self.shots *= 3
        self.speed_fly = self.speed*10
        self.blood = 4.5   # liters standard
        print(f"I'm flying, my standard speed = {self.speed} km/h of fly")
        print(f"Usually I drink = {self.blood} liters' blood")
        print("I am Dracula")

    def fly(self, item=1):
        self.speed_fly *= item  # for fast or slowly speed
        print(f"I'm flying, my speed = {self.speed_fly} km/h!")
        if item != 1:
            self.collection.remove(item)  # we used this item

    def drink_blood(self, item=1):
        liter_blood = self.blood*item
        print(f"I'm drink {liter_blood} liters!")
        if item != 1:
            self.collection.remove(item)  # we used this item


class Ichthyander(Character):

    def __init__(self):
        super()
        self.speed *= 5
        self.shots *= 2
        self.speed_swim=self.speed*3
        print(f"I'm swimming, my standard speed = {self.speed_swim}  km/h!")
        print("I am Ichthyander")

    def swim(self, item=1):
        self.speed_swim *= item  # for fast or slowly speed
        print(f"I'm swimming, my speed = {self.speed_swim}  km/h!")
        if item != 1:
            self.collection.remove(item)  # we used this item



class Item:
    value = 1


class FastItem(Item):    # fast_item=FastItem() and fast_item.value==2
    def __init__(self):
        self.value = 2


class SlowlyItem(Item):  # slowly_item=SlowlyItem() and slowly_item.value==0.5
        def __init__(self):
            self.value = 0.5

