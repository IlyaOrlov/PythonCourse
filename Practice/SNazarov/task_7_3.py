import random
import pickle


class Human:

    def __init__(self, first_name, last_name, age, auto, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.auto = auto
        self.profession = profession

    def __getstate__(self):
        return self.__dict__


def write_human(number):
    arr = []
    f_name = ['Andrey', 'Sergey', 'Roma', 'Yura', 'Oleg', 'Dmitriy', 'Ilya']
    l_name = ['Ivanov', 'Petrov', 'Sidorov', 'Kotov', 'Gorin', 'Socolov', 'Delov']
    auto = ['BMW', 'Audi', 'Nissan', 'Mercedes', 'Honda', 'Toyota', 'Lexus']
    profession = ['engineer', 'pilot', 'farmer', 'lawyer', 'businessman', 'actor', 'waiter']

    for i in range(number):
        first, last, car, prof, = random.choice(f_name), random.choice(l_name), \
                                  random.choice(auto), random.choice(profession)
        arr.append(Human(first, last, random.randint(18, 55), car, prof))
        f_name.remove(first)
        l_name.remove(last)
        auto.remove(car)
        profession.remove(prof)

    with open("human.data", "wb") as f:
        pickle.dump(arr, f)


def open_human():
    with open("human.data", "rb") as f:
        data = pickle.load(f)
        for read in data:
            print(f'This is {read.first_name} {read.last_name}, he is {read.age} years old. '
                  f'He has a {read.auto} car and his profession is a {read.profession}.')


if __name__ == '__main__':
    write_human(7)
    open_human()
