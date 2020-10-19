# Отсутствие значения и пустота в python отличаются
# None - это пустое место, оно равно только самому себе


def is_none(thing):
    if thing is None:
        print(thing, " It's None")
    elif thing:
        print(thing, " It's True")
    else:
        print(thing, " It's False")


is_none(None)
is_none(False)
is_none(True)
is_none(0)
is_none(0.0)
is_none('')  # строка string
is_none([])  # список list
is_none(()) # кортеж tuple
is_none({})  # словарь dictionary
is_none(set()) # множество set
