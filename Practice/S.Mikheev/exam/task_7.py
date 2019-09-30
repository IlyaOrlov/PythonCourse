def copyfile(source, destination):
    try:
        f = open(source, 'r')
    except FileNotFoundError:  # Ошибка если файл не найден
        return "File doesn't exist."
    except Exception as exc:
        return "Some unexpected error: {}".format(type(exc).__name__)
    else:
        try:
            with open(destination, 'w') as w:
                w.write(f.read())
        except PermissionError:  # Ошибка недостаточно прав для записи
            return "Editing is not available."
        except Exception as exc:
            return "Some unexpected error: {}".format(type(exc).__name__)
        else:
            return "Запись выполнена"
        finally:
            f.close()


print(copyfile('test.txt', 'test2.txt'))
