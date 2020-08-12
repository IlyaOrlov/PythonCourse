import os               # порядок импорты стандартной библиотеки \ сторонних библиотек \ импорты модулей текущего проекта
import sys              # пробелы между группами импорта

import hashlib
import ast
import argparse

from fileinput import filename
from time import *
                        # 2 строки между блоком import и началом блока кода

class Shuffler:         # имена классов вида CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []                                      # выравнивание-отступы
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3, path + '/' + hashname)       # два лишних закрывающих пробела в строке
        f = open(output, 'r')                           # выравнивание-отступы
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:                  # использование filename без импорта
            self.map = ast.literal_eval(f.read())
        mp3s = []                                       # выравнивание-отступы
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])     # лишняя скобка
            os.remove(restore_path)

    def generate_name(self, seed=time()):                # выравнивание-отступы и отсутствует ':'
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    shuffler = Shuffler()               # имя экемпляра класса с маленькой а имя класса с заглавной
    if args.subcommand == 'rename':
          if args.output:
                shuffler.rename(args.dirname, 'restore.info')
          else:
                shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
