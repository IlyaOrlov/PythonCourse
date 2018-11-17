def chargen():
    # while True: - программа будет вычисляться вечно,
    # можно или убрать этот оператор или заменить на какое либо условие,
    # которое будет прерывать наш цикл while
    for c in '0123456789':
        yield c


words = [c + c for c in chargen()]
print(words)
