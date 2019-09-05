import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:# класс должен быть с большой буквы

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []# лишний отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'# Name с большой буквы
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))# лишние скобки
          f = open(output, 'r')# лишние пробелы
          f.write(str(self.map))# лишние пробелы

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:# лишний отступ
            self.map = ast.literal_eval(f.read())
          mp3s = []# # лишний отступ
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':# не хватает пробелов
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))# лишняя скобка
        os.remove(restore_path)# не хватает пробелов
                
     def generateName(self, seed=time()):# лишний пробел
          return hashlib.md5(str(seed)).hexdigest()# лишние пробелы


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
    Shuffler = shuffler()# локальная переменная с маленькой буквы, класс с большой
    if args.subcommand == 'rename':
          if args.output:# лишние пробелы
                Shuffler.rename(args.dirname, 'restore.info')# лишние пробелы
          else:# лишние пробелы
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
