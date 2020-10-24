def chargen():
    for c in '0123456789':
        yield c


words = [c + c for c in chargen()]
print(words)
