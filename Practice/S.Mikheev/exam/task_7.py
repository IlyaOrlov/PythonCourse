import os


def copyfile(source, destination):
    try:
        f = open(source, 'r')
    except FileNotFoundError:  # Ошибка если файл не найден
        return "File doesn't exist."
    except Exception as exc:
        return "Some unexpected error: {}".format(type(exc).__name__)
    else:
        try:
            w = open(destination, 'w')
        except PermissionError:  # Ошибка недостаточно прав для записи
            return "Editing is not available."
        except Exception as exc:
            return "Some unexpected error: {}".format(type(exc).__name__)
        else:
            w.write(f.read())
            return "Запись выполнена"


print(copyfile('test.txt', 'test2.txt'))
