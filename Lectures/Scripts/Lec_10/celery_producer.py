# -*- coding: utf-8 -*-
from celery import group, chain, chord

from celery_consumer import (add, mul, xsum, broken_task, on_task_error, print_task, on_task_success)


result = add.delay(1, 1)  # асинхронный вызов, эквивалентен add.apply_async((1, 1))
print(result.state)  # PENDING
print(result.ready())  # False
print(result.get(timeout=3))  # ожидаем результата и выводим его
print(result.state)  # SUCCESS
print(result.ready())  # True
print(add(1, 1))  # синхронный вызов
print(group(add.s(i, i) for i in range(10))().get())  # запуск группы задач
# результат выполнения первой задачи используется как аргумент для следующей
print(chain(add.s(4, 4) | mul.s(8))().get())
# результат выполнения группы задач используется как аргумент для xsum,
# вызываемой как callback
print(chord(group(add.s(i, i) for i in range(10)), xsum.s())().get())
# линкование одной задачи к другой в случае неудачного выполнения первой
broken_task.apply_async(link_error=on_task_error.s('broken_task'))
# линкование одной задачи к другой в случае успешного выполнения первой
print_task.apply_async(('something', ), link=on_task_success.s('print_task'))
