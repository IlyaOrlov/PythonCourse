def to_title(text):
    text = text.strip()
    a = [elem[0].upper() + elem[1:] for elem in text.split()]
    return " ".join(a)


print(to_title('   orlov     Ilya    evgenyevich   '))
