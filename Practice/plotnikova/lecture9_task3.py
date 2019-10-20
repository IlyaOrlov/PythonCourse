import threading


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.var = None

    def get_name_thread(self):
        self.var=threading.current_thread().name
        return self.var

    def run(self):
        self.get_name_thread()


if __name__ == '__main__':
    for i in range(3):
        th = MyThread()
        th.start()
        print(th.var)
