def chargen():
#Ошибка здесь: "while True:" можно не прописывать,
# т.к. цикл "for" и так перебирает элементы строки
    for c in '0123456789':
        yield c
#Каждая итерация элемента строки
        print(c)
words = [c+c for c in chargen()][:10]
#Вывод сгенерированного списка
print(words)