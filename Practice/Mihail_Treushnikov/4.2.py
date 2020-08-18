def interpolate(string):
    dict = {' ':'*', '.':'!'}
    for key, value in dict.items():
        string = string.replace(key, value)
    return string


str = "Hello my frien. What is your name."
print(interpolate(str))