# Импорт из сторонней библиотеки должен идти вторым.
import sys
# Импорт из стандартной библиотеки должен идти первым.
import os
import hashlib
import ast
import argparse
from time import *


# Имя класса не в CapWords.
class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
# 2 лишних отступа.
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
# Не хватает 1 открывающей и 1 лишняя закрывющая скобка
            os.rename(path + '/' + mp3), path + '/' + hashname))
# Не хватает 2 отступов.          
          f = open(output, 'r')
# Не хватает 2 отступов.    
          f.write(str(self.map))

    def restore(self, dirname, restore_path):
# 2 лишних отступа.        
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
# Не хватает 2 отступов.            
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
# Не хватает 1 отступа.                
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
# Лишняя закрывающая скобка.            
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
# Не хватает 4 отступов.      
        os.remove(restore_path)
    
# 1 лишний отступ.     
     def generateName(self, seed=time()):
# 2 лишних отступа.         
          return hashlib.md5(str(seed)).hexdigest()
# Методы внутри класса разделяются одной строкой.


# Не хватает 4 отступов для всего абзаца.
def parse_arguments():
    parser = argparse.ArgumentParser()
# Превышена допустимая длина строки, требуется перенос.    
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
# Превышена допустимая длина строки, требуется перенос.    
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

# Не хватает 4 отступа для 4 следующих строк.
def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
# Не хватает 2 отступа.        
          if args.output:   
                Shuffler.rename(args.dirname, 'restore.info')
# Не хватает 2 отступа.    
          else:       
                Shuffler.rename(args.dirname, args.output)
# Не хватает 4 отступа для 4 следующих строк.            
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()
# 2 лишние пустые строки.


# Не хватает 4 отступа.
main()