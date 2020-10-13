import multiprocessing

def sum_mixer(*args):
    for i in range(len(args)):
        if not isinstance(args[i], type(args[0])):
            raise TypeError
    if isinstance(args[0], list):
        new_list = []
        for i in range(len(args)):
            new_list += args[i]
            print(len(new_list))
        return new_list
    elif isinstance(args[0], int):
        print(sum(args))
        return sum(args)
    elif isinstance(args[0], str):
        new_str = ""
        for i in range(len(args)):
            new_str += args[i]
            print(str(new_str))
        return new_str
    else:
        return 1


if __name__ == "__main__":

    processes = [multiprocessing.Process(target=sum_mixer, args=([0, 2, 9])),
                 multiprocessing.Process(target=sum_mixer, args=(1, 0, 00, 2, 1)),
                 multiprocessing.Process(target=sum_mixer, args=("py", "th", "on"))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
