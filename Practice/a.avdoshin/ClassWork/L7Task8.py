# 22.11 - [ИО]:  Проверено (есть замечания) - пока 4 балла из 5.
import os

from L7Task7 import copyFile


def copydir(source, distanation):
    if os.path.isdir(distanation):
        # 22.11 - [ИО]:  где же исключение?
        pass  # raise FileExistsError
    os.mkdir(distanation)
    for file in os.listdir(source):
        # 22.11 - [ИО]:  для платформенно-независмой
        # конкатенации путей надо использовать os.path.join
        if os.path.isfile(source + '/' + file):
            copyFile(source + '/' + file, distanation + '/' + file)
        else:
            os.mkdir(distanation + '/' + file)


copydir('testDir', 'testDircopy')
