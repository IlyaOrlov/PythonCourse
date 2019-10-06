# Написать реализацию функции format


def my_format(* args):
    res = args[0]
    count=res.count("{}")
    for idx, val in enumerate(args):
        if idx!=0:
            if count==0:
                print(res.count("{" + str(idx - 1) + "}"))
                if res.count("{" + str(idx - 1) + "}") > 0:
                    res = res.replace("{" + str(idx - 1) + "}", str(val))
                else:
                    return "Ошибка аргументов1"
            else:
                if res.count("{}") > 0:
                    res = res.replace("{}", str(val), 1)
                else:
                    return "Ошибка аргументов2"
    return res


a=my_format("coordinates: {} и {}", '33','44')
a_1=my_format("coordinates: {} и {}", '33',44)
b=my_format("coordinates: {100} и {0}", '33','44')
c=my_format("coordinates: {1} и {0}", '33','44')
d=my_format("coordinates: {0} и {}", '33','44')
e=my_format("coordinates: {1} и {0}", '33',44)
f=my_format("coordinates: {1} и {2}", '33','44')

print("a = {}". format(a))
print("a_1 = {}". format(a_1))
print("b = {}". format(b))
print("c = {}". format(c))
print("d = {}". format(d))
print("e = {}". format(e))
print("f = {}". format(f))
