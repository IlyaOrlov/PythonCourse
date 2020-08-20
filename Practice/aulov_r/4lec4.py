def roll_up(file):
    for line in file:
        line = line.replace(' ', '    ')
        print(line)

def deploy(file):
    for line in file:
        line = line.replace('    ', ' ')
        print(line)

a = open("file1.txt", "r+")
cmd = int(input("Введите команду 1 - меняем пробелы на табуляцию; 2 - меняем табуляцию на пробелы: "))
if cmd == 1:
    roll_up(a)
else:
    deploy(a)
a.close()
