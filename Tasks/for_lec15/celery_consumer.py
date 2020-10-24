# Версия для Linux. В Windows запускается с gevent: python –m celery –A celery_consumer worker –P gevent
import time
from celery import Celery


app = Celery('celery_consumer', broker='amqp://', backend='redis://localhost')


@app.task
def add(x, y):
    print(f'add({x}, {y})')
    time.sleep(0.1)
    return x + y

@app.task
def mul(x, y):
    print(f'mul({x}, {y})')
    return x * y

@app.task
def xsum(lst):
    print(f'xsum({lst})')
    return sum(lst)

@app.task
def broken_task():
    raise Exception('failed')

@app.task
def on_task_error(task_context, status, traceback, task_name):
    print(f'ERROR IN TASK {task_name}: {task_context}; {status}; {traceback}')

@app.task
def print_task(x):
    print(x)

@app.task
def on_task_success(task_id, task_name):
    print(f'TASK SUCCEDED {task_id}: {task_name}')


if __name__ == '__main__':
    app.Worker().start()
    # app.worker_main()
