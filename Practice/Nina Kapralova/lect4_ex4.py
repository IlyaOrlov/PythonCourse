def change(a: str):
    if '    ' in a:
        b = a.replace('    ', '\t')  # для замены пробелов на табуляцию
    elif '\t' in a:
        b = a.replace('\t', '    ')  # для замены табуляции на пробелы
    print(b)

change('    запуск    функции    для проверки')
change('\tпроверка\tфункции')