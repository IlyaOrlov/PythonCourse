
# import os.path


def copyfile(a, b):
    # if os.path.isfile(a):
    try:
        fo = open(a)
        f = fo.read()
        print('Original content:', f)
        fod = open(b, 'w')
        fnew = fod.write(f)
        print('Done copying')
        fo.close()
        fod.close()
    except FileNotFoundError:
        print('This file is not found')

if __name__ == "__main__":
    a = "myfile.txt" # source file
    b = "myfile1.txt" # destination.file
    copyfile(a, b)
