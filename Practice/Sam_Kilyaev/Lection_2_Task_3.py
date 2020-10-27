import random


class Run:
    def run(self):
        print("I`m running!")


class FastRun(Run):
    def run(self):
        print("I`m running very fast!")


class SlowRun(Run):
    def run(self):
        print("I`m frozen")


class Samurais:
    action = Run()
    x = 0
    y = 0

    def run(self):
        self.action.run()
        self.x += 1
        self.y += 1

    def runFast(self):
        self.action.run()
        self.x += 3
        self.y += 3

    def runSlow(self):
        self.action.run()
        self.x -= 2
        self.y -= 2

    def set_action(self, new_action):
        self.action = new_action

    def draw(self):
        print(f"I`m Samurai at - {self.x} : {self.y}")

    def shooting(self):
        print("I open fire from my samurai's gun")


def pick_up(thing):
    print("I pick up somewhat!")
    i = random.randint(0, 1)
    if i == 1:
        print("I'm Flash")
        thing.set_action(FastRun())
        thing.run = thing.runFast

    else:
        print("I can not move faster!")
        thing.set_action(SlowRun())
        thing.run = thing.runSlow


class Oni(Samurais):
    def draw(self):
        print(f"I`m Oni at - {self.x}:{self.y}")

    def fly(self):
        self.x += 10
        self.y += 10


class Nindja(Samurais):
    def draw(self):
        print(f"I`m Nindja at - {self.x}:{self.y}")


class KianeRivz(Samurais):
    def draw(self):
        print(f"I`m Kianu Rivz at - {self.x}:{self.y}")
