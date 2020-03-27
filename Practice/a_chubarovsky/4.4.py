def space_to_tab(file):
    for line in file:
        line = line.replace('    ', '\t')
        print(line)


def tab_to_space(file):
    for line in file:
        line = line.replace('\t', '    ')
        print(line)


f = open("my_file.txt", "r+")
cmd = int(input("Введите команду (1 - заменить пробелы на табуляцию; 2 - заменить табуляцию на пробелы: "))
if cmd == 1:
    space_to_tab(f)
else:
    tab_to_space(f)
f.close()
