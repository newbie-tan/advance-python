"""
@author: tony-tan
@time: 2019/6/21 12:05
@file: loop_test_2.py
@site: 
@describe: 协程返回值获取你及协程执行完成的回调
"""
import asyncio
import time
from functools import partial


async def get_html(start_time):
	print("start get html")
	await asyncio.sleep(1)
	print(time.time() - start_time)
	return "tony"


def call_back(future):
	print(future.result())
	print("send email to tony")


if __name__ == '__main__':
	start_time = time.time()
	loop = asyncio.get_event_loop()
	# task = loop.create_task() 也能达到: 向事件循环器提交协程任务
	get_future = asyncio.ensure_future(get_html(start_time))  # future 对象中存有返回值
	get_future.add_done_callback(call_back)
	loop.run_until_complete(get_future)
	print(get_future.result())
