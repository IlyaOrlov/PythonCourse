import socket
import random
import pickle
from Lection_7_Task_3 import Human


def make_human(quantity):
    first_name = ['Batman', 'Spider-man', 'Daredevil', 'Hulk', 'Superman', 'Starlord', 'Wonder Woman', 'Iron Fist']
    second_name = ['Brus Wayne', 'Peter Parker', 'Matt Murdok', 'Brus Banner', 'Clark Kent', 'Peter Quill', 'Diana',
                   'Danny']
    age = [33, 25, 31, 40, 36, 29, 1126, 22]
    was_born = ['Gotham', 'New York', 'Hell Kitchen', 'USA', 'Krypton', 'Texas', 'Temeskira', 'Chinatown']
    city = ['London', 'Dzerginsk', 'Los Angeles', 'Monreal', 'Stambul', 'Rome', 'Paris']
    pet = ['cat', 'dog', 'spider', 'bird']
    name_pet = ['Bill', 'Ted', 'Robin', 'Ben', 'Marta', 'Doctor Doom']
    human = []
    for i in range(quantity):
        human.append(
            Human(random.choice(first_name), random.choice(second_name), random.choice(age), random.choice(was_born),
                  random.choice(city), random.choice(pet), random.choice(name_pet)))
    return human



host = '127.0.0.1'
port = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send(pickle.dumps(make_human(1)))
print(f'{client.recv(1024).decode()}')

client.close()
