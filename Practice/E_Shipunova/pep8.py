import sys
import os
import hashlib
import ast
import argparse
from time import *  # this is not the best import option, we don't know what exactly is being imported
                    # "from time import time"  or  "import time" and use with name's library


class shuffler:     # have to be "class Shuffler"

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):  # have to be "dir_name"
        mp3s = []
        # line № 18-25 move right 4 spaces, because rename() has it
    for root, directories, files in os.walk(dirname): # have to be "dir_name"
        for file in files:
            if file[-3:] == '.mp3': # have to be "if file[-4:]", because '.mp3'.len()=4
                mp3s.append([root, file])  # after this line add empty line
    for path, mp3 in mp3s:
        hashname = self.generateName() + '.mp3' # have to be "hash_name"
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3), path + '/' + hashname)) # after this line add empty line and delete ')' ')'

        f = open(output, 'r')  # may be 'a' for f.write()
        f.write(str(self.map)) # we can not write , because 'r' - only reading.

    def restore(self, dirname, restore_path):  # have to be "dir_name"
        with open(filename, '+') as f:         # have to be "file_name"
            self.map = ast.literal_eval(f.read())
        mp3s = []
        # line № 35-41 move right 4 spaces, because restore() has it
    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3': # have to be "if file[-4:]", because '.mp3'.len()=4
                mp3s.append({root, file})  # after this line add empty line
    for path, hashname in mp3s:
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))  # delete ')'
        os.remove(restore_path)

    def generateName(self, seed=time()): # have to be "generate_name"
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help') # have to be "sub_command"
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')                                         # have to be "dir_name"
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')                                        # have to be "dir_name"
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    Shuffler = shuffler()  # have to be "shuffler=Shuffler()" and use the object
    if args.subcommand == 'rename':
        if args.output:
            Shuffler.rename(args.dirname, 'restore.info') # use "shuffler.rename(args.dir_name, 'restore_info')"
        else:
            Shuffler.rename(args.dirname, args.output)   # use "shuffler. ..." and add empty line after this line
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map) # use "shuffler. ..."
    else:
        sys.exit()


main() # after this line add empty line