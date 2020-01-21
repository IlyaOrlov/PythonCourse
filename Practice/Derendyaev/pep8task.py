import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = [] #вставлены лишние 2 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r') #вставлен лишний пробел
          f.write(str(self.map)) #вставлен лишний пробел

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: #вставлены лишние 2 пробела
            self.map = ast.literal_eval(f.read())
          mp3s = [] #вставлены лишние 2 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file}) #вставлен лишний пробел
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
                
     def generateName(self, seed=time()): #вставлен лишний пробел
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
          if args.output: #вставлен лишний пробел
                Shuffler.rename(args.dirname, 'restore.info') #вставлены лишние 2 пробела
          else:
                Shuffler.rename(args.dirname, args.output) #вставлен лишний пробел
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
