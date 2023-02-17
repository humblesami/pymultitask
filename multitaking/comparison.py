import asyncio
import threading
import multiprocessing
from datetime import datetime


def worker(arg):
    lr = 999910
    i = 1
    num1 = lr
    while num1 > 2:
        num1 -= 1
        i += 1
    i = 1
    while num1 < lr:
        num1 *= 2
        i += 1
    i = 1
    while num1 >= 2:
        num1 /= 2
        i += 1
    i = 1
    while i < lr:
        num1 += 1
        i += 1
    return f'{num1} from => {arg}'


async def worker1(arg):
    return worker(arg)


x_times = 40


def using_process():
    threads = []
    dt1 = datetime.now()
    for i in range(x_times):
        t = multiprocessing.Process(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for x in threads:
        x.join()

    dt2 = datetime.now()
    print(f"\nProcess => {(dt2 - dt1).seconds} => {str(dt2)[14:22]}")


def using_thread():
    threads = []
    dt1 = datetime.now()
    for i in range(x_times):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for x in threads:
        x.join()
    dt2 = datetime.now()
    print(f"\nThread => {(dt2 - dt1).seconds} => {str(dt2)[14:22]}")


def using_async():
    dt1 = datetime.now()
    
    async def run_async_method():
        coroutines = []
        for i in range(x_times):
            coroutines.append(worker1(i))
        values1 = await asyncio.gather(*coroutines)
        # print(values1)
        return values1

    values = asyncio.run(run_async_method())
    dt2 = datetime.now()
    print(f"\nAsync => {(dt2-dt1).seconds} => {str(dt2)[14:22]}")
    return values


def using_nothing():
    dt1 = datetime.now()
    for i in range(x_times):
        worker(i)
    dt2 = datetime.now()
    print(f"\nSimple => {(dt2 - dt1).seconds} => {str(dt2)[14:22]}")


def main():
    dt_start = datetime.now()
    print(f'\nTime starts now => {str(dt_start)[14:22]}')
    using_nothing()
    using_process()
    using_async()
    using_thread()
    
    
main()
