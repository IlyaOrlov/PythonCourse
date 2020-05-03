
def copyfile(source, destination):

    try:
        with open(source, 'r') as f1:
            with open(destination, 'x') as f2:
                f2.write(f1.read())
    except FileNotFoundError:
        print('файл не существует')
    except FileExistsError:
        print('Файл существует')



source = 'test2.txt'
destination = 'test1.txt'
copyfile(source, destination)