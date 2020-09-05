def to_title(string):
    new_str = ""
    i = 0
    if len(string) > 0:
        new_str = string[0].capitalize()
        i += 1
    while i < len(string):
        new_str += string[i]
        i += 1
    return new_str


print(to_title('what a wonderful world'))
