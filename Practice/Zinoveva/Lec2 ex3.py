class Items():
    x = 3
    some_option = 10

class Person():
    x = 0
    y = 0
    def go(self):
        self.x = self.x + 1
    
    def show_where_i(self):
        print("x:{}, y{}", self.x, self.y)

    def fly(self):
        print("i can't")

    def shoot(self):
        print("pau-pau")

class SupPerson(Person):
    
    def fly(self):
        self.y = self.y + 1

def main():
    
    itm     = Items()
    person  = Person()
    sperson = SupPerson()
    persons = list()
    persons.append(person)
    persons.append(sperson)
    
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
        
        if persons[number].x == itm.x:
            print("player{} got item", )
       
    
main()