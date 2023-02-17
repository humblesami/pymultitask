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


def print_time_taken(dt1, method='Simple'):
    dt2 = datetime.now()
    ms = round(((dt2 - dt1).microseconds / 1000))
    print(f"\n{method}:\t\t{(dt2 - dt1).seconds} seconds + {ms} milliseconds =>\t\t{str(dt2)[14:23]}")


def using_process():
    threads = []
    dt1 = datetime.now()
    for i in range(x_times):
        t = multiprocessing.Process(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for x in threads:
        x.join()
        
    print_time_taken(dt1, "MultiProc")


def using_thread():
    threads = []
    dt1 = datetime.now()
    for i in range(x_times):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for x in threads:
        x.join()
    print_time_taken(dt1, "ThreadLoop")


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
    print_time_taken(dt1, "AsyncLoop")
    return values


def using_nothing():
    dt1 = datetime.now()
    for i in range(x_times):
        worker(i)
    print_time_taken(dt1, "NoThread")


def main():
    dt_start = datetime.now()
    print(f'\nTime line\t\t\t\t\t\t\t\t\t =>\t\t{str(dt_start)[14:22]}')
    using_process()
    using_nothing()
    using_async()
    using_thread()
    
    
main()
