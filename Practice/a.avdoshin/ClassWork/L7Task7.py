# 22.11 - [ИО]:  Проверено (есть замечания) - 0 баллов.
import os


def copyFile(source, distanation):
    if os.path.isfile(distanation):
        raise FileExistsError
    # 22.11 - [ИО]:  работать с файлами без менеджера контекста неправильно,
    # а не закрывать их после работы вообще преступление)
    origin = open(source, 'rb')
    copy = open(distanation, 'wb')
    copy.write(origin.read())

if __name__ == '__main__':
    copyFile('TestFile.txt', 'copyTest')
