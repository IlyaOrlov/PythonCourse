import time  #импортируем библиотеку time

class TimeBreaker:  #определяем класс
    def __enter__(self):  #определяем функцию входа в МК
        self.start = time.time()  #определяем переменную класса замеряющую стартовое время

    def __exit__(self, exc_type, exc_val, exc_tb):  #определяем функцию выхода из МК
        self.stop = time.time() - self.start  #рассчет времени выполнения
        print("Operation time = {}".format(self.stop))  #вывод искомого значения

with TimeBreaker():
    i = 10000000
    while i > 0:
        i -= 1
