import threading


class PrivateThread(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self._data = data

    def run(self):
        print(f"Thread's name: {threading.current_thread().name}, data: {self._data}")


threads = [PrivateThread("abc"), PrivateThread(5), PrivateThread([1, 2, 3, 4])]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
