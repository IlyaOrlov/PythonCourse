import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:  # имя класса с большой буквы должно быть

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []  # два лишних пробела сделано
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'  #  name с маленькой буквы должен быть
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))  # лишняя скобка в конце и одной не хватает в начале
          f = open(output, 'r')  # два лишних пробела
          f.write(str(self.map))  # два лишних пробела

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: # два лишних пробела
            self.map = ast.literal_eval(f.read())
          mp3s = []  # два лишних пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':  # не хватает одного пробела
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))  # лишняя скобка
        os.remove(restore_path)
                
     def generateName(self, seed=time()):  # один пробел лишний
          return hashlib.md5(str(seed)).hexdigest()  # два пробела лишних


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

def main():  # не хватает еще одной строки как отступа
    args = parse_arguments()
    Shuffler = shuffler()  # переменная наоборот с маленькой буквы, а класс с большой должен быть
    if args.subcommand == 'rename':
          if args.output:  # два пробела лишних
                Shuffler.rename(args.dirname, 'restore.info')  # 4 лишних пробела здесь, название должно быть с маленькой буквы
          else:  # два пробела лишних
                Shuffler.rename(args.dirname, args.output)  # 4 лишних пробела здесь, название должно быть с маленькой буквы
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)  # название должно быть с маленькой буквы
    else:
        sys.exit()


main()
