import random


class Player:
    x = 1

    def name(self):
        x = str(input(self.x))
        return x

    def cond(self, x):
        self.x = x
        print("{} ready to game".format(self.x))

    def move(self):
        print('I move to')

    def run(self):
        print("Okay, i run to")

    def slow(self):
        print("Wtf, i so slowly")

    def pick(self):
        print('I picked up')

    def shoot(self):
        print('I see the target')


class sky_player(Player):
    def move(self):
        print('i believe i can touch the sky')


class obj:
    def drop(self):
        print('im here')

    def picked(self):
        print('Picked at:')


def progress(play):
    play.move()
    play.run()
    play.pick()
    play.slow()
    play.cond()


command_list = ["name", "cond", "move", "run", "slow", "pick", "shoot"]
Players = [Player(), Player(), sky_player()]
for all in Players:
    while True:
        choice = int(input("input player number(in range 1 to 3):")) - 1
        if choice > 2:
            continue
        command = random.choice(command_list)
        print(command)
        if command == "name":
            name = Players[choice].name()
            Players[choice].cond(name)
        elif command == "cond":
            print("oh, i havent name please input")
            name = Players[choice].name()
            Players[choice].cond(name)
        elif command == "move":
            Players[choice].move()
        elif command == "run":
            Players[choice].run()
        elif command == "slow":
            Players[choice].slow()
        elif command == "pick":
            Players[choice].pick()
            Players[choice].slow()
        elif command == "shoot":
            Players[choice].shoot()
        else:
            print("Try again")
            break
