def numbers():
    """Выводит большое число из двух."""
    a = input("Первое число: ")
    b = input("Второе число: ")
    if a > b:
        print(str(a) + " большее из двух.")
    else:
        print(str(b) + " большее из двух.")


numbers()
