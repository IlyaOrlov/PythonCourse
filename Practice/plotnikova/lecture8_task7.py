def copyfile(source, destination):
    # Считывание файла
    try:
        with open(source, 'rt') as f:
           text= f.read()
    except FileNotFoundError:
        return print ("Файл {} не найден".format(source))
    except Exception  as e:
        return print("Ошибка чтения: {}".format(e))
    # Запись  файла
    try:
        with open(destination, 'x') as f:
            f.write(text)
    except FileExistsError:
        return print ("Файл {} уже существует.".format(destination))
    except Exception  as e:
        return print("Ошибка записи: {}".format(e))
    return print("Файл {} успешно записан".format(destination) )

source="1.txt"
destination="2.txt"
copyfile(source, destination)