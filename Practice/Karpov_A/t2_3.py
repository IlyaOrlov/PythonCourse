class Specif():
    speed = 3
    jump = 4
    shot = 10

class Charact():
    x = 0
    y = 0
    def walk(self):
        self.x = self.x + 1

    def show_where_i(self):
        print("x:{}, y{}", self.x, self.y)

    def fly(self):
        print("I can'fly")

    def shoot(self):
        print("I can shoot")

    def jump(self):
        print("I can jump")

class SpecCharact(Charact):

    def fly(self):
        self.y = self.y + 1

def main():

    spec     = Specif()
    charact  = Charact()
    scharact = SpecCharact()
    persons = list()
    persons.append(charact)
    persons.append(scharact)

    while(1):
        print("input number of player")
        number = int(input())
        print("input command to player")
        command = input()

        if command == "go":
            persons[number].go()
        elif command == "shoot":
            persons[number].shoot()
        elif command == "fly":
            persons[number].fly()
        else:
            print("Unknown command: {}".format(command))

        persons[number].show_where_i()

        if persons[number].x == spec.x:
            print("player{} got item", )


