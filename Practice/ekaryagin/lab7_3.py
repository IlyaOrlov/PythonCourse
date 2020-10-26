import pickle
from random import randint as rand
from random import choice


class Human:

    def __init__(self, name, surname, age, city, position, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.position = position
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} years old, {self.city} city, {self.position}, {self.phone}"


def create_human(number):
    humans = []
    name = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas"]
    surname = ["Abramson", "Hoggarth", "Adamson", "Holmes", "Fulton", "Mercer", "Calhoun", "Miln", "Farrell", "Ryder"]
    position = ["Actor", "Baby-sitter", "Cook", "Clerk", "Dentist", "Engineer", "Tailor", "Waiter", "Writer", "Soldier"]
    city = ["Austin", "Baltimore", "Chicago", "Dallas", "El Paso", "Fairfield", "Gilbert", "Hampton", "Killeen"]

    for i in range(number):
        humans.append(
            Human(choice(name), choice(surname), rand(18, 35), choice(city), choice(position), phone()))

    with open("human.data", "wb") as f:
        pickle.dump(humans, f)


def phone():
    random_phone = ["+1 ", rand(2, 9), rand(0, 9), rand(0, 9), " ", rand(0, 9), rand(0, 9), rand(0, 9), "-", rand(0, 9),
                    rand(0, 9), "-", rand(0, 9), rand(0, 9)]
    return "".join([str(x) for x in random_phone])


def print_human(file):
    with open(file, "rb") as f:
        humans = pickle.load(f)
        for human in humans:
            print(human)


if __name__ == "__main__":
    create_human(10)
    print_human("human.data")
