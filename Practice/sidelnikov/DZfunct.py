def bolshee1(chislo1, chislo2):
    if (int(chislo1) > int(chislo2)):
        print('Otvet1 = {}'.format(chislo1))
    else:
        print('Otvet1 = {}'.format(chislo2))


def bolshee2(chislo1, chislo2):
    if (int(chislo1) > int(chislo2)):
        return chislo1
    else:
        return chislo2


chislo1 = input("Vvediet chislo1:")
chislo2 = input("Vvedite chislo2:")
bolshee1(chislo1, chislo2)
chislo3 = bolshee2(chislo1, chislo2)
print('Otvet2 = {}'.format(chislo3))