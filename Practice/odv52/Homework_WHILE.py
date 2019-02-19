cmd = input('Введите команду для выхода из консоли Python : ')
while cmd != 'exit':
    print('Не верно!')
    cmd = input('Попробуйте еще раз : ')
    if cmd != 'exit':
        print('Опять мимо((!')
    #continue
else:
    print('ВЕРНО!')
