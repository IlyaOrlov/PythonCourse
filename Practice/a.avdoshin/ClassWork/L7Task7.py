import os


def copyFile(source, distanation):
    if os.path.isfile(distanation):
        raise FileExistsError
    origin = open(source, 'rb')
    copy = open(distanation, 'wb')
    copy.write(origin.read())

if __name__ == '__main__':
    copyFile('TestFile.txt', 'copyTest')
