import shelve, subprocess
from random import randint


class Human:
    def __init__(self, first_name, last_name, age, employed, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employed = employed
        self.phone_number = phone_number

    @property
    def full_name(self):
        return self.first_name + self.last_name

    def __str__(self):
        return f"Human (name: {self.first_name} {self.last_name}," \
               f" age: {self.age}," \
               f" employed: {self.employed}," \
               f" phone number: {self.phone_number})"


def save_data(data, file_name='human.data'):
    with shelve.open(file_name) as db:
        for human in data:
            db[human.full_name] = human


def load_data(file_name="human.data"):
    res = []
    with shelve.open(file_name) as db:
        for key in db:
            res.append(db[key])
    return res


if __name__ == "__main__":
    names = [("Ivan", "Ivanov"), ("Petr", "Petrov"), ("Boris", "Borisov"), ("Aleksey", "Alekseev"), ("Andrey", "Andreev")]
    humans = []
    file_name = "human.data"
    for i in range(len(names)):
        humans.append(Human(*names[i], randint(18, 100), bool(randint(0, 2)), randint(100000, 999999)))
    print(*humans, sep='\n')
    print("*" * 40)
    save_data(humans, file_name)
    # res = subprocess.run(["cat", file_name], text=True, capture_output=True)
    # res = subprocess.run(["cat", file_name], capture_output=True)
    # print(res.stdout.splitlines())
    # print('*' * 40)
    print(*load_data(file_name), sep='\n')
