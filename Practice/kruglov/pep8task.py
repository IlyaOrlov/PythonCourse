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
        # Vertical alignment required
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            # The variable name matches the system
            hashname = self.generateName() + '.mp3'
            # The variable name matches the system
            self.map[hashname] = mp3
            # Two extra brackets
            # The variable name matches the system
            os.rename(path + '/' + mp3), path + '/' + hashname))
          # Vertical alignment required
          f = open(output, 'r')
          # Vertical alignment required
          f.write(str(self.map))

    def restore(self, dirname, restore_path):
          # Vertical alignment required
          # An undeclared variable is used, maybe the name of the variable is dirname
          with open(filename, '+') as f:
            # Vertical alignment required
            self.map = ast.literal_eval(f.read())
          # Vertical alignment required
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               # Vertical alignment required
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        # The variable name matches the system
        for path, hashname in mp3s:
            # The variable name matches the system
            # One extra brackets
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
                
     def generateName(self, seed=time()):
          # Vertical alignment required
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
    # Variable should be lowercase and the class name with a capital letter
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          # Vertical alignment required
          if args.output:
                # Vertical alignment required
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                # Vertical alignment required
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
