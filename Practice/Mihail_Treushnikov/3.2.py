a = 10894

def number (a):
    List = []
    while a>0:
        List.append(a%10)
        a = int (a/10)
    List.reverse()
    for i in List:
        print("Элемент {} \n".format(i))
number(a)
