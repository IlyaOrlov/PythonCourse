"""
This module read the file and substitute tabulations with 4 spaces or vv.
Please use 'q4.txt' as accompanying file for test.
There are a tab in 1st line and 4 spaces in 2nd line.
"""

filename = input('Please, input the name of your file with extension: ')
fo = open(filename,'r')
filetext = fo.read()
print(filetext)  # print text for further comparison
fo.close()  # to exclude smth bad

print('')  # empty line
# filetext = filetext.replace('\t','QQQQ')  # C&D
# filetext = filetext.replace('    ','QQQQ')  # C&D

flag = input('If you prefer change tabulation on 4 spaces, please, press 0\n'
             'for inverse change, press t: ')

if flag == '0':
    filetext = filetext.replace('\t', 'QQQQ')
elif flag == 't':
    filetext = filetext.replace('    ', 'TTTT')
else:
    print('You are miss the target. The text remains the same.')

print(filetext)