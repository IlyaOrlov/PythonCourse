def templates(newLine):
    dict = {'снег':'дождь', 'не':'очень'}

    for k, v in dict.items():
        newLine = newLine.replace(k, v)
    print(newLine)

line = 'Сегоня идет снег. Я не люблю это время.'
print(line)
templates(line)