words = dict()
words['T'] = 'Table'
words['C'] = 'Cat'
str = ['T', 'C']
for i in str:
    if i in words:
        print(i + " is " + words[i])