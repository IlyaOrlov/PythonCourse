#1
def chargen():
    #while True: #unwanted loop, endless repeat
        for c in "0123456789":
            yield c

words = [c + c for c in chargen()][:10]

#right function:
def chargen():
    for c in "0123456789":
        yield c

words = [c + c for c in chargen()][:10]

#2
def multiplier(m = 1, source = [1,2,3]):
    result = source #result is a reference to the [1,2,3]
    for i, x in enumerate(source):
        result[i] *= m
    return result

#right function
def multiplier(m = 1, source = [1,2,3]):
    result = source[:] #now result is a shallow-copy of the source
    for i, x in enumerate(source):
        result[i] *= m
    return result

#or
def multiplier(m = 1, source = [1,2,3]):
    return [x * m for x in source]

#3
import time
class MyContextManager(object):
    def __enter__(self):
        self.timer = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timer = time.time() - self.timer
        print('{0}{1}'.format(round(self.timer, 3), " seconds"))

with MyContextManager():
    time.sleep(3)


