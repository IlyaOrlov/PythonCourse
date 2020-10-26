def interpolate(string, dictionary):
<<<<<<< HEAD
    for key in dictionary:
        if key in string:
            string = string.replace(key, dictionary[key])
=======
    for key in dictionary:       
        string = string.replace(key, dictionary[key])
>>>>>>> c8db6ed0c1733acc791023d6cbb9cab97186a5ae
    return string

string = "Люди только чай пьют, а в их душах совершается трагедия"
dictionary = {'чай': 'кофе', 'трагедия': 'комедия'}
print(string)
<<<<<<< HEAD
print(interpolate(string, dictionary))
=======
print(interpolate(string, dictionary))
>>>>>>> c8db6ed0c1733acc791023d6cbb9cab97186a5ae
