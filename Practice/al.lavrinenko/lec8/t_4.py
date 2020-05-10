import re


def to_title(string):
    return re.sub(r'\b[a-z]', lambda x: x.group().upper(), string)


print(to_title('neutral milk hotel'))
