import random
import time


class Man:

    def __init__(self, name_of_man):
        self.name = name_of_man

    @staticmethod     # because we don't use attributes of the class
    def solve_talk():
        print("I'm not ready yet")


class Pupil(Man):

    def __init__(self, name_of_pupil):
        super().__init__(name_of_pupil)

    @staticmethod
    def solve_talk():
        print("I think...")
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")


if __name__ == "__main__":
    pupil = Pupil("Pupil")
    print(f"{pupil.name}:", end=" ")
    pupil.solve_talk()
