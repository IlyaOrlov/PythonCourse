import threading
import queue
import time


start = time.perf_counter()

q = queue.Queue()


def worker():  # функция выполняемая в дочернем потоке
    with open('outfile.txt', 'w') as fout:
        item = '0'
        while item.isdigit():
            item = q.get()  # ожидаем появление элемента в очереди
            fout.write('start\n')
            if item.isdigit():
                fout.write(f'{int(item) ** 2}, ')
            fout.write('finish\n')
            q.task_done()  # уведомляем очередь о завершении обработки


t = threading.Thread(target=worker)
t.start()

with open('infile.txt') as fin:
    for line in fin:
        items = line.split()
        for each in items:
            if each.isdigit():
                q.put(each)  # добавляем элемент в очередь и ничего не ждем,
                q.join()  # ожидаем обработки элементов в очереди
    q.put('stop')  # добавляем элемент в очередь и ничего не ждем,
    q.join()  # ожидаем обработки элементов в очереди

t.join()

print('Total time: {}'.format(time.perf_counter() - start))