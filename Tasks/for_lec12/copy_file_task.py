import os


def copyfile(source, destination):
    with open(source, 'r') as src:
        with open(destination, 'x') as dst:
            dst.writelines(src.readlines())


if __name__ == '__main__':
    copyfile('source.txt', 'destination.txt')
