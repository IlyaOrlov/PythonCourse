class Tank:
    x = 0

    def draw(self):
        print("I'm Tank at {}".format(self.x))

    def move(self):
        self.x += 1

    def shoot(self):
        print("Ba-bah")


class T34(Tank):
    def draw(self):
        print("I'm T34 at {}".format(self.x))

class Tiger(Tank):
    def draw(self):
        print("I'm Tiger at {}".format(self.x))


tanks = [Tank(), T34(), Tiger()]
for tank in tanks:
    tank.draw()
while True:
    cmd = input("Введите команду (shoot или move): ")
    n = int(input("Введите номер танка (от 0 до 2): "))
    if cmd == "move":
        tanks[n].move()
    elif cmd == "shoot":
        tanks[n].shoot()
    else:
        break
    for tank in tanks:
        tank.draw()

