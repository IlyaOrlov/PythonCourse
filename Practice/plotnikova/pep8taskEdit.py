import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []#лишние 2 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))#лишние 2 скобки ) поле mp3 и после hashname
          f = open(output, 'r')#необходимо добавть 2 пробела
          f.write(str(self.map))#необходимо добавть 2 пробела

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:#лишние 2 пробела
            self.map = ast.literal_eval(f.read())
          mp3s = []#лишние 2 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':#необходимо добавть 1 пробел
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))#лишние 1 скобк )
        os.remove(restore_path)#пустая сттрока (ниже) содержит пробелы
                
     def generateName(self, seed=time()):#лишний пробел
         return hashlib.md5(str(seed)).hexdigest()#лишний пробел


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')#длина строки >79
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')#длина строки >79
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():#Выше должно быть 2 пустые строки для отделения класса от функции
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:#лишний пробел
                Shuffler.rename(args.dirname, 'restore.info')#лишний пробел
          else:#лишний пробел
                Shuffler.rename(args.dirname, args.output)#лишний пробел
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
