def interpolate(string, dictionary):
    for key in dictionary:
        if key in string:
            string = string.replace(key, dictionary[key])
    return string


dictionar = {'python': 'это самое', 'успел': 'опаздал', 'я': 'я опять'}
stroka = 'и вот я успел сделать python'
print(interpolate(stroka, dictionar))
