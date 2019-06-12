import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler:  # имя класса сделал с заглавной буквы

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3,
                      path + '/' + hashname)  # снес параметры в скобках
            # на строку ниже
            # привел метод 'os.rename' к виду:
            # os.rename(src, dst), где:
            # src − This is the actual name of the file or directory.
            # dst − This is the new name of the file or directory.
        f = open(output, 'r')  # вынул из цикла
        f.write(str(self.map))  # вынул из цикла

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:  # убрал 2 пробела
            self.map = ast.literal_eval(f.read())
        mp3s = []  # убрал 2 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3': # добавил 1 пробел
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
            # убрал ')' в конце предыдущей строки
        os.remove(restore_path)

    def generate_name(self, seed=time()):  # изменил имя с 'generateName'
        # на 'generate_name'
        return hashlib.md5(str(seed)).hexdigest()  # убрал 1 пробел


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand',
                                       help='subcommand help')  # разбил
    # длинную строку на 2
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output',
                               help='path to a file where '
                                    'restore map is stored')   # разбил
    # длинную строку на 3
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():  # добавил пустую строку перед main
    args = parse_arguments()
    Shuffler_new = Shuffler()  # имя экземпляра класса изменил с Shuffler
    # на Shuffler_new
    # shuffler() изменил на Shuffler()
    if args.subcommand == 'rename':
        if args.output:  # убрал 2 пробела
            Shuffler_new.rename(args.dirname, 'restore.info')  # убрал 4
            # пробела
            # Shuffler.rename изменил на Shuffler_new.rename
        else:  # убрал 2 пробела
            Shuffler_new.rename(args.dirname, args.output)  # убрал 4 пробела
            # Shuffler.rename изменил на Shuffler_new.rename
    elif args.subcommand == 'restore':
        Shuffler_new.restore(args.dirname, args.restore_map)  # Shuffler.restore
        # изменил на Shuffler_new.restore
    else:
        sys.exit()


main()  # добавил пустую строку (ниже) в конец файла
