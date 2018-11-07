#  -*- coding: utf-8 -*-
# 08.11 - [ИО]:  Проверено (есть небольшие замечания).
arr=[5, 3, 24, 2, 0, -3, 7, 3]
print arr
# 08.11 - [ИО]:  Можете везде использовать len(arr),
# необходимости в дополнительной переменной l нет.
l=len(arr)
#print l
j=0
for j in range (0, l-1):
    min=arr[j]
    for i in range(j+1, l):
        if arr[i]<min:
            min=arr[i]
            m_id=i
            #print min, m_id
    # 08.11 - [ИО]:  В одной строке несколько операторов лучше
    # не писать: такой стиль не соответствует pep8.
    if min!=arr[j]: arr[m_id]=arr[j]; arr[j]=min
print arr
