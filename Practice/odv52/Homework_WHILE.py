cmd = input('Введите команду для выхода из консоли Python : ')
while cmd != 'exit':
    if cmd.isdigit():
        print('Вводите только буквы!')
        cmd = input('Попробуйте еще раз : ')
    else:
        print('Неверно!')
        cmd = input('Попробуйте еще раз : ')
else:
    print('ВЕРНО!')
