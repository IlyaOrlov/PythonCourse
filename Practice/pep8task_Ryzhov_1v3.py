import sys
import os
import hashlib
import ast
import argparse
from time import *


"""
Operations 'open' and 'write' in definiton of 'rename' function improved.
"""


class shuffler:  # ClassName with Capital letter

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []  # 4 spaces per indentation level
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
        f = open(output, 'a')  # 4+4 spaces per indentation level\
            # 'a' instead of 'r' for appending
        f.write(str(self.map))  # 4+4 spaces per indentation level

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:  # 4 spaces per indentation level
            self.map = ast.literal_eval(f.read())
        mp3s = []  # 4 spaces per indentation level
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':  # 4 spaces per indentation level
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
                
    def generateName(self, seed=time()):  # 4 spaces per indentation level
        return hashlib.md5(str(seed)).hexdigest()  # 4 spaces per indentation level


def parse_arguments():  # There one type of PEP*_Error: \
    # TLL = too long line (>79 letters)
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', \  # TLL
                                       help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', \  # TLL
                         help='path to a file where restore map is stored')
    # 'help' is not aligned with '(' on previous line to exclude TLL \
    # due to Zen rule 9: 'Although practicality beats purity'
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        if args.output:  # 4 spaces per indentation level
            Shuffler.rename(args.dirname, 'restore.info')  # 4 spaces per indentation level
        else:  # 4 spaces per indentation level (inheritance from line 66)
            Shuffler.rename(args.dirname, args.output)  # 4 spaces per indentation level (inheritance from line 66)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()