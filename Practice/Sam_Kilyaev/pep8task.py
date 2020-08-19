import sys
import os
import hashlib
import ast
import argparse
from time import *   #Лучше использовать import time, или from time import конкретная функция


#class shuffler:  Нужно использовать CapWords
class Shuffler

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          #mp3s = []  Отступы
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
           #os.rename(path + '/' + mp3), path + '/' + hashname))   Лишняя скобка в середине
            os.rename(path + '/' + mp3, path + '/' + hashname))
          #f = open(output, 'r')   Лишние отступы
          #f.write(str(self.map))
        f = open(output, 'r')
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:  #Разные отступы в with, исправленный вариант
            self.map = ast.literal_eval(f.read())
            mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s: #Разные отступы в цикле, исправленный вариант
            #os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) Лишняя скобка
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
            os.remove(restore_path)
                
     def generateName(self, seed=time()):
          #return hashlib.md5(str(seed)).hexdigest() Лишние отступы
         return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    #Везде одинарные кавычки, а в строке ниже двойные, не ошибка, но лучше использовать один тип везде
    #restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser = subparsers.add_parser('restore', help='command_a help')
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler() #Название класса с маленькой буквы
    Shuffler = Shuffler()
    if args.subcommand == 'rename':
        if args.output: #Лишние отступы в if/else, исправленный вариант
            Shuffler.rename(args.dirname, 'restore.info') #
        else:
            Shuffler.rename(args.dirname, args.output)  #
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
