a = 2
b = 2
c = 2
d = 2
class Player1:
    x = 0
    y = 0
    global a
    def draw(self):
        print("I Player1 to {}".format(self.x))

    def runforward(self):
        self.x += a
        print("I run to {}".format(self.x))

    def runback(self):
        if self.x < a:
            self.x = 0
            print("I run to {}".format(self.x))
        else:
            self.x -= a
            print("I run to {}".format(self.x))

    def shoot(self):
        print("Trrrrr")

    def take(self):

        def predmet1():
            global a
            a += 1
            print("Uskorenie na 1")

        def predmet2():
            global a
            a -= 1
            print("Zamedlenie na 1")

        cmd = input("Какой предмет взять: predmet1, predmet2:")
        if cmd == "predmet1":
            predmet1()
        elif cmd == "predmet2":
            predmet2()

    def flyup(self):
        print("I can't fly")

    def flydown(self):
        print("I can't fly")

class Player2(Player1):
    global b
    def draw(self):
        print("I Player2 to {}".format(self.x))

    def runforward(self):
        self.x += b
        print("I run to {}".format(self.x))

    def runback(self):
        if self.x < b:
            self.x = 0
            print("I run to {}".format(self.x))
        else:
            self.x -= b
            print("I run to {}".format(self.x))

    def take(self):

        def predmet1():
            global b
            b += 1
            print("Uskorenie na 1")

        def predmet2():
            global b
            b -= 1
            print("Zamedlenie na 1")

        cmd = input("Какой предмет взять: predmet1, predmet2:")
        if cmd == "predmet1":
            predmet1()
        elif cmd == "predmet2":
            predmet2()


class Player3(Player1):
    global c
    def runforward(self):
        self.x += c
        print("I run to {}".format(self.x))

    def runback(self):
        if self.x < c:
            self.x = 0
            print("I run to {}".format(self.x))
        else:
            self.x -= c
            print("I run to {}".format(self.x))

    def draw(self):
        print("I Player3 to {}".format(self.x))

    def flyup(self):
        self.y+=1
        print("I'm flying to a height of {}".format(self.y))

    def flydown(self):
        if (self.y == 0):
            print("I'm on earth")
        else:
            self.y -= 1
            print("I'm flying to a height of {}".format(self.y))

    def take(self):

        def predmet1():
            global c
            c += 1
            print("Uskorenie na 1")

        def predmet2():
            global c
            c -= 1
            print("Zamedlenie na 1")

        cmd = input("Какой предмет взять: predmet1, predmet2:")
        if cmd == "predmet1":
            predmet1()
        elif cmd == "predmet2":
            predmet2()


class Player4(Player3):
    global d
    def runforward(self):
        self.x += d
        print("I run to {}".format(self.x))

    def runback(self):
        if self.x < d:
            self.x = 0
            print("I run to {}".format(self.x))
        else:
            self.x -= d
            print("I run to {}".format(self.x))


    def draw(self):
        print("I Player4 to {}".format(self.x))

    def take(self):

        def predmet1():
            global d
            d += 1
            print("Uskorenie na 1")

        def predmet2():
            global d
            d -= 1
            print("Zamedlenie na 1")

        cmd = input("Какой предмет взять: predmet1, predmet2:")
        if cmd == "predmet1":
            predmet1()
        elif cmd == "predmet2":
            predmet2()


players = [Player1(), Player2(), Player3(), Player4()]
for player in players:
    player.draw()
while True:
    cmd = input("Введите команду (shoot, runforward, runback, flyup, flydown, take): ")
    n = int(input("Введите номер персонажа (от 0 до 3): "))
    if cmd == "runforward":
        players[n].runforward()
    elif cmd == "runback":
        players[n].runback()
    elif cmd == "shoot":
        players[n].shoot()
    elif cmd == "flyup":
        players[n].flyup()
    elif cmd == "flydown":
        players[n].flydown()
    elif cmd == "take":
        players[n].take()
    else:
        break
    for player in players:
        player.draw()