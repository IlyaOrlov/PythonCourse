# Ошибка: использован бесконечный цикл, во внутреннем цикле отсутствуют проверки на необходимое количество элементов

def chargen(counter=10):
    while True:
        for c in '0123456789':
            if counter > 0:
                counter -= 1
                yield c

            else:
                return c

words = [c+c for c in chargen(10)] #[:10]
print (words)
