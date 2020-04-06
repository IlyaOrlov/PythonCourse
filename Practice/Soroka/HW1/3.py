# Задание 4 Лекция 4
with open('my_file.txt', 'r') as f:
    old_format = f.read()

new_format = old_format.replace('    ', '####')
# у меня почему-то в файле .txt табуляция преобразуется в 4 пробела по умолчанию,
# поэтому я заменила \t на ####

with open('my_file.txt', 'w') as f1:
    f1.write(new_format)

# Задание 5 Лекция 4
d = {
    'name': 'Анна',
    'level': 33,
    'team': 'NwCrSclBgn'
}

message = f"""Здравствуйте, {d['name']}, поздравляем, Вы достигли {d['level'] + 1} уровня,
продолжайте свой прогресс в нашей команде {d['team']}!"""

print(message)



