from subprocess import Popen,PIPE

def readfile (path_file,name_file):
    proc = Popen(['cat',f'{path_file}/{name_file}'],stdout=PIPE,stderr=PIPE)
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1])
    print(res[0].decode())

readfile("/Users/mihailtreushnikov/Desktop/NIIT/Python/Lec7","file.txt")