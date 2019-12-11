import sys
import os
import hashlib
import ast
import argparse

from time import *

# Class names must begin with a capital letter
class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        # Two extra spaces
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            # Two extra brackets, first-after'mp3', second-after'hashname'
            os.rename(path + '/' + mp3), path + '/' + hashname))
          # Two extra spaces
          f = open(output, 'r')
          # Two extra spaces
          f.write(str(self.map))

    def restore(self, dirname, restore_path):
          # Two extra spaces
          # An undeclared variable is used-'filename', maybe the name of the variable is 'dirname'
          with open(filename, '+') as f:
            # Two extra spaces
            self.map = ast.literal_eval(f.read())
          # Two extra spaces
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               # Two extra spaces
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            # One extra brackets, after '[hashname])'
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
                
     def generateName(self, seed=time()):
          # Two extra spaces
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
    # Variable 'Shuffler' should be lowercase and
    # the class name 'shuffler()' with a capital letter
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          # Two extra spaces
          if args.output:
                # Two extra spaces
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                # Two extra spaces
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
