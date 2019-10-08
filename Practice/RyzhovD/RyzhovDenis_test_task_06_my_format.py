'''
Function my_format which is my realization of format.
It works with substitution of {} with everything you want.
'''

import re

def my_format(string, *args):
    if len(args) == 0:  # When there is None for substitution
        print('\nYou did not provide substitutions.')
        return string
    if len(re.findall('{\d+}', string)) > 0:  # Case of 'numbered' patterns
        findObj = re.findall('{\d+}', string)
        for x in findObj:  # x is an string, kind of '{1}' or '{0}'
            x_int = int(x[1:len(x)-1])  # extracting integer number from x
            # string = re.sub(repr(x), str(args[x_int]), string)  # does not raise error,
                                                            # but do nothing.
            # The reason is: '{' and '}' are special symbols for re.methods.
            # Therefore here we use replace method for string.
            string = string.replace(x, str(args[x_int]))
    else:
        ### Case of not 'numbered' patterns (i.e., just {})
        for x in args:
            string = re.sub('{}', str(x), string, count=1)
            # Without count=1 both substitutions are '9' and
            # string = 'That is one small step for 9, one giant 9 for mankind',
            # since re.sub without count find all '{}' and substitute them with x.
    return string

#_# TEST
Quote = 'That is one small step for {}, one giant {} for mankind'

# print('')
# frmt = my_format(Quote)
# print(frmt)
#
# print('')
# frmt = my_format(Quote, 'a frog')
# print(frmt)
#
# print('')
# frmt = my_format(Quote, 9)
# print(frmt)

print('')
frmt = my_format(Quote, 9, 7)
print(frmt)

# Quote = 'coordinates: {}, {}'
# print('')
# frmt = my_format(Quote, '37.4N', '18.3W')
# print(frmt)

print('')
Quote = '{1}, {0}, {2}'
frmt = my_format(Quote, 'a', 'b', 'c')
print('The answer is: {}'.format(frmt))