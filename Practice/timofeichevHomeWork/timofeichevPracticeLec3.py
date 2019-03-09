a = input("Введите что хотите:")
while a !="exit":
    if a.isdigit():
        print(int(a) ** 2)
        break
    else:
        print("Ошибка,введите еще раз:")
        a = input("Введите что хотите:")
else:
    print("Завершение работы программы")