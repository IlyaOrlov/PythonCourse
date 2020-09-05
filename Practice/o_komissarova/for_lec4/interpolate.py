def interpolate(string, dictionary):
    for key in dictionary:
        if key in string:
            string = string.replace(key, dictionary[key])
    return string


dict = {'cat': 'кошка', 'table': 'стол'}
str = 'cat is on the table'
print(interpolate(str, dict))

