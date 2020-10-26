import multiprocessing


def sum(args):
    int_val, str_val, list_val = args
    list_val.append(str_val + str(int_val))
    return list_val


def main():
    sets = [(1, "one", ["set1"]),
            (2, "two", ["set2"]),
            (3, "three", ["set3"]),
            (4, "four", ["set4"]),
            (5, "five", ["set5"])]

    with multiprocessing.Pool(5) as pool:
        res = pool.map(sum, sets)

    print(res)


if __name__ == '__main__':
    main()