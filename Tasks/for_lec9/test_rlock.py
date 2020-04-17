import threading
import time

start = time.time()

q = []
mymutex = threading.RLock()

def worker():
    with open('outfile.txt', 'w') as fout:
        item = '0'
        while item.isdigit():
            with mymutex:
                fout.write("start\n")
                while len(q) > 0:
                    item = q.pop(0)
                    if item.isdigit():
                        fout.write("{}, ".format(int(item)**2))
                    else:
                        break
                fout.write("finish\n")

t = threading.Thread(target=worker)
t.start()
with open('infile.txt') as fin:
    for line in fin:
        items = line.split()
        for each in items:
            with mymutex:
                if each.isdigit():
                    q.append(each)
    with mymutex:
        q.append('stop')

t.join()

print("Total time: {}".format(time.time() - start))