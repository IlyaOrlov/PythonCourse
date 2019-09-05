import sys                                                         # вероятно порячдок импорта
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:                                                    # Имя класса должно быть с большой буквы

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []                                                # отступ 4 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'                # маленькая буква N
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))   # две лишних скобки
          f = open(output, 'r')                                    
          f.write(str(self.map))                                   

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:                           # отступы
            self.map = ast.literal_eval(f.read())                  # отступы
          mp3s = []                                                # отступы
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':                             # отступы
                    mp3s.append({root, file})                      # отступы
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))   # скобка
        os.remove(restore_path)
                
     def generateName(self, seed=time()):                          # отступы и маленькая буква N, и вероятно метод стат.
          return hashlib.md5(str(seed)).hexdigest()                # отступы


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

def main():                                                        # отступ в две строки
    args = parse_arguments()
    Shuffler = shuffler()                                          # Поменять местами названия переменной и класса
    if args.subcommand == 'rename':
          if args.output:                                          # отступы
                Shuffler.rename(args.dirname, 'restore.info')      # отступы, название
          else:                                                    # отступы
                Shuffler.rename(args.dirname, args.output)         # отступы, название
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)           # название
    else:
        sys.exit()


main()
