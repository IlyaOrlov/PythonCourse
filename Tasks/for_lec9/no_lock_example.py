# Два потока запрашивают и выводят координаты точки на плоскости
from threading import Thread
import time


class Base:
    x = 0
    y = 0


def print_fun():
    i = 0
    while i < 2:
        Base.x = input("2x: ")
        Base.y = input("2y: ")
        print(f'Thread 2: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    t = Thread(target=print_fun)
    t.start()
    i = 0
    while i < 2:
        Base.x = input("1x: ")
        Base.y = input("1y: ")
        print(f'Thread 1: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(1)
    t.join()
