# 20.08.2020
# Найти все команды git в тексте https://github.com/IlyaOrlov/PythonCourse/tree/master/Practice используя модуль re

import re
import requests

def find():
    response = requests.get('https://github.com/IlyaOrlov/PythonCourse/tree/master/Practice')
    text = response.text
    print (text)

    matches = re.findall(r'git [a-z]* ', text)
    for ex in matches:
        if ex:
            print("git: {}".format(ex))
        else:
            print("No match!")

find()

# Транспонировать матрицу

def transpose(matr):
        newMatr = []
        for i in range(len(matr[0])):
             newMatr.append([0] * len(matr))
        for row in range(len(matr)):
                for column in range(len(matr[row])):
                        newMatr[column][row] = matr[row][column]
        return newMatr

# [print(list(x)) for x in zip(*matr)]

print(transpose([[1, 2, 3], [4, 5, 6]]))
