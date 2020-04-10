s = " Я куплю один ластик, два карандаша и три руки"
slov = {"один": "1", "два": "2", "три": "3"}
spisok = s.split()
i = 0
while i < len(spisok):
    if spisok[i] in slov:
        spisok[i] = slov[spisok[i]]
    i += 1
print(" ".join(spisok))
