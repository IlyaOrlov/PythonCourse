#1
import datetime
import time
def dateFun(date1, date2):
    workingDates = []
    delta = datetime.timedelta(1)
    tempDate = date2
    while tempDate <= date1:
        if (tempDate.weekday() != 5) & (tempDate.weekday() != 6):
            workingDates.append(tempDate)
        tempDate += delta
    return len(workingDates)

time1 = datetime.date(2020, 8, 1)
time2 = datetime.date(2020, 8, 31)
print(dateFun(time2, time1))

#2
from subprocess import PIPE, Popen
def subProc(fileDirection):
    fileName = ("%r"%fileDirection)[1:-1]
    proc = Popen(['type', fileName], stdout = PIPE, stderr = PIPE, shell=True)
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1])
    print(res[0])

subProc('.\task_7.py')

#3
import pickle
from random import choice, randint

names = ['Jhon', 'Bob', 'Clara', 'Kate', 'Boris']
surnames = ['Din-Don', 'Ivanov', 'Schmidt', 'Barashek', 'Lol']
genders = ['man', 'woman']
adresses = ['Paris', 'Moscow', 'London', 'Berlin', 'Boston']

class Human(object):
    def __init__(self):
        self.name = choice(names)
        self.surname = choice(surnames)
        self.age = randint(1,100)
        self.gender = choice(genders)
        self.adress = choice(adresses)
    def printHuman(self):
        print(self.name, self.surname, self.age, self.gender, self.adress)

with open('./human.data', 'wb') as outF:
    humans = []
    for i in range (5):
        human = Human()
        humans.append(human)
    pickle.dump(humans, outF)

with open('./human.data', 'rb') as inF:
    try:
        people = pickle.load(inF)
    except EOFError:
        pass

for p in people:
    p.printHuman()
