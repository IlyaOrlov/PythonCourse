def numbers():
    """Выводит большое число из двух."""
    a = input("Первое число: ")
    b = input("Второе число: ")
    if a > b:
        return a
    else:
        return b


number = numbers()
print("Большее: " + str(number))

number_2 = numbers()
print("Большее: " + str(number_2))
