'''
There is really no time to write a proper documentation and comments.
I'll do it later.
Sorry.
'''

import re
def my_format(string, *args):
    k = 0
    if len(args) == 0:
        return(string)
    else:
        for x in args:
            # print(args[k])  ##
            # print(type(args[k]))  ##
            if isinstance(args[k], str):
                string = re.sub('{}', args[k], string, count=1)
            else:
                subst = str(args[k])
                string = re.sub('{}', subst, string, count=1)
            # print(str_new)  ##
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