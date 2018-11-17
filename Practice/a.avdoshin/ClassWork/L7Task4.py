import re


def to_title(input_str):
    input_str = input_str[0].upper() + input_str[1:]
    words = re.split('[\s]', input_str)
    result = ''
    for word in words:
        result += ' ' + word[0].upper() + word[1:]

    return result[1:]


print(to_title('orlov Ilya evgen'))
