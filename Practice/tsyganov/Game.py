class Hero:
    def name(self):
        print("I'm ", Name)

    def move(self):
        print('идти')

    def take(self):
        print('взять предмет')

    def weapons(self):
        print('Способность не открыта')

    def fly(self):
        print('Способность не открыта')

class Skills(Hero):
    def weapons(self):
        print("Выстрел")

    def fly(self):
        print("Полет")

# Cценарии:
def project_1():
    action = input('Выберите действие  "move"  ')
    if action =='move':
        Name.move()
    else:
        action = input('Выберите действие: "move"')
        if action =='move':
            Name.move()

def project_2():
    action = input('Выберите действие "take" ')
    if action == 'take':
        print('Открыта новая способность - "Полет"')
    else:
        action = input('Выберите действие: "take"')
        if action == 'take':
            print('Открыта новая способность - "Полет"')
def project_3():
    action = input('Выберите действие: "move" or "fly"')
    if action =='fly':
        Name = Skills()
        Name.fly()
        print('Чуть не погиб')
    elif action=='move':
        Name.move()
        print('Game over')

Name=input('укажите имя героя ')
Name = Hero() #присвоение класса
Name.name()  #вызов имени

x=1
while x <4:
    print('round №', x)  # число раунда

    if x ==1:
        project_1()

    elif x==2:
        print('Внимание предмет!!!')
        project_2()

    elif x ==3:
        print('Внимание обрыв!!')
        project_3()

    x+=1
