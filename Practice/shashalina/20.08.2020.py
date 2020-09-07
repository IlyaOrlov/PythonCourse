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
import numpy

def matrix(m):
    mt = m.transpose()
    print(mt)

matrix(numpy.array([[1, 2, 3], [4, 5, 6]]))