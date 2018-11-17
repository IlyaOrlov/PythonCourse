#for Python 3.6
#task 5

string_example = '''Madge shoots him a look,
trying to see if it's a genuine compliment or if he's just being ironic.
It is a pretty dress, but she would never be wearing it ordinarily.
She presses her lips together and then smiles.
“Well, if I end up going to the Capitol, I want to look nice, don't I?”'''

dict_example = {"it's":"it is","I'm":"I am", "you're":"you are",
                "she's":"she is","he's":"he is",
                "haven't":"have not", "hasn't":"has not",
                "don't":"do not", "can't":"can not"}

def change_words(mystring, mydict):
    '''Заменяет части строки по ключу из словаря'''
    newstring = mystring
    for i in iter(mydict):
        newstring = newstring.replace(i, mydict[i])
    return newstring

if __name__ == '__main__':
    print(string_example)
    print("Строка после замены:")
    print(change_words(string_example, dict_example))

