import threading


def addition(*args):
    if type(args[0]) is int:
        a = 0
    if type(args[0]) is str:
        a = ""
    if type(args[0]) is list:
        a = []
    for arg in args:
        a += arg
    return print(a)


integers = 2, 7, 3, 9, 4
strings = "The ", "people ", "on ", "subways ", "and ", "trains"
lists = ["Monday", "Tuesday", "Wednesday", "Thursday"], ["Friday", "Saturday", "Sunday"]

threads = []
for data in integers, strings, lists:
    thr = threading.Thread(target=addition, args=data)
    thr.start()
    threads.append(thr)
for thr in threads:
    thr.join()
