#ЛЕКЦИЯ СЕМЬ
#task one
import datetime as dating

def calculate_working_days(start, end):

    if start > end:
         return "Uncorrect date"
    else:
     total = ((end - start).days)+ 1
     days = (int(total / 7))
     summary = days * 5

    for key in range(days * 7 , total):
        holyday = (start + dating.timedelta(key)).weekday()
        if holyday!= 5 and holyday != 6:
            summary = summary + 1
    return summary

date_01 =dating.date(2015,4,11)
date_02 = dating.date(2020,4,11)
print(f'Количество дней  = {calculate_working_days(date_01,date_02)}')
date_02 =dating.date(2015,4,11)
date_01 = dating.date(2020,4,11)
print(calculate_working_days(date_01,date_02))

#Task two
import subprocess

def reading_file(name):
    process = subprocess.Popen(['type', name], shell=True)
    process.wait()
    res = process.communicate()
    if process.returncode:
        return res
reading_file('test.txt')
print(" ")

#Task three
import pickle
import random


class Human:
    def __init__(self, first_name, surname, age, place,work):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.place = place
        self.work = work

    def __str__(self):
     str  = f'first_name = {self.first_name} , surname = {self.surname}, age = {self.age} , place = {self.place}, work = {self.work}'
     return str


def create_people(ammount):
    first_names = ['Alexander', 'Ivan', 'Kirill', 'Mikhail', 'Vasya']
    surname = ['Makarov', 'Bobrov', 'Svetlov', 'Ivanov', 'Klimov']
    place = ['Moscow', 'Nizhy_Novgorod', 'Kazan', 'New_York', 'Paris']
    work = ['developer', 'plumber', 'surgery', 'manager', 'tester']
    list= []
    if ammount > 0:
        for key in range(ammount):
            list.append(Human(random.choice(first_names),
                              random.choice(surname),
                              random.randint(18, 50),
                              random.choice(place),
                              random.choice(work)))
        with open('human.data', 'wb') as readings:
            j = 0
            while j < ammount:
                pickle.dump(list[j], readings, protocol=pickle.HIGHEST_PROTOCOL)
                j += 1
    elif ammount <= 0:
        print("Количество должно быть больше нуля")

    return list


def printing_list(file, buffer):
    with open(file, 'rb+') as files:
        for key in buffer:
            people_list = pickle.load(files)
            print(f'{people_list}')


if __name__ == '__main__':
    arr = create_people(5)
    printing_list('human.data', arr)
    arr = create_people(0)
    printing_list('human.data',arr)
