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
          mp3s = [] #� ������ 2 ������ �������
          
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) #2 ������ ������, ������ � ������
          f = open(output, 'r') #�� ������� ���� ��������
          f.write(str(self.map)) #�� ������� ���� ��������
          
    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: #� ������ 2 ������ �������
            self.map = ast.literal_eval(f.read()) #�� ������� ���� ��������
          mp3s = [] #� ������ 2 ������ �������
          
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3': #�� ������� ������ �������
                    mp3s.append({root, file}) #���� ������ ������
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) #������ ������ ������
        os.remove(restore_path) #�� ������� 4 ��������
                        
     def generateName(self, seed=time()): #���� ������ ������
          return hashlib.md5(str(seed)).hexdigest() #���� ������ ������
       

#������ ������� ������
def parse_arguments(): #��� ��������
    parser = argparse.ArgumentParser() #������ ��������� �� 4 �������
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help') #������ ��������� �� 4 �������
    rename_parser = subparsers.add_parser('rename', help='rename help') #������ ��������� �� 4 �������
    rename_parser.add_argument('dirname') #������ ��������� �� 4 �������
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored') #����� ������ ������ 79 �������� � ������ ��������� �� 4 �������
    restore_parser = subparsers.add_parser('restore', help="command_a help") #������ ��������� �� 4 �������
    restore_parser.add_argument('dirname') #������ ��������� �� 4 �������
    restore_parser.add_argument('restore_map') #������ ��������� �� 4 �������
    args = parser.parse_args() #������ ��������� �� 4 �������
    return args #������ ��������� �� 4 �������

def main(): #��� �������� � ��� ������ ���� ��������� �� 4 �������
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:
          #��� ������ �������
                Shuffler.rename(args.dirname, 'restore.info')
                #��� ������ �������
          else:
          #��� ������ �������
                Shuffler.rename(args.dirname, args.output)
                #��� ������ �������
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


#������ ������� ������
main()