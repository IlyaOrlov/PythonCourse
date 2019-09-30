def count_symbol(lst, symb):
    counter = 0
    for x in lst:
        if x == symb:
            counter += 1
    return counter


### TEST
print('')
words = 'Hi, Elvis, I am here!'
symb = 'i'
print(words)
cc = count_symbol(words, symb)
if cc == 0:
    print('Symbol \'{}\' not found.'.format(symb))
elif cc == 1:
    print('There is 1 symbol \'{}\' here.'.format(symb))
else:
    print('There are {} symbols \'{}\' here.'.format(cc, symb))

print('')
words = 'It\'s been a hard days night'
symb = 'D'
print(words)
cc = count_symbol(words, symb)
if cc == 0:
    print('Symbol \'{}\' is not found.'.format(symb))
elif cc == 1:
    print('There is 1 symbol \'{}\' here.'.format(symb))
else:
    print('There are {} symbols \'{}\' here.'.format(cc, symb))