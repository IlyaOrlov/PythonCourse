import pickle
import random


first_name_list = ['John', 'Stuart', 'Scott', 'Jeff', 'Lou', 'David', 'Oliver']
last_name_list = ['Smith', 'Jones', 'Brown', 'Taylor', 'Wilson', 'Evans', 'Walker']
occupation_list = ['surgeon', 'software developer', 'psychiatrist', 'dentist',
                   'manager', 'statistician', 'database administrator']
residence_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
                  'Philadelphia', 'San Antonio']


class Human:
    def __init__(self, first_name, last_name, age, occupation, residence):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.residence = residence

    def __str__(self):
        return f'{self.first_name} {self.last_name} is a {self.age} y.o. ' \
               f'{self.occupation} from {self.residence}'


def create_serialize_save(number):
    human_list = []
    for _ in range(number):
        human_list.append(Human(random.choice(first_name_list),
                                random.choice(last_name_list),
                                random.randint(18, 60),
                                random.choice(occupation_list),
                                random.choice(residence_list)))
    with open('human.data', 'wb') as f:
        pickle.dump(human_list, f)


def deserialize_print(file):
    with open(file, 'rb') as f:
        print(*pickle.load(f), sep='\n')


create_serialize_save(20)
deserialize_print('human.data')
