'''
Function my_format which is my realization of format.
It works with substitution of {} with everything you want.
But I have an error for 'numbered' version: when I have {\d}.
'''

import re

def my_format(string, *args):
    if len(args) == 0:  # When there is None for substitution
        print('\nYou did not provide substitutions.')
        return string
    if len(re.findall('{\d+}', string)) > 0:  # Case of 'numbered' patterns
        findObj = re.findall('{\d+}', string)
        for x in findObj:  # x is an string, kind of '{1}' or '{0}'
            print('x = {}'.format(x))  ##
            print('repr(x) = {}'.format(repr(x)))  ##
            x_int = int(x[1:len(x)-1])  # extracting integer number from x
            print('x_int = {}'.format(x_int))  ##
            print('args[x_int] = {}'.format(args[x_int]))  ##
            string = re.sub(repr(x), str(args[x_int]), string)  # does not raise error,
                                                            # but do nothing
            # string = re.sub(x, str(args[x_int]), string)  # error
            # string = re.sub(r'\{1\}', str(args[1]), string)  # it works
            print(string)  ##
            print('-- iter --\n')  ##
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
print('answer is {}'.format(frmt))