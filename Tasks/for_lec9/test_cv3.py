import threading
import time

start = time.time()

q = []
cv = threading.Condition()
busy = False

def worker():
    global busy
    with open('outfile.txt', 'w') as fout:
        item = '0'
        while item.isdigit():
            with cv:
                cv.wait_for(lambda: len(q) != 0)
                fout.write("start\n")
                busy = True
                while len(q) > 0:
                    item = q.pop(0)
                    if item.isdigit():
                        fout.write("{}, ".format(int(item)**2))
                    else:
                        break
                busy = False
                cv.notify()
                fout.write("finish\n")

t = threading.Thread(target=worker)
t.start()

with open('infile.txt') as fin:
    for line in fin:
        items = line.split()
        for each in items:
            with cv:
                cv.wait_for(lambda: busy == False)
                if each.isdigit():
                    q.append(each)
                    cv.notify()
    with cv:
        cv.wait_for(lambda: busy == False)
        q.append('stop')
        cv.notify()

t.join()

print("Total time: {}".format(time.time() - start))