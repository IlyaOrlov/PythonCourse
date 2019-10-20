import time
from celery import Celery


app = Celery('celery_consumer')
app.conf.CELERY_RESULT_BACKEND = 'amqp://'
#app.conf.CELERY_INCLUDE = []
app.conf.BROKER_URL = 'amqp://guest@localhost//'
#app.conf.CELERYD_POOL = 'gevent'
#app.conf.update(
#    CELERY_RESULT_BACKEND='amqp://',
#)

@app.task
def add(x,y):
    print('add({0}, {1})'.format(x, y))
    time.sleep(1)
    return x + y

@app.task
def mul(x,y):
    print('mul({0}, {1})'.format(x, y))
    return x * y

@app.task
def xsum(l):
    print('xsum({0})'.format(l))
    return sum(l)

@app.task
def broken_task():
    raise Exception('failed')

@app.task
def on_task_error(task_id, task_name):
    print('ERROR IN TASK {0}: {1}'.format(task_id, task_name))

@app.task
def print_task(x):
    print(x)

@app.task
def on_task_success(task_id, task_name):
    print('TASK SUCCEDED {0}: {1}'.format(task_id, task_name))

if __name__ == '__main__':
    app.worker_main()