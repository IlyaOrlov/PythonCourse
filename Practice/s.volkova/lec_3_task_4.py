#for Python 3.6
#task 4

import sys

def change_to_tab(some_string):
    #Меняет 4 пробела подряд на знак табуляции
    new_string = some_string.replace("    ", "\t")
    return new_string

def change_to_space(some_string):
    #Меняет знак табуляции на 4 пробела
    new_string = some_string.replace( "\t", "    ")
    return new_string   

def main():
    #проверяет аргументы командной строки
    args = sys.argv[1:]
    if len(args)!=2 or args[0] not in ["--tab", "--space"]:
        print('Введите аргументы "--tab" или "--space" и название файла')
    else:
        #Открывает указанный файл и создает новый файл для записи
        input_file = open(args[1], "r")
        insert_point = args[1].rfind(".")
        output_name = args[1][:insert_point] + "_new" + args[1][insert_point:]
        output_file = open(output_name, "w")
        #В зависимости от введенного аргумента производит замену
        if args[0] == "--tab":
            for line in input_file:
                output_file.write(change_to_tab(line))
            print("Создан файл " + output_name + ", пробелы заменены на знак табуляции")
        elif args[0] == "--space":
            for line in input_file:
                output_file.write(change_to_space(line))
            print("Создан файл " + output_name + ", знаки табуляции заменены на пробелы")
        input_file.close()
        output_file.close()
        
                        
if __name__ == '__main__':
    main()     
