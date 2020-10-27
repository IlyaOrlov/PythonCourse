import threading


def sum_different(*args):
    for i in range(len(args)):
        if not isinstance(args[i], type(args[0])):
            raise TypeError
    if isinstance(args[0], list):
        new_list = []
        for i in range(len(args)):
            new_list += args[i]
        return new_list
    elif isinstance(args[0], int):
        return sum(args)
    elif isinstance(args[0], str):
        new_str = ""
        for i in range(len(args)):
            new_str += args[i]
        return new_str
    else:
        raise TypeError


threads = [threading.Thread(target=sum_different, args=([1, 2, 3], [4, 5, 6])),
           threading.Thread(target=sum_different, args=(1, 2, 3, 4, 5, 6)),
           threading.Thread(target=sum_different, args=("a", "b", "c"))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
