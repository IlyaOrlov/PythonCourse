import sys
import os
import hashlib
import ast
import argparse
from fileinput import filename
from time import *


class Shuffler:  # class shuffler меняем на class Shuffler

    def __init__(self):
        self.map = {}

    def rename(self, dir_name, output):  # dirname поменять dir_name
        mp3s = []  # сдвинуть на 2 пробела назад

    for root, directories, files in os.walk(dir_name):  # dirname на dir_name
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
    for path, mp3 in mp3s:
        hash_name = self.generateName() + '.mp3'  # hashname на hash_name
        self.map[hash_name] = mp3  # hashname на hash_name
        os.rename(path + '/' + mp3, path + '/' + hash_name)  # удалил скобки в средине и в конце, и заменить hashname на hash_name
    f = open(output, 'r')  # удалить пробелы
    f.write(str(self.map))  # удалить пробелы

    def restore(self, dir_name, restore_path): # dirname поменять dir_name
        with open(filename, '+') as f:  # удалить 2 пробела. Импорт filename, добавляется from fileinput import filename
            self.map = ast.literal_eval(f.read())
            mp3s = []  # добавить на пробелы

    for root, directories, files in os.walk(dir_name):  # dirname поменять dir_name
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append({root, file})
    for path, hash_name in mp3s:  # hashname на hash_name
        os.rename(path + '/' + hash_name, path + '/' + self.map[hash_name]))  # удалить одну скобку в конце и заменить на hash_name
        os.remove(restore_path)  # добавить пробелы
    def generate_name(self, seed=time()): # generateName менять на generate_name
        return hashlib.md5(str(seed)).hexdigest()  # удалить пробелы


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dir_name') # dirname поменять dir_name
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dir_name')  # dirname поменять dir_name
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    shuffler = Shuffler()  # замена на shuffler = Shuffler()
    if args.subcommand == 'rename':
        if args.output:
            shuffler.rename(args.dir_name, 'restore.info')
        else:
            shuffler.rename(args.dir_name, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dir_name, args.restore_map)
    else:
        sys.exit()


main()