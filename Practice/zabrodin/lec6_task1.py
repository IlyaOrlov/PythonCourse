def chargen():
        yield from'0123456789'


words = [c+c for c in chargen()][:10]
print(words)
