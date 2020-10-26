#2
from multiprocessing import Pool
import time

def my_sum(lst):
    if len(lst)==0:
        return lst
    tmp = lst[:]
    for i in range(len(tmp)-1):
        tmp[i+1] = tmp[i]+tmp[i+1]
    return tmp[len(tmp)-1]

def common_sum(args):
    ints=[]
    strs=[]
    lists=[]

    for arg in args:
        if isinstance(arg, int):
            ints.append(arg)
        elif isinstance(arg, str):
            strs.append(arg)
        elif isinstance(arg, list):
            lists.append(arg)

    return (my_sum(ints), my_sum(strs), my_sum(lists))

def multi_sum(lst):
    pool = Pool(processes=len(lst))
    return pool.map(common_sum, lst)

if __name__ == '__main__':
    lst = [(0,'H',1,[1,2],'e',[3,4,5]),
           ('l', 1,[6,7,8,9],'l',1,[10]),
           (1,[11,12],'o',2)]
    print(multi_sum(lst))





