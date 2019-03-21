import math

class MyRange:

    def __init__(self, first, second = None, step = 1):

        if isinstance(first, int):                                  #Данная проверка не работает. При передаче в кач-ве
            self.first = first                                      #параметра экземпляру класса MyRange например буквы a
        else:                                                       #Python воспринимает её как переменную и выдаёт ошибку
            raise NameError("Values of range must be an integer")   #NameError, которая почему то не перехватывается рэйзом


        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

        if step != 0:
            self.step = step
        else:
            raise ValueError("Step can't be a zero")

        self.lenght = math.ceil((self.end - self.start) / self.step)

    def __len__(self):
        return self.lenght

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError("Myrange index out of range")


d = MyRange(200, 0, -5)


for i in d:
    print(i)