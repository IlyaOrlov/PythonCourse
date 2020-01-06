def removeCol(list, num):
    for it in list:
        it.pop(num)

def findElem(list, elem):
    for it in list:
        for it2 in it:
            if(it2 == elem):
                removeCol(list, it.index(it2))


def printTable(list):
    for it in list:
         print(it)

mylist = [[3,4,5,2,1,6],[3,2,15,5,2,5],[7,3123,32,5,8,0],[3,4,5,2,3,5],[9,0,5,3,2,3]]
printTable(mylist);
findElem(mylist, 0)
printTable(mylist)