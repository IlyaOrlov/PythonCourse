a=input('Веведите пятизначное число: ')

if a.isdigit()==True and len(str(a))==5:
    for x in a:
        print(x)
else:
    a = input('Веведите пятизначное число: ')
    if a.isdigit()==True and len(str(a))==5:
        for x in a:
            print(x)