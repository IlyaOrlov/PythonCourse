# Интерполировать некие шаблоны в строке.Есть строка с определенного вида форматированием.
# необходимо заменить в этой строке все вхождения шаблонов на их значение из словаря

d = {"red": "blue", "car": "bike", "beautiful": "cool"}


def dict_words():
    file = open("text.txt", "r")
    for i in file:
        for k, v in d.items():
            i = i.replace(k, v)
        print(i)


dict_words()
