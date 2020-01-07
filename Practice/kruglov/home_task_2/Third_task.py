class Human:
    state = "Staying"

    # under development
    def status(self):
        print("My status - {}".format(self.state))

    def animation(self):
        print("Animation - {}".format(self.state))

    def draw(self):
        print("I'm Human")

    def run(self):
        Human.state = "Runing"
        Flyer.state = "Runing"

    def shoot(self):
        Human.state = "Shoting"
        Flyer.state = "Shoting"


class Flyer(Human):
    def draw(self):
        print("I'm Flyer")

    def fly(self):
        Flyer.state = "Flying"


players = [Human(), Flyer()]
for player in players:
    player.draw()
while True:
    cmd = input("Please entering cmd (shoot, run or fly): ")
    if cmd == "run":
        player.run()
    elif cmd == "shoot":
        player.shoot()
    elif cmd == "fly":
        player.fly()
    else:
        break
    for player in players:
        player.draw()
        player.animation()
