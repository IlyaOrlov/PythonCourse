import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler: # имена классов с большой буквы

    def __init__(self):
        self.map = {} 

    def rename(self, dirname, output):
          mp3s = [] # нет отступа от функции rename
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) # лишняя скобка
          f = open(output, 'r') # нет отступа от функции rename
          f.write(str(self.map)) # нет отступа от функции rename

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
          mp3s = [] # нет отступа от функции with
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # лишняя скобка
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # лишний отступ от shuffler
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
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output: # лишние пробелы
                Shuffler.rename(args.dirname, 'restore.info') # лишние пробелы
          else: # лишние пробелы
                Shuffler.rename(args.dirname, args.output) # лишние пробелы
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
