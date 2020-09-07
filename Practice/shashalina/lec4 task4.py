# Task 4.4
# Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле или строке.
# То есть, передается на вход файл или строка, необходимо заменить все символы табуляции на четыре пробела,
# либо же заменить все комбинации из четырех символов пробела на символ табуляции.

import os.path

def tab(obj):

    if os.path.exists(obj) == True:
        fr = open(obj, "r+")
        file_str = fr.read()
        fr.close

        print (file_str)

        lst_file_str = file_str.split("    ")
        inter_lst_file_str = []

        for i in lst_file_str:
            inter_lst_file_str.append(i.expandtabs(tabsize=4))

        new_obj = "\t".join(inter_lst_file_str)

        print(new_obj)

        fw = open(obj, "w+")
        fw.write(new_obj)
        fw.close

    else:
        lst_str = obj.split("    ")
        inter_lst = []

        for i in lst_str:
            inter_lst.append(i.expandtabs(tabsize=4))

        new_obj = "\t".join(inter_lst)

        print(new_obj)
        return new_obj

tab("text.txt")
tab("The cat\tsee\ta\ttree    .")

