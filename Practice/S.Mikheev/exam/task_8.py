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


def copydir(folders, tree):
    for current_dir, dirs, files in os.walk(folders):
        for dir in dirs:
            link = os.path.join(tree, current_dir, dir)
            if not os.path.exists(link):
                os.makedirs(link)
        for file in files:
            link = os.path.join(current_dir, file)
            link_new = os.path.join(tree, current_dir, file)
            print(copyfile(link, link_new))


copydir('test', 'test2')
