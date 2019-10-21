import threading


class MyThread(threading.Thread):
    list_name=[]

    def __init__(self):
        threading.Thread.__init__(self)

    def get_name_thread(self):
        MyThread.list_name.append(threading.current_thread().name)

    def run(self):
        self.get_name_thread()


if __name__ == '__main__':
    for i in range(3):
        th = MyThread()
        th.start()

    for p in threading.enumerate():
        if p is threading.main_thread():
            continue
        p.join()

    print(MyThread.list_name)