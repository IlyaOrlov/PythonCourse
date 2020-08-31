import pickle


class Human:

   def __init__(self, first_name, last_name, age, position, phone):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.position = position
       self.phone = phone

   def __iter__(self):
       return iter(self)


def print_human():
    i = 0
    with open("human.data", "rb") as f:
        humans = pickle.load(f)
        for human in humans:
            i += 1
            print(f"{i} human is: ")
            print(human.first_name, human.last_name)
            print(f"He is {human.age} years old. He is a {human.position}. Phone: {human.phone}\n")


if __name__ == "__main__":
    print_human()
