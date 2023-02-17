import asyncio
import requests as requests
from datetime import datetime


async def async_functions_list_processor(tasks_list):
    coroutines = []
    for task_to_do in tasks_list:
        coroutines.append(task_to_do)
    res = await asyncio.gather(*coroutines)
    return res


async def custom_coroutines_wrapper():
    
    args1 = 'https://www.google.com'
    args2 = 'https://www.facebook.com'
    args3 = 'https://github.com'

    # this task should be async itself but can call any type of methods
    async def custom_task1(arg):
        resp = requests.get(arg)
        return resp

    async def custom_task2(arg):
        resp = requests.get(arg)
        return resp
    
    # any io or network dependent tasks
    coroutines = [custom_task1(args1), custom_task2(args2), custom_task1(args3)]
    responses_list = await async_functions_list_processor(coroutines)
    return responses_list, len(coroutines)


def synchronous_method():
    dt1 = datetime.now()
    
    # -------- awaits async method even being synchronous itself ------- #
    resp_list, number_of_tasks = asyncio.run(custom_coroutines_wrapper())
    # ------------------------------------------------------------------ #
    
    resp_codes = [item.status_code for item in resp_list]
    dt2 = datetime.now()
    print(f'\nResponse list => ', resp_codes)
    print(f'Time taken for {len(number_of_tasks)} tasks = {(dt2 - dt1).seconds} seconds')
    return resp_list
    
    
synchronous_method()

