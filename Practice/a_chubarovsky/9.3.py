import threading as thrd


def get_info(some_data):
    thread_name = thrd.current_thread().name
    print(f"{thread_name} contains data about turbine {some_data[0]}:\nPower: {some_data[1]} MW, "
          f"Steam pressure: {some_data[2]} MPa, Feed water temperature: {some_data[3]} °C")


if __name__ == '__main__':
    K_210 = ('K-210', 210, 12.8, 242)
    K_300 = ('K-300', 300, 23.5, 275)
    K_500 = ('K-500', 525, 23.5, 276)
    K_800 = ('K-800', 800, 23.5, 274)
    threads = [thrd.Thread(target=get_info, args=(K_210,)), thrd.Thread(target=get_info, args=(K_300,)),
               thrd.Thread(target=get_info, args=(K_500,)), thrd.Thread(target=get_info, args=(K_800,))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
