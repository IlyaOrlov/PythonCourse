#Лекция ДВА
# first task
def biggestPrint(a,b):
    if(a>b):
        print(a)
    else: print(b)
biggestPrint(2,4)
biggestPrint(15,11)

#second task
def biggestReturn(a,b):
    if(a>b):
        return a
    else:return b
result = biggestReturn(100,200)
result2=biggestReturn(1000,500)
print(result)
print(result2)

#oop task GAME
class Characters:
    def __init__(self,name,capability):
        self.name=name,
        self.capability=capability
    @staticmethod
    def gameStarted():
        print("Game started")

    def running(self,speed):
        print(f'{self.name} is beginning running with speed {speed}')
        return 'Running'

    def usingCapability(self):
        print(f'{self.name}using capability {self.capability}')
        return self.capability

    def pickUpItemForUpgrade(self):
        print(f'{self.name}picked up item BonusSpeed')
        return 'BonusSpeed'

    def pickUpItemForDowngrade(self):
        print(f'{self.name}picked up item SlowSpeed')
        return 'SlowSpeed'

    def UsingItem(self,item,speed,obj):
        print(f"{self.name}using item on {obj}")
        if item == 'BonusSpeed':
            return speed + 10
        elif item=='SlowSpeed':
            return speed - 20
        else : return 0

    def flying(self,speed):
        print(f'{self.name} is beginning flying with speed {speed} ')
        return 'flying'
    #воспроизвести в зависимости от действия анимацию
    def chooseAnimation(self,anim):
        if anim == 'Running':
            print(f'{self.name} run animation starts')
        if anim == 'flying':
            print(f'{self.name} fly animation starts')
        if anim == 'Shooting':
            print(f'{self.name} shooting animation starts')
        if anim == 'Attack from air':
            print(f'{self.name} attack from air animation starts')
        if anim == 'Attack with axe':
            print(f'{self.name} attack with axe animation starts')
    #Взять анимацию
    def getAnim(self,anim):
        return anim
    
    def getItem(self,item):
        return item

Characters.gameStarted()
human = Characters("Human","Shooting")
daemon = Characters("Demon","Attack from air")
ork=Characters("Ork","Attack with axe")

human.chooseAnimation(human.getAnim(human.running(50)))
daemon.chooseAnimation(daemon.getAnim(daemon.flying(100)))
ork.chooseAnimation(ork.getAnim(ork.running(75)))
speedDown = daemon.UsingItem(daemon.getItem(daemon.pickUpItemForDowngrade()),50,'Human')
human.chooseAnimation(human.getAnim(human.running(speedDown)))
speedUp=human.UsingItem(human.getItem(human.pickUpItemForUpgrade()),speedDown,'Human')
human.chooseAnimation(human.getAnim(human.running(speedUp)))
human.chooseAnimation(human.getAnim(human.usingCapability()))
daemon.chooseAnimation(daemon.getAnim(daemon.usingCapability()))
ork.chooseAnimation(ork.getAnim(ork.usingCapability()))
