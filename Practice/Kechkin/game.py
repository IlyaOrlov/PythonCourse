import random
import time


class Characters:  # main class for all
    _health = 100
    _speed = 10
    _jump = 5
    _shoot = 50  # power of shoot
    _status = False  # Dead or Alive

    def getStatus(self):
        if not self._status:
            print("Alive")
        else:
            print("Dead")

    def damage(self, damage):
        if not self._status:
            self._health = self._health - damage
            if self._health > 0:
                print("Damage: ", damage)
                print("health: ", self._health)
            else:
                self._status = True
                print("dead: ", self._health)

    def show_health(self):
        print("My health: ", self._health)

    def collect_items(self):  # Black box or something like that

        if not self._status:
            _item = random.randint(1, 4)
            if _item == 1:
                self._health += random.randint(1, 10)
                print("health++ ")
            elif _item == 2:
                self._speed += random.randint(1, 5)
                print("speed++ ")
            elif _item == 3:
                self._jump += random.randint(1, 5)
                print("jump++ ")
            elif _item == 4:
                self._shoot += random.randint(1, 5)
                print("shoot++ ")

    def run(self):
        if not self._status:
            self._speed += 4
            print("run: speed", self._speed)

    def jump(self):
        if not self._status:
            self._jump += 2
            print("jump:", self._jump)

    def shoot(self):
        if not self._status:
            print("I'm shooting: power", self._shoot)


class Solder(Characters):
    _health = 200
    _grenade = 40

    def throw_grenade(self):
        if not self._status:
            print("throw grenade:", self._grenade)
            time.sleep(3)
            print("BA-BAH")


class FlySolder(Characters):  # solder is using jet pack for example
    _health = 150
    _flySpeed = 40
    _shoot = 30
    _turbo = 10

    def fly(self):
        if not self._status:
            self._flySpeed += 2
            print("fly: speed", self._flySpeed)

    def turboSpeed(self):
        if not self._status:
            self._flySpeed += self._turbo
            print("Turbo on: speed", self._flySpeed)


class DriverSolder(Characters):  # just a driver
    _carSpeed = 80
    _turbo = 5

    def drive(self):
        if not self._status:
            print("driving: speed", self._carSpeed)

    def turboDrive(self):
        if not self._status:
            self._carSpeed += self._turbo
            print("Turbo on: speed", self._carSpeed)


if __name__ == '__main__':  # point for start
    # for demonstration only
    solder = Solder()
    driver = DriverSolder()
    flySolder = FlySolder()

    print("---------solder------------")
    solder.show_health()
    solder.run()
    solder.jump()
    solder.throw_grenade()
    solder.damage(75)
    time.sleep(2)

    print("---------driver-------------")
    driver.getStatus()
    driver.drive()
    driver.turboDrive()
    time.sleep(2)

    print("-------flySolder--------------")
    flySolder.fly()
    flySolder.shoot()
    flySolder.turboSpeed()
