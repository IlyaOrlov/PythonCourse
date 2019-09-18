def change_spaces(file_name):
    with open(file_name, 'r+') as file_object:
        lines = file_object.readlines()

    format_text = ''
    for line in lines:
        format_text += line.replace('    ', '\t')

    return format_text


q = change_spaces('some_text_file.txt')
print(q)


def change_tab(file_name):
    with open(file_name, 'r+') as file_object:
        lines = file_object.readlines()

    format_text = ''
    for line in lines:
        format_text += line.replace("\t", '    ')

    return format_text


qq = change_spaces('some_text_file2.txt')
print(qq)


"""
Для ручного ввода:
x = input("Если хотите заменить кобинацию прбелов на символ табуляции,"
          " введите - t, наоборот - s : ")
if x == 't':
    name = input("Введите название файла с расширением: ")
    text_w_t = change_spaces(name)
    print("Измененный текст: ")
    print('\n' + text_w_t)
elif x == 's':
    name = input("Введите название файла с расширением: ")
    text_w_s = change_tab(name)
    print("Измененный текст: ")
    print('\n' + text_w_s)

else:
    print('Выход.')"""
