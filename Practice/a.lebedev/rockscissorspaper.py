import random
w = 0
l = 0
z = 0
while True:
    choice = str(input())
    if choice == 'камень' or choice == 'ножницы' or choice == 'бумага':
        base = ["камень", "ножницы", "бумага"]
        comp = random.choice(base)
        base.append(base[0])
        base1 = base[1:]
        numchoice = base.index(choice)
        numcomp = base1.index(comp)
        if (numcomp - numchoice) == 0:
            print("YOU WIN")
            w += 1
            print(w, l, z)
        elif (numcomp - numchoice) == 1:
            print("YOU LOSE")
            l += 1
            print(w, l, z)
        else:
            print("REPEAT")
            z += 1
            print(w, l, z)
    elif choice == 'exit':
        print('WINS = {}'.format(w))
        print('LOSES = {}'.format(l))
        print('DRAWNS = {}'.format(z))
    else:
        print('Попробуйте еще раз')
        continue

