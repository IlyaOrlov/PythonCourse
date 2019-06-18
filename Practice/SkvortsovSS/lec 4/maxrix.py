def matrix(a):
    for i in a:
        print(i)
    print("enter number for 1 to 9")
    t = int(input())
    
    c = []
    b = []
    i=0
    while i < len(a[0]):
        j=0    
        while j < len(a):
            c.append(a[j][i])
            j+=1
        i+=1
        if not t in c:
            b.append(c)
        c=[]
    
    a=[]
    i=0
    while i < len(b[0]):
        j=0    
        while j < len(b):
            c.append(b[j][i])
            j+=1
        i+=1
        a.append(c)
        c=[]
    for i in a:
        print(i)
    
   
matrix ([[1, 2, 3], [4, 5, 5], [7, 8, 9], [0, 4, 5]])  