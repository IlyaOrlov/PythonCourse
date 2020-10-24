def check_equal(item1, item2):
    if type(item1) != type(item2) or (type(item1) != type(list()) and type(item1) != type(tuple())):
        return False
    if item1 is item2:
        return True
    if len(item1) != len(item2):
        return False
    for elem1, elem2 in zip(item1, item2):
        if elem1 != elem2:
            return False
    return True
