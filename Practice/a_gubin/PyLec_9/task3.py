import threading


class ThreadWithPrivateData(threading.Thread):
    def __init__(self, func, private_data):
        super().__init__()
        self.__data = private_data
        self._func = func

    def run(self):
        self._func(threading.current_thread().name, self.__data)


def print_thread_data(name, data):
    print(f"The thread's name is '{name}', its private data: {data}")


def main():
    threads = []
    for i in range(5):
        thread = ThreadWithPrivateData(print_thread_data, f"data #{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
