from datetime import datetime
from random import randint


class TimeForWith:
    def __enter__(self):
        self.start_time = datetime.now()
    def __exit__(self, exc_type, exc_val, exc_tb,):
        self.all_time = datetime.now()-self.start_time
        print("Code execution time: {}".format(self.all_time.total_seconds()))

#Create selection sort
def select_sort (arr):
    i = 0
    while i<len(arr)-1:
        j = i+1
        pos = j
        while j<len(arr)-1:
            if (arr[j+1]<arr[pos]):
                pos = j+1
            j+=1
        if (arr[pos]<arr[i]):
            arr[i],arr[pos] = arr[pos], arr[i]
        i+=1
    return arr

#Create list with 10000 random element
array = []
for i in range(10000):
    array.append(randint(0,20))


#Timed sorting
with TimeForWith():
    select_sort(array)

#Print to the screen
print(array)