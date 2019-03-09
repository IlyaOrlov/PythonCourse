import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler: # Имя класса должно начинаться с заглавной буквы-"Shuffler"

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []                         # отступ превышает 4 пробела

    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
    for path, mp3 in mp3s:
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3), path + '/' + hashname)) #нужно добавить 1 скобку в начало и убрать 1 скобку в конце
      f = open(output, 'r')                 # данная строка должна быть выровнена с предыдущей по вертикали
      f.write(str(self.map))

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:    # отступ превышает 4 пробела
            self.map = ast.literal_eval(f.read())
          mp3s = []           # отступ превышает 4 пробела

    for root, directories, files in os.walk(dirname):
        for file in files:
           if file[-3:] == '.mp3':          # не соблюден отступ в 4 пробела
                mp3s.append({root, file})
    for path, hashname in mp3s:
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))  # последняя скобка лишняя
        os.remove(restore_path)

     def generateName(self, seed=time()):   # должно быть generate_name и отступ превышает 4 пробела
          return hashlib.md5(str(seed)).hexdigest()  # отступ превышает 4 пробела


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored') # длина данной строки больше 79 символов.
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:   # отступ превышает 4 пробела
                Shuffler.rename(args.dirname, 'restore.info')  # отступ превышает 4 пробела
          else:             # отступ превышает 4 пробела
                Shuffler.rename(args.dirname, args.output)     # отступ превышает 4 пробела
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
