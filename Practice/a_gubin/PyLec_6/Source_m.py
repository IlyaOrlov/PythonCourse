def multiplier(m=1, source=(1, 2, 3)):
    result = []
    for item in source:
        result.append(item * m)
    return result


if __name__ == "__main__":
    print(multiplier(2, range(6)))
