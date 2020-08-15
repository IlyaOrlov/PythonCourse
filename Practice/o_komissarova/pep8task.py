import sys
import os
import hashlib
import ast
import argparse
from time import *
from fileinput import filename

# Изменить имя класса на Shuffler
class shuffler:

    def __init__(self):
        self.map = {}

    # Изменить dirname на dir_name
    def rename(self, dirname, output):
        # Сдвинуть на два пробела влево
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            # изменить hashname на hash_name
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            # удалить две закрывающие скобки
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r')
          f.write(str(self.map))

    # изменить dirname на dir_name
    def restore(self, dirname, restore_path):
        # добавить from fileinput import filename
        # сдвинуть на два пробела влево
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
          mp3s = []
        # изменить dirname на dir_name
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        # изменить hashname на hash_name
        for path, hashname in mp3s:
            # убрать закрывающую скобку
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
    # Изменить generateName на generate_name
    # Сдвинуть на один пробел влево
     def generateName(self, seed=time()):
          return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    # изменить dirname на dir_name
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    # изменить dirname на dir_name
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    # изменить на shuffler = Shuffler()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        # сдвинуть на два пробела влево
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()

