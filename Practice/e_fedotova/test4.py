guess = ''

while guess != 'exit':
    guess = input('Введите целое число или exit: ')
    if guess.isdigit():
        print(int(guess) ** 2)
    elif guess != 'exit':
        print(guess, '- не целое число')

print('exiting...')





