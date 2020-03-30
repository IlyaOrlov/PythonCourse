stroka = input('Введите строку: ')
if stroka.find('    ') > 0:
    print('\\t'.join(stroka.split('    ')))
elif stroka.find('/t') > 0:
    print('    '.join(stroka.split('/t')))
