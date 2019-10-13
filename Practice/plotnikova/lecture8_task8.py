import os


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

def copydir(old_dir, new_dir):
    if not os.path.isdir(old_dir):
        return "Директория {} не найдена.".format(old_dir)
    for root, directories, files in os.walk(old_dir):
        [os.makedirs(os.path.join(new_dir, root, c)) for c in directories if not os.path.exists( os.path.join(new_dir, root, c))]
        [copyfile(os.path.join(root, c), os.path.join(new_dir, root, c)) for c in files]
    return "Директория {} успешно скопирована в директорию {}".format(old_dir, new_dir)

old_dir="old_dir"
new_dir="new_dir"
print(copydir(old_dir, new_dir))
