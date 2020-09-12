import threading


class PrivateData:
    def __init__(self, data):
        self.__data = str(data)

    def get_data(self):
        return self.__data


def print_private_data(*args):
    str = ""
    for i in range(len(args)):
        str += args[i]
    print(f"Thread's name: {threading.current_thread().name}, data: {str}")


data1 = PrivateData("data1")
data2 = PrivateData(5)
data3 = PrivateData([1, 2, 3])

threads = [threading.Thread(target=print_private_data, args=data1.get_data()),
           threading.Thread(target=print_private_data, args=data2.get_data()),
           threading.Thread(target=print_private_data, args=data3.get_data())]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
