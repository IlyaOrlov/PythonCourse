import random


class RunAction:
    def run(self):
        print("I`m running!")

class FastRunAction(RunAction):
    def run(self):
        print("I`m running very fast!!!")

class SlowRunAction(RunAction):
    def run(self):
        print("I`m running slower!!!")

class Warriors:
    run_action = RunAction()
    x = 0

    def run(self):
        self.run_action.run()
        self.x += 1

    def runFast(self):
        self.run_action.run()
        self.x += 2

    def runSlow(self):
        self.run_action.run()
        self.x -= 2

    def set_action(self, new_action):
        self.run_action = new_action

    def draw(self):
        print(f"I`m warrior at - {self.x}")

    def shoot(self):
        print("BA-baHhhh!!!!")

def leftUp(warrior):
    print("I pick up something!")
    i = random.randint(0, 1)
    if i == 1:
        print("you found thing! It is + 2 speed!!!")
        warrior.set_action(FastRunAction())
        warrior.run = warrior.runFast

    else:
        print("you found thing! It is - 2 speed!!!")
        warrior.set_action(SlowRunAction())
        warrior.run = warrior.runSlow

class CaptainVdv(Warriors):
    def draw(self):
        print(f"I`m CaptainVdv at - {self.x}")

    def fly(self):
        self.x += 2

class MajorInfantry(Warriors):
    def draw(self):
        print(f"I`m MajorInfantry at - {self.x}")

class ColonelAviation(Warriors):
    def draw(self):
        print(f"I`m ColonelAviation at - {self.x}")

warrior = [CaptainVdv(), ColonelAviation(), MajorInfantry()]

for warr in warrior:
    warr.draw()
while True:
    pers = int(input("Choose your warrior: | 0.CaptainVdv | 1.ColonelAviation | 2.MajorInfantry |: "))
    if pers != 0 and pers != 1 and pers != 2:
        print("Wrong choise!!!")
        continue
    choose = input("What a warrior has to do? Select, please!: | 1.Run | 2.Shoot | 3.Fly | 4.Pick up an item | 5.Exit |: ")
    if choose == '1':
        warrior[pers].run()
    elif choose == '2':
        warrior[pers].shoot()
    elif choose == '3':
        if pers == 0:
            warrior[pers].fly()
        else:
            print("This warrior can`t fly!!!")    
    elif choose == '4':
        leftUp(warrior[pers])
    elif choose == '5':
        break    
    else:
        print("Wrong choise!!!")
        continue
    for warr in warrior:
        warr.draw()