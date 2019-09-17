d = {'name': 'Bob', 'tel': 'number', 'address': 'street'}
val = d.values()
a = str(list(val))
for value in d:
    #stroka = 'hello, %s %s %s{} {} {} !!!'.format(value) не работает
    stroka = 'hello, %(name) %s %s !!!' % d.values() #
    print(stroka)

