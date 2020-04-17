import os


# Задание 7
def copyfile(source, destination):
    with open(source, 'r') as f1:
        with open(destination, 'x') as f2:
            for line in f1:
                f2.write(line)


source = 'test.txt'
destination = 'test2.txt'
copyfile(source, destination)
# исключение, destination уже создан
# copyfile(source, destination)

# исключение, source не существует
# source = 'bla_bla.txt'
# destination = 'bla_bla2.txt'
# copyfile(source, destination)

# Задание 8
path_to_source = r'C:\Users\днс\Desktop\test'
paht_to_destination = r'C:\Users\днс\\Desktop\test(dublicate)'


def copydir(paht_to_source, paht_to_destination):
    os.mkdir(paht_to_destination)
    for root, subfoldars, files in os.walk(paht_to_source):
        for folder in subfoldars:
            path_to_copyfolder = paht_to_destination + '\\' + folder + '\\'
            os.mkdir(path_to_copyfolder)

        for file in files:
            path_to_file = os.path.join(root, file)
            path_to_copyfile = paht_to_destination + path_to_file[len(paht_to_source):]
            copyfile(path_to_file, path_to_copyfile)


copydir(path_to_source, paht_to_destination)