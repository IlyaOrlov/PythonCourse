"""
This module read the file and substitute blocks in text using dictionary.
Please use 'qs.txt' as accompanying file for test.
"""

filename = input('Please, input the name of your file with extension: ')
fo = open(filename,'r')
filetext = fo.read()
print(filetext)  # option to read the original text (it will be a 'string')
# print(type(filetext))  # C&D
fo.close()  # to exclude smth bad

# Create dictionaries. Note, that use only word roots (for Russian)
# And now we omit the case of plurals
# (sometimes they interfere with single, e.g. розы - им.мн. == вин.ед.)
# NB! short roots should follow long ones
my_dict_keys = ['розы', 'розо', 'роз',
                'Розы', 'Розо', 'Роз']
my_dict_values = ['сажи', 'саже', 'саж',
                  'Сажи', 'Саже', 'Саж']


if len(my_dict_keys) == len(my_dict_values):
    my_dict = dict(zip(my_dict_keys, my_dict_values))
else:
    print('Length of keys and values is not the same!')

# print(my_dict)  ## C&D

my_dict_range = my_dict.items()
# Returns pairs (key, value) for each element of the dictionary.

for key, value in my_dict_range:
    filetext = filetext.replace(key,value)

print(filetext)

# FROM pythonz.net
# my_str = 'barbarian'
# my_str = my_str.replace('bar', 'mur')  # 'murmurian'
# my_str = my_str.replace('mur', 'bur', 1)