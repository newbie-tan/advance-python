"""
@author: tony-tan
@time: 2019/6/21 13:48
@file: corotine_nest.py
@site: 
@describe: 协程的嵌套
"""
# 协程的嵌套调用流程

import asyncio

"""
1. 运行事件调度器loop
2. 调度运行task - print_sum()- 第一层协程
3. 运行到 await compute(), 协程print_task 进入暂停状态,将控制权交给compute() -第二层协程
4. 第二层运行到 await 处,再次进入暂停, 会将控制器释放, 交给task, task再会报状态给loop,loop再去分配执行其他的task
5. 等到sleep 事件过了, loop 检测到可以执行的情况,会继续执行其任务, 然后完成调度
"""


async def compute():
	print("compute start")
	await asyncio.sleep(2)
	print("sleep over")
	return 1 + 2


async def print_sum():
	sum_ = await compute()
	print(sum_)


if __name__ == '__main__':
	import time

	s_t = time.time()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(print_sum())
	print(time.time() - s_t)
