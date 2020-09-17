import sys
import os
import hashlib
import ast
import argparse
from time import * # лучше импортировать конкретные функции или использовать import time


class shuffler: # изменить имя класса на Shuffler

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output): # изменить dirname на dir_name
          mp3s = [] # лишние два пробела в начале строки
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3' # изменить hashname на hash_name
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))  # удалить лишние закрывающие скобки в середине и в конце
          f = open(output, 'r') # лишние два пробела в начале строки
          f.write(str(self.map)) # лишние два пробела в начале строки

    def restore(self, dirname, restore_path): # изменить dirname на dir_name
          with open(filename, '+') as f: # лишние два пробела в начале строки
            self.map = ast.literal_eval(f.read()) 
          mp3s = [] # добавить два пробела в начале строки
        for root, directories, files in os.walk(dirname): # изменить dirname на dir_name
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s: # изменить hashname на hash_name
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # удалить лишнюю закрывающую скобку
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # Изменить generateName на generate_name и удалить лишний пробел в начале строки
          return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname') # изменить dirname на dir_name
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help") # лучше использовать везде  один тип ковычек "" или ''
    restore_parser.add_argument('dirname') # изменить dirname на dir_name
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler() # изменить на shuffler = Shuffler()
    if args.subcommand == 'rename':
          if args.output: # лишние два пробела в начале строки
                Shuffler.rename(args.dirname, 'restore.info') # лишние четыре пробела в начале строки
          else: # лишние два пробела в начале строки
                Shuffler.rename(args.dirname, args.output) # лишние четыре два пробела в начале строки
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
