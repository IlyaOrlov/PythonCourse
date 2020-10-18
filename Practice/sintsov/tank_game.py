import random
import time
import os
import msvcrt
import math
from random import randint

class Item():
    _xCord = 1
    _yCord = 1
    _cellSymb = ""
    _step = 1
    _shot = 1
    _direction ="north"
    _state = ""
    _name = ""
    def __init__(self, arena):
        self.arena = arena
    def getX(self):
        return self._xCord
    def getY(self):
        return self._yCord
    def getSymb(self):
        return self._cellSymb
    def getDir(self):
        return self._direction
    def setX(self, x):
        self._xCord = x
    def setY(self, y):
        self._yCord = y
    def getState(self):
        return self._state
    def setState(self, str):
        self._state = self._state.replace(self._state, str)
    def getName(self):
        return self._name

    def isRightDirection(self, item2):
        if ((self._yCord > self.arena.hight - 1)
                or (self._yCord < 0)
                or (self._yCord == item2.getY())
                or (self._xCord > self.arena.width - 1)
                or (self._xCord < 0)
                or (self._xCord == item2.getX())):
            return False
        return True

    def defaultMoving(self, direction, item2, factor):
        step = self._step * factor
        if (direction == 'w'):
            self._yCord -= step
            self._direction = 'north'
        elif (direction == 's'):
            self._yCord += step
            self._direction = 'south'
        elif (direction == 'a'):
            self._xCord -= step
            self._direction = 'west'
        elif (direction == 'd'):
            self._xCord += step
            self._direction = 'east'
        elif (direction == 'q'):
            self._yCord -= step
            self._xCord -= step
            self._direction = 'north-west'
        elif (direction == 'e'):
            self._yCord -= step
            self._xCord += step
            self._direction = 'north-east'

    def doubleStepMoving(self, direction, item2, factor):
        doubleStep = self._step * 2 * factor
        if (direction == 'w'):
            self._yCord -= doubleStep
            self._direction = 'north'
        elif (direction == 's'):
            self._yCord += doubleStep
            self._direction = 'south'
        elif (direction == 'a'):
            self._xCord -= doubleStep
            self._direction = 'west'
        elif (direction == 'd'):
            self._xCord += doubleStep
            self._direction = 'east'
        elif (direction == 'q'):
            self._yCord -= doubleStep
            self._xCord -= doubleStep
            self._direction = 'north-west'
        elif (direction == 'e'):
            self._yCord -= doubleStep
            self._xCord += doubleStep
            self._direction = 'north-east'

    def move(self, direction, item2, movingType):
        moving = self.defaultMoving
        if (movingType == 'DOUBLESTEP'):
            moving = self.doubleStepMoving
        moving(direction, item2, 1)
        self.setState("RUNNING")

        if (not isRightDirection):
            moving(direction, item2, -1)
            self.setState("WRONG WAY")

    def shoot(self, bang):
        if (self._direction == 'north'):
            if (self._yCord - self._shot > 0):
                bang.setY(self._yCord - self._shot)
            else:
                self.setState("WRONG SHOT")
        elif (self._direction == 'south'):
            if (self._yCord + self._shot < self.arena.hight - 1):
                bang.setY(self._yCord + self._shot)
            else:
                self.setState("WRONG SHOT")
        elif (self._direction == 'west'):
            if (self._xCord - self._shot > 0):
                bang.setX(self._xCord - self._shot)
            else:
                self.setState("WRONG SHOT")
        elif (self._direction == 'east'):
            if (self._xCord + self._shot < self.arena.width - 1):
                bang.setX(self._xCord + self._shot)
            else:
                self.setState("WRONG SHOT")
        elif (self._direction == 'north-west'):
            if (self._yCord - self._shot > 0 and self._xCord - self._shot > 0):
                bang.setY(self._yCord - self._shot)
                bang.setX(self._xCord - self._shot)
            else:
                self.setState("WRONG SHOT")
        elif (self._direction == 'north-east'):
            if (self._yCord - self._step > 0 and self._xCord + self._step < self.arena.width - 1):
                bang.setY(self._yCord - self._step)
                bang.setX(self._xCord + self._step)
            else:
                self.setState("WRONG SHOT")


