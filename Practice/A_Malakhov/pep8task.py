import sys
import os
#import os должен стоять в начале, только после него можно ввести import sys
import hashlib
import ast
import argparse
from time import *


class shuffler:
#Возможно нужно нижнее подчеркивание после class (class_shuffle)???

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []

    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
            #нужна пустая строка(PEP8 Определения методов внутри класса разделяются одной пустой строкой)
    for path, mp3 in mp3s:
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3), path + '/' + hashname))
        # 2 лишние закрывающие скобки (SyntaxError: invalid syntax)
        f = open(output, 'r')
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []

    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append({root, file})
            # нужна пустая строка(PEP8 Определения методов внутри класса разделяются одной пустой строкой)
    for path, hashname in mp3s:
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        #снова лишняя закрывающая скобка (SyntaxError: invalid syntax)
        os.remove(restore_path)

    def generateName(self, seed=time()):
    #нет пробелов вокруг оператора сравнения "="
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
        if args.output:
            Shuffler.rename(args.dirname, 'restore.info')
        else:
            Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
#необхима пустая строка в конце файла