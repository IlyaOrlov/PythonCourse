import sys
import os
import hashlib
import ast
import argparse
from time import *

# имя класса рекомендуется писать с заглавной буквы
class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        # два лишних пробела
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
        # лишняя скобка после mp3 и после hashname
            os.rename(path + '/' + mp3), path + '/' + hashname))

        # два лишних пробела
          f = open(output, 'r')
        # два лишних пробела
          f.write(str(self.map))

    def restore(self, dirname, restore_path):
        # два лишних пробела
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
        # два лишних пробела
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
        # не хватает пробела
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
        # лишняя закрывающая скобка
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
        
    # лишний пробел            
     def generateName(self, seed=time()):
        # два лишних пробела
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
    # имя переменной рекомендуется писать с маленькой буквы
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        # два лишних пробела
          if args.output:
        # 4 лишних пробела
                Shuffler.rename(args.dirname, 'restore.info')
        # два лишних пробела
          else:
        # 4 лишних пробела
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()

main()