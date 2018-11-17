import os

from L7Task7 import copyFile


def copydir(source, distanation):
    if os.path.isdir(distanation):
        pass  # raise FileExistsError
    os.mkdir(distanation)
    for file in os.listdir(source):
        if os.path.isfile(source + '/' + file):
            copyFile(source + '/' + file, distanation + '/' + file)
        else:
            os.mkdir(distanation + '/' + file)


copydir('testDir', 'testDircopy')
