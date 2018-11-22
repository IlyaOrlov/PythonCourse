#  -*- coding: utf-8 -*-
# 08.11 - [ИО]:  Тег "-*- coding: utf-8 -*-" сообщает интерпретатору Python2,
# что в скрипте используется кодировка utf-8, которая включает в т.ч. и
# русские символы. Таким образом Python2 не будет ругаться на
# комментарии и прочие символы на русском языке.
# Для Python3 такой тег указывать не нужно. Он и так все понимает.

# 08.11 - [ИО]:  Проверено (есть замечания).
for i in range(1,101):
    # 08.11 - [ИО]:  Если число без остатка делится на 15, значит оно и на 3
	# и на 5 делится без остатка.
    if (i%3==0 and i%5!=0): print 'Fizz'
    elif (i%3!=0 and i%5==0): print 'Buzz'
    elif (i%3==0 and i%5==0): print 'FizzBuzz'
    else: print i
