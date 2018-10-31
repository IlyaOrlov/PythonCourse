arr=[5, 3, 24, 2, 0, -3, 7, 3]
print arr
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
    if min!=arr[j]: arr[m_id]=arr[j]; arr[j]=min
print arr
