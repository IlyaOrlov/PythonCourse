import threading


class MyThread(threading.Thread):
    def __init__(self, a,b):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
        self.res=None

    def run(self):
        thread = threading.current_thread().getName()
        if type(self.a)!=type(self.b):
            self.res= "{}: Операция не выполнена - типы данных не совпадают: {} и {}".format(thread, self.a, self.b)
        else:
            self.res= "{}:Результат: {}". format(thread, self.a+self.b)

if __name__ == '__main__':
    arg=[
                [1, 2],
                ["string1", "string2"],
                [["1", "2"], ["3","4","5"]],
                [["1", "2"], "string2"]
        ]
    for i in range(4):
        th = MyThread(arg[i][0],arg[i][1])
        th.start()
        print(th.res)

