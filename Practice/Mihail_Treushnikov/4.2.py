def interpolate(string_text):
    dictionary = {' ': '*', '.': '!'}
    for key, value in dictionary.items():
        string_text = string_text.replace(key, value)
    return string_text


text = "Hello my friend. What is your name."
print(interpolate(text))
