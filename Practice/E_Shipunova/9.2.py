import re
from multiprocessing import Process


def add_any_args(*args):
    dic_type = {"int": 0, "str": "", "list": []}  # for initialize res

    for i in range(len(args)-1):                  # check for all arg to match the same type
        if type(args[i]) is not type(args[i+1]):
            return "Incorrect data!"

    if (type(args[0]) is int) or (type(args[0]) is str) or (type(args[0]) is list):    # type inference by the first arg
        res = dic_type[re.search("'(\w{3,5})'>$", str(type(args[0]))).group(1)]        # initialize res

        for i in range(len(args)):
            res += args[i]
        print(res)
        return res

    return "Incorrect data!"


if __name__ == "__main__":
    # for testing add_any_args()
    #print(add_any_args(1, 2, 3, 4, 5))
    #print(add_any_args("1, ", "2, ", "3, ", "4, ", "5"))
    #print(add_any_args([1, 2, 3], [4], [5, 6, 7]))
    #print(add_any_args(1, "error"))
    #print(add_any_args({"1": 1}, {"2": 2}))

    arguments = [[1, 2, 3, 4, 5], ["1, ", "2, ", "3, ", "4, ", "5"], [[1, 2, 3], [4], [5, 6, 7]]]
    processes = []
    for i in range(3):
        p = Process(target=add_any_args, args=(arguments[i]))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
