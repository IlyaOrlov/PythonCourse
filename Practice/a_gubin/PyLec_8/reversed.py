def reversed(list_):
    list_ = list_[::-1]
    return list_


if __name__ == "__main__":
    my_list = [x for x in range(10)]
    print(reversed(my_list))

