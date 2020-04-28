import subprocess  # импортируем библиотеку


def file_content(name):  # определяем функцию обработчик
    subprocess.run(['type', name],
                   shell=True)  # в списке используем команды для командной строки[type - вывод содержимого текстового файла, name - имя]

file_content("111")  # вызов функции
