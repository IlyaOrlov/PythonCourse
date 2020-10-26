"""
№1: поиск работает быстрее в хешируемых коллекциях(dict, set), а перебор в list, tuple потому-что их элементы
расположены последовательно в памяти

№2 Разницы нет
"""

# №3:
class SelfCounter:
    counter = 0

    def __init__(self, name):
        self.name = name
        SelfCounter.counter += 1

    @classmethod
    def how_much(cls):
        return cls.counter

# №4
def do_dict(keys, values):
    res = {}
    for i, key in enumerate(keys):
        if i < len(values):
            res[key] = values[i]
        else:
            res[key] = None
    return res


if __name__ == "__main__":
    a = SelfCounter("a")
    b = SelfCounter('b')
    c = SelfCounter('c')
    print(SelfCounter.how_much())

    print(do_dict(['a', 'b', 'c'], [1, 2]))
    print(do_dict(['a', 'b', 'c'], [1, 2, 3, 4]))
