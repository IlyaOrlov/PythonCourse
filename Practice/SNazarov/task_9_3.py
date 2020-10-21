import threading


def thread_private(new_car, new_data):
    new_data.p = new_car
    print(f'thread name is {threading.current_thread().name}, and his car is {new_data.p[0]}, model {new_data.p[1]}'
          f' this car has {new_data.p[2]} horsepower.')


if __name__ == '__main__':
    my_data = threading.local()
    thread_lst = []
    cars = [['BMW', 'M-5', '625'], ['AUDI', 'RS-6', '605'], ['TOYOTA', 'SUPRA', '324']]

    for car in cars:
        thr = threading.Thread(target=thread_private, args=(car, my_data))
        thr.start()
        thread_lst.append(thr)

    for thr in thread_lst:
        thr.join()
