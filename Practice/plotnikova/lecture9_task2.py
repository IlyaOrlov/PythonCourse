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
        print(self.res)

if __name__ == '__main__':
    th1 = MyThread(1, 2)
    th2 = MyThread("string1", "string2")
    th3 = MyThread(["1", "2"], ["3","4","5"])
    th4 = MyThread(["1", "2"], "string2")

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()


