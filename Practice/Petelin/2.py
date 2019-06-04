def f1():
    lst = []
    for x in range(1,101):
        t=""
        if x%3==0 :
            t+="Fizz"
        if x%5==0:
            t+="Buzz"
        if not (x%3==0 or x%5==0 ):
            t=x
        lst.append(t)
    print(lst)

f1()

def f2():
  n=input('введите число: ')
  t=tuple(n)
  k=0
  for i in t:
     k+=1
     print('{} цифра равна {}'.format(k,i))

f2()


def f3():
    arr = [0,3,24,2,3,7]
    i=0
    while i< len(arr):
         arr2=arr[i:]
         x=min(arr2)
         j=arr.index(x,i)
         t=arr[i]
         arr[i]=arr[j]
         arr[j]=t
         i+=1
         #print(arr)
    print(arr)
f3()


def f4_1(str):
    newStr=str.expandtabs(4)
    return newStr

def f4_2(str):
    newStr=str.replace("    ","\t")
    return newStr

str = "asdf\t\tasdf\tas"
print(str)
str2=f4_1(str)
print(str2)
print(f4_2(str2))
str3="шесть      пробелов"
print(f4_2(str3))

def f5(str):
    d= {"a":"A", "b":"B", "s":"S"}
    for key in iter(d):
        str=str.replace(key,d[key] )
    return str

str="a i b sideli na trube"
print(str)
print( f5(str) )


def T(arr):
    tCol=[]
    tRow=[]
    i=0
    if len(arr)==0:#"нулевая матрица"
        return []
    while i<len(arr[0]):
        j=0
        while j< len(arr):
            tCol.append(arr[j][i])
            j+= 1
        tRow.append(tCol.copy())
        tCol.clear()
        i += 1
    return tRow

def f6(arr, num):
    i=0
    while i<len(arr):
        if num in arr[i]:
            del arr[i]
            i-=1
        i+=1
    return arr

num = 12
arr= [[11,12,13],[21,22,23],[12,32,33],[41,42,12]]
for s in arr:
    print(s)
arr2=T(f6(T(arr),num))
for s in arr2:
    print(s)
print(arr2)
