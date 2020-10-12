# 1
def fizzBuzz():
    print("".join(str(el)+" " for el in ["FizzBuzz" if (x % 3 == 0 and x % 5 == 0)
                                                    else ("Fizz" if (x % 3 == 0)
                                                    else ("Buzz" if (x % 5 == 0)
                                                    else x)) for x in range(1, 101)]))

# 2
def numberToDigits(num: int):
    print(*list(str(num)), sep = "\n")



# 3
def sort(arr):
    for i in range(0, len(arr) - 1):
        lst = arr[i::]
        x = lst.index(min(lst))
        lst[0], lst[x] = lst[x], lst[0] #почему не работает lst[0], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[0]
        arr[i::] = lst
    return arr

# 4
def tabToSpace(fileDirection: str, switcher: int):
    d = {"    " : "\t"}
    f = open(fileDirection, "r")
    lst = []
    for line in f:
        for k, v in d.items():
            if switcher is 1:
                line = line.replace(k, v)
            elif switcher is 2:
                line = line.replace(v, k)
            lst.append(line)
    f = open(fileDirection, "w")
    f.write("".join(lst))
    f.close()

#5
def templates(line: str, templates: dict):
    for k, v in templates.items():
        line = line.replace(k, v)
    return line



fizzBuzz()
numberToDigits(10819)
print(sort([0, 3, 24, 2, 3, 7]))
tabToSpace("./test.txt", 1)
print(templates("qwe asd zxc", {"q":"Q", "w": "W", "e": "E"}))
