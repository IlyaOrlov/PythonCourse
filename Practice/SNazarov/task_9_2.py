from multiprocessing import Process, Queue


def sum_data(new_data, q):
    result = {'int': 0, 'str': '', 'list': []}

    for i in new_data:
        if type(i) is int:
            result['int'] += i

        elif type(i) is str:
            if i != ' ':
                result['str'] += i
            else:
                result['str'] += ' '.join(i)

        elif type(i) is list:
            result['list'] += i

    for k, v in result.items():
        if v != 0 and v != [] and v != '':
            q.put((k, v))


if __name__ == '__main__':
    type_data = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 ['H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', '?'], [[25], [25], [50]]]
    lst_pro = []
    res = []
    q = Queue()
    for i in type_data:
        proc = Process(target=sum_data, args=(i, q))
        proc.start()
        lst_pro.append(proc)

    for proc in lst_pro:
        proc.join()

    for j in range(q.qsize()):
        res.append(q.get())

    print(res)
