def interpolate(string, dictionary):
    for key in dictionary:
        if key in string:
            string = string.replace(key, dictionary[key])
    return string

string = "Люди только чай пьют, а в их душах совершается трагедия"
dictionary = {'чай': 'кофе', 'трагедия': 'комедия'}
print(string)
print(interpolate(string, dictionary))