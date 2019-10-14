def copyfile(source, destination):
    # Считывание файла
    try:
        with open(source, 'rt') as f:
           text= f.read()
    except FileNotFoundError:
        return [-1, "Ошибка чтения файла {}.".format(source)]
    except Exception  as e:
        return [-1, "Ошибка чтения файла {}.".format(source)]

    # Запись  файла
    try:
        with open(destination, 'x') as f:
            f.write(text)
    except FileExistsError:
        return [-1, "Ошибка записи файла {}.".format(destination)]
    except Exception  as e:
        return [-2, "Ошибка записи файла {}.".format(destination)]
    return [0, 'Файл {} скопирован успешно в {}'.format(source, destination)]

if __name__ == '__main__':
    source="1.txt"
    destination="2.txt"
    print(copyfile(source, destination))