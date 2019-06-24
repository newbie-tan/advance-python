"""
@author: tony-tan
@time: 2019/6/18 13:21
@file: thread_pool_concurrent_futures.py
@site: 
@describe: python 的线程池
"""

from concurrent import futures
import time

# 线程池
# 需求: 主线程中可以获取某一个线程或者某一个任务的状态,以及返回值
# 需求: 一个线程完成的时候,主线程可以立即知道
# future 可以让多线程和多进程编码接口一致
from concurrent.futures import as_completed, wait


def get_html(times):
	time.sleep(times)
	print("got page {} success".format(times))
	return times


executor = futures.ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中,submit 是立即返回的
# task_1 = executor.submit(get_html, (2))
# task_2 = executor.submit(get_html, (3))

# print(task_1.done())


# 即时获取以及成功的task 的返回
urls = [4, 2, 3, 5]
all_task = [executor.submit(get_html, (url)) for url in urls]

for task in as_completed(all_task):
	# as_complete 监听已经完成的线程,并获取返回值
	data = task.result()
	print("get {} page".format(data))

# 获知用executor.map


# wait 可以阻塞主线程


# future 未来对象:Future 的设计理念

