
def to_title(str):
    l = str.split(' ')
    i = 0
    newstr = None
    while i < len(l):
        l[i] = l[i].capitalize()
        i += 1
    newstr = ' '.join(l)
    return newstr


str = 'fedotova elena vladimirovna'
print(to_title(str))