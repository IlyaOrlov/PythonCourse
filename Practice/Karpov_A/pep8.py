import sys
import os
import hashlib
import ast
import argparse
from fileinput import filename
from time import *


class shuffler:                                         			# class Shufler

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):								# заменить на dir_name
          mp3s = []                                     			# более 4 пробелов, сдвинуть на 2 пробела назад
        for root, directories, files in os.walk(dirname):   		# заменить на dir_name
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'					# заменить на hash_name
            self.map[hashname] = mp3								# заменить на hash_name
            os.rename(path + '/' + mp3), path + '/' + hashname))	# удалить скобки в средине и в конце, и заменить на hash_name
          f = open(output, 'r')                         			# удалить 2 пробела
          f.write(str(self.map))									# удалить на 2 пробела

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:							# удалить 2 пробела. Импорт filename, добавляется from fileinput import filename
            self.map = ast.literal_eval(f.read())					
          mp3s = []													# добавить на 2 пробела		  
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:									# заменить на hash_name
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))	# удалить одну скобку в конце и заменить на hash_name
        os.remove(restore_path)										# добавить на 4 пробела
                
     def generateName(self, seed=time()):
          return hashlib.md5(str(seed)).hexdigest()					# удалить 2 пробела


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
    Shuffler = shuffler()															# заменить на shuffler = Shuffler()
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')						# заменить на shuffler.rename(args.dirname, 'restore.info')
          else:
                Shuffler.rename(args.dirname, args.output)							# заменить на shuffler.rename(args.dirname, 'restore.info')
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)							# заменить на shuffler.rename(args.dirname, 'restore.info')
    else:
        sys.exit()


main()