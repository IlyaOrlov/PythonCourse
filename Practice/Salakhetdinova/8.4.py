def to_title(string):
    str = string.split(" ")
    new_str = ""
    i = 0
    for i in range(len(str)):
        new_str += str[i][0].capitalize()
        new_str += str[i][1:]
        new_str += " "
    return new_str


