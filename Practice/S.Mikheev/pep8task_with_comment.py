import sys
import os
import hashlib
import ast
import argparse
from time import * #так делать не рекомендуется, может быть конфликт имен


class shuffler: #Имена классов должны обычно следовать соглашению CapWords

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []


    for root, directories, files in os.walk(dirname): #пропущен отступ для всего цикла
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
    for path, mp3 in mp3s: #пропущен отступ для всего цикла
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3), path + '/' + hashname)) #лишние закрывающие скобки
        f = open(output, 'r') #файл открыт для чтения, нужно поставить w или +
        f.write(str(self.map)) #попытка записи в файл, открытый для чтения. Нужно закрыть файл после записи в него (f.close())

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []

    for root, directories, files in os.walk(dirname): #пропущен отступ для всего цикла
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append({root, file})
    for path, hashname in mp3s: #пропущен отступ для всего цикла
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) #лишняя закрывающая скобка
        os.remove(restore_path)

    def generateName(self, seed=time()): #имя функции должно быть написано маленькими буквами
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help') #Строка длиннее 79 символов
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored') #Строка длиннее 79 символов
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    Shuffler = shuffler() #Имя функции должно быть написано с маленькой буквы, а имя класса - с большой
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