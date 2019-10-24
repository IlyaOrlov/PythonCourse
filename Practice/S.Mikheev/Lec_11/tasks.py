# -*- coding: utf-8 -*-
# Сначала запускаем python –m celery worker --app=tasks -l info
# Затем запускаем python –m celery -A tasks beat --loglevel=info
import requests
import re
from datetime import datetime, date
import time
from celery import Celery
from celery.schedules import crontab
import os
from celery.task import periodic_task


os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('tasks')
app.conf.result_backend = 'amqp://'
app.conf.broker_url = 'amqp://guest@localhost//'
CELERY_TIMEZONE = 'UTC'


def convert(x):
    t = x - 273.15
    t = float('{:.3f}'.format(t))
    return t


@periodic_task(
    run_every=(crontab(minute='*/20')),
    name="get_weather",
    ignore_result=True
)
def get_weather():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"callback": "test", "id": "2172797", "lang": "Ru", "units": "\"metric\" or \"imperial\"",
                   "mode": "xml, html", "q": "Nizhniy Novgorod,RU"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "6d9c4ed203mshfc0ec67c6b7fa0dp1a0d03jsn34f416af7a76"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    res = re.search(r'\((.+)\)', response.text)
    weather = eval(res.group(1))
    result = '{}: Weather from {}: {}, temperature {} C{}, Wind {} m/s, Pressure {} hPa, Humidity {} %\n'.format(
        datetime.now(), weather['name'],
        weather['weather'][0]['description'],
        convert(weather['main']["temp"]),
        u"\u00b0",
        weather["wind"]['speed'],
        weather['main']["pressure"],
        weather['main']["humidity"])
    with open('logfile.log', "a", encoding='utf8') as file:  # Открываем файл на запись
        file.write(result)
        print('Запись выполнена')


if __name__ == '__main__':
    app.worker_main()

