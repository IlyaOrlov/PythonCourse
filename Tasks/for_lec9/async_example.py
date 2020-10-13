import asyncio

res = 0

# Производим вычисления
async def calc_fun(num):
    global res
    while num > 0:
        print(num)
        if num % 10 == 0:
            res = num
        num -= 1
        await asyncio.sleep(0.1)


# Сообщаем о статусе вычислений
async def status_fun():
    global res
    prev_res = 0
    while res > 0:
        if res != prev_res:
            print(f'{res} numbers remain')
            prev_res = res
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    ev_loop = asyncio.get_event_loop()
    tasks = [ev_loop.create_task(calc_fun(1000)),
             ev_loop.create_task(status_fun())]
    futures = asyncio.wait(tasks)
    ev_loop.run_until_complete(futures)
    ev_loop.close()


# async def main():
#     tasks = [asyncio.create_task(calc_fun(8000)), asyncio.create_task(status_fun())]
#     await asyncio.gather(*tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())
