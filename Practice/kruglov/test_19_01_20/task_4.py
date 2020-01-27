# 4 Function to_title


def to_title(str1):
    lst1 = []
    lst2 = []
    str2 = ""
    lst1 = str1.split(' ')
    for el in lst1:
        lst2.append(el.capitalize())
    str2 = ' '.join(lst2)
    return str2


print(to_title('orlov Ilya evgenyevich'))
