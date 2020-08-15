class Man:

    def __init__(self, name_of_man):
        self.name = name_of_man

    @staticmethod     # because we don't use attributes of the class
    def solve_talk():
        print("I'm not ready yet")


if __name__ == "__main__":
    man = Man("Isaak")
    print(f"{man.name}:", end=" ")
    man.solve_talk()
