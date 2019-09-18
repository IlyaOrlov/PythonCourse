def fun():
    i=1
    while i<=100:
        print((i % 15 == 0 and "FizzBuzz") or
             (i % 5 == 0 and "Buzz") or
              (i % 3 == 0 and "Fizz") or i)
        i+=1


def fun1():
    i=1
    while i<=100:
        text = ""
        if i % 3 == 0:
            text="Fizz"
        if i % 5 == 0:
            text = text+"Buzz"
        if len(text)==0:
            text=str(i)
        print(text)
        i+=1


fun()
fun1()



