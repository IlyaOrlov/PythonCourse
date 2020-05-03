import random
import pickle

class Human():
    def __init__(self, first_name, last_name, age, hair_color, p_of_residence):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color
        self.p_of_residence = p_of_residence
    def __str__(self):
        return f"Human: first_name={self.first_name}, last_name={self.last_name}, age={self.age}, hair_color={self.hair_color}," \
               f" p_of_residence={self.p_of_residence}"

def fun(num):
    f_name = ['Denis', 'Ksenia', 'Alex', 'Ivan', 'Ilya']
    l_name = ['Moirov', 'Shoikhet', 'Vasin', 'Riviera', 'Pupkin']
    p_of_r = ['Moscow', 'Nizhny Novgorod', 'Rybinsk', 'St. Petersburg', 'California']
    hair_color = ['Green', 'Red', 'Blue', 'Gray', 'Black']
    people = []
    for i in range(num):
        people.append(Human(random.choice(f_name), random.choice(l_name), random.randint(1, 115), random.choice(hair_color), random.choice(p_of_r)))
    for i in people:
        print(i)
    with open('data.pickle', 'wb') as f:
        pickle.dump(people, f)
    return people

def fun2(file):
    with open(file, 'rb') as f:
        data_new = pickle.load(f)
    for line in data_new:
        print(line)
    return data_new


fun(5)
fun2('data.pickle')





