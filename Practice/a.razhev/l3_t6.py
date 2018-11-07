#  -*- coding: utf-8 -*-
# 08.11 - [ИО]:  Проверено (ОК).
matr=[[1, 2, 3, 4, 5, 6],
     [2, 4, 5, 1, 7, 100],
     [3, 100, 4, 2, 1, 6],
     [5, 3, 2, 1, 7, 6],
     [2, 4, 6, 100, 3,1]]

len_matr=len(matr)
#print len_matr
len_str=len(matr[0])
#print len_str
for i in range(0, len_matr):
    print matr[i]
bad_elem=100
print''
bad_id=[]
for i in range(0, len_matr):
    for j in range(0, len_str):
        #print matr[i][j]
        if matr[i][j]==bad_elem:
            bad_id.append(j)
#print bad_id
len_bad=len(bad_id)
for i in range(0, len_matr):
    for j in range(len_str-1, -1, -1):
        for k in range(0, len_bad):
            if j==bad_id[k]:
                matr[i].pop(j)

#len_str=len_str-1
len_str=len(matr[0])
for i in range(0, len_matr):
    print matr[i]       
