# Заменяет символы табуляции на 4 пробела
def tab_to_blank(str):
    return str.replace("\t", "    ")


# Заменяет 4 пробела на символы табуляции
def blank_to_tab(str):
    return str.replace("    ", "\t")


# Считывает содержимое файла, которое требуется заменить
def read_file_to_str(file_name_in):
    with open(file_name_in, 'rt', encoding="UTF-8") as file_in:
        return file_in.read()


# Записывает в новый файл измененный текст
def write_file_from_str(file_name_out):
    with open(file_name_out, 'w', encoding="UTF-8") as file_out:
        file_out.write(str_out)
        print("Файл {} записан".format('text_res.txt'))


str_in = read_file_to_str('text.txt')
print('Для сворачивания табуляции введите 0, для разворачивания - 1, '
      'для отмены - любой символ')
choice = input("Введите число:")

if choice == "0":
    str_out = tab_to_blank(str_in)
    write_file_from_str('text_res.txt')
else:
    if choice == "1":
        str_out = blank_to_tab(str_in)
        write_file_from_str('text_res.txt')
    else:
        print("Операция отменена ")