class Bang:
    def __init__(self, tank):
        self._tank = tank
        self._xCord = self._tank.getX()
        self._yCord = self._tank.getY()
    def getX(self):
        return self._xCord
    def getY(self):
        return self._yCord
    def setX(self, x):
        self._xCord = x
    def setY(self, y):
        self._yCord = y
    def updateCords(self):
        self._xCord = self._tank.getX()
        self._yCord = self._tank.getY()


class Tank_T34(Item):
    _name = "TANK T34"
    _cellSymb = "T"
    _step = 2
    _shot = 1


class Tank_Tiger(Item):
    _name = "TANK TIGER"
    _cellSymb = "8"
    _step = 1
    _shot = 2
    _dialWrongWay = "WRONG WAY"


class Aim (Item):
    _name = "AIM"
    _cellSymb = "@"
    _step = 1
    _cellSymbAfterBang = "X"

    def setCellSymb(self):
        self._cellSymb = self._cellSymbAfterBang

class Arena:
    _emptyCell = ' '
    _borderCell = '#'
    hight = 0
    width = 0
    arena = []
    typeTank = ""
    command = ""
    dialog = ""
    instruction = "The command-list:\n 'w' - up,\n 's' - down,\n 'a' - left,\n 'd' - right,\n 'q' - left-up," \
                  "\n 'e' - right-up,\n space - shoot,\n 'n' - new game,\n 'x' - end game"

    def __init__(self, nHight, nWidth):
        self.hight = nHight+2
        self.width = nWidth+2

    def _createArena(self):
        self.arena = [0] * self.hight
        self.arena[0] = self.arena[self.hight - 1] = [self._borderCell] * self.width
        for i in range(1, (self.hight - 1)):
            self.arena[i] = [0] * self.width
            self.arena[i][0] = self.arena[i][self.width - 1] = self._borderCell
            for j in range(1, (self.width - 1)):
                self.arena[i][j] = self._emptyCell
        if (self.typeTank == "2"):
            self.tank = Tank_Tiger(self)
        else:
            self.tank = Tank_T34(self)
        self.aim = Aim(self)
        self.bang = Bang(self.tank)
        self.setDialog("ENTER THE COMMAND")

    def _updateArena(self):
        for i in range(1, (self.hight-1)):
            self.arena[i][0] = self.arena[i][self.width - 1] = self._borderCell
            for j in range(1, (self.width - 1)):
                self.arena[i][j] = self._emptyCell
        self.arena[self.tank.getY()][self.tank.getX()] = self.tank.getSymb()
        self.arena[self.aim.getY()][self.aim.getX()] = self.aim.getSymb()

    def _printArena(self):
        os.system('cls')
        print(self.instruction)
        for i in range(self.hight):
            for j in range (self.width):
                print(self.arena[i][j], end="")
            print('\n', end="")
        print("Tank cords: ", self.tank.getX(), self.tank.getY())
        print("Aim cords: ", self.aim.getX(), self.aim.getY())
        print("Shot cords: ",self.bang.getX(),self.bang.getY())
        print ("Direction: "+self.tank.getDir())
        print(self.dialog)

    def _locateTank(self):
        self.tank.setX(randint(1,self.width-2))
        self.tank.setY(randint(1, self.hight-2))
        self.bang.updateCords()

    def _lokateAim(self):
        self.aim.setX(self.tank.getX())
        self.aim.setY(self.tank.getY())
        while (abs(self.aim.getX() - self.tank.getX()) <= 1):
            self.aim.setX(randint(1, self.width - 2))
        while (abs(self.aim.getY() - self.tank.getY()) <= 1):
            self.aim.setY(randint(1, self.hight - 2))

    def _getCommand(self):
        # s = input()
        s=msvcrt.getche().decode('utf-8')
        self.command = self.command.replace(self.command, s)

    def setDialog(self, str):
        self.dialog = self.dialog.replace(self.dialog, str)

    def _moveTank(self):
        if (self.command == 'w'):
            self.tank.move('w', self.aim, 'DEFAULT')
            self.bang.updateCords()
        elif (self.command == 's'):
            self.tank.move('s', self.aim, 'DEFAULT')
            self.bang.updateCords()
        elif (self.command == 'a'):
            self.tank.move('a', self.aim, 'DEFAULT')
            self.bang.updateCords()
        elif (self.command == 'd'):
            self.tank.move('d', self.aim, 'DEFAULT')
            self.bang.updateCords()
        elif (self.command == 'q'):
            self.tank.move('q', self.aim, 'DEFAULT')
            self.bang.updateCords()
        elif (self.command == 'e'):
            self.tank.move('e', self.aim, 'DEFAULT')
            self.bang.updateCords()

    def _shootTank(self):
        if (self.command == ' '):
            self.tank.shoot(self.bang)
            if (self.dialog != "WRONG SHOT"):
                self._checkShot()

    def _checkShot(self):
        if (self.aim.getX() == self.bang.getX() and self.aim.getY() == self.bang.getY()):
            self.setDialog("HIT THE TARGET!")
        #else:
            self.setDialog("YOU ARE MISS")


    def _moveAim(self):
        r = randint(1,4)
        if (r == 1):
            self.aim.move('w', self.tank, 'DEFAULT')
        elif (r == 2):
            self.aim.move('s', self.tank, 'DEFAULT')
        elif (r == 3):
            self.aim.move('a', self.tank, 'DEFAULT')
        elif (r == 4):
            self.aim.move('d', self.tank, 'DEFAULT')

    def _startMenu(self):
        print("Tanki the Game (by asintsov)")
        print("Choice your Tank: ")
        print("T34 - fast, but short-range : step=2, shot=1. Button for choice: 1")
        print("Tiger - long-range, but slow: step=1, shot=2. Button for choice: 2")
        print("Input number of the Tank")
        #str = input()
        s = msvcrt.getche().decode('utf-8')
        self.typeTank = self.typeTank.replace(self.typeTank, s)
        print("LET THE FIGHT BEGIN")


    def startGame(self):
        os.system('cls')
        self._startMenu()
        os.system('cls')
        self._createArena()
        self._locateTank()
        self._lokateAim()
        self._updateArena()
        self._printArena()
        self._playGame()

    def _endGame(self):
        self.aim.setCellSymb()
        self._updateArena()
        self._printArena()
        print("YOU ARE WINNER!!!")

    def _missShot(self):
        distance = round(math.sqrt(((self.tank.getX() - self.aim.getX()) ** 2) + ((self.tank.getY() - self.aim.getY()) ** 2)), 3)
        return "miss! distance is = {d} kilometrs".format(d = distance)


    def _playGame(self):
        while(True):
            self._getCommand()
            if (self.command == 'x'):
                break
            elif(self.command == 'n'):
                self.startGame()
                break
            elif (self.command == 'w' or self.command == 's'
                  or self.command == 'a' or self.command == 'd'
                  or self.command == 'q' or self.command == 'e'):
                self._moveTank()
                if (self.tank.getState() != "WRONG WAY" and self.tank.getState() != "WRONG SHOT"):
                    self.setDialog(self.tank.getState())
                    self._updateArena()
                    self._printArena()
                    time.sleep(1)
                    self._moveAim()
                    while (self.aim.getState() != "RUNNING"):
                        self._moveAim()
                else:
                    self.setDialog(self.tank.getState())
            elif (self.command == ' '):
                self._shootTank()
                if (self.tank.getState() == "WRONG SHOT"):
                    self.setDialog(self.tank.getState())
                else:
                    if (self.dialog == "HIT THE TARGET!"):
                        self._endGame()
                        self._getCommand()
                        self.startGame()
                        break
                    else:
                        self.dialog = self._missShot()
            else:
                self.setDialog("WRONG COMMAND")
            self._updateArena()
            self._printArena()


a = Arena(10,10)
a.startGame()