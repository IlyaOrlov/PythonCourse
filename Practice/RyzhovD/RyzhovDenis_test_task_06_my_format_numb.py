'''
Function my_format which is my realization of format.
It works with substitution of {} with everything you want.
But I have an error for 'numbered' version: when I have {\d}.
'''

import re

def my_format(string, *args):
    if len(args) == 0:  # When there is None for substitution
        return (string)
    elif len(re.findall('{\d}', string)) > 0:  # Case of 'numbered' patterns
        # print(re.findall('{\d}', string))
        for j in range(0, len(args)):
            pattern_j = '{' + str(j) + '}'
            # print(pattern_j)
            # print(type(pattern_j))
            # print(args[j])
            if isinstance(args[j], str):
                string = re.sub(pattern_j, args[j], string)  # ! HERE!
            else:
                subst = str(args[j])
                string = re.sub(pattern_j, subst, string, count=1)

    else:
        ## Case of not 'numbered' patterns (i.e., just {})
        k = 0
        for x in args:
            if isinstance(args[k], str):
                string = re.sub('{}', args[k], string, count=1)
            else:
                subst = str(args[k])
                string = re.sub('{}', subst, string, count=1)
            k += 1
        return(string)

### TEST
Quote = 'That is one small step for {}, one giant {} for mankind'

print('')
frmt = my_format(Quote)
print(frmt)

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

Quote = 'coordinates: {}, {}'
print('')
frmt = my_format(Quote, '37.4N', '18.3W')
print(frmt)

print('')
Quote = '{1}, {0}, {2}'
frmt = my_format(Quote, 'a', 'b', 'c')
print(frmt)