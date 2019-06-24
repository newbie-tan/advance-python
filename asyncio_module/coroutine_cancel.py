"""
@author: tony-tan
@time: 2019/6/21 13:23
@file: coroutine_cancel.py
@site: 
@describe: 协程的取消
"""
import asyncio
import time


# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()


# 1. loop 会被放到future中(loop 中也放有future)
# 2. 取消future(task)

async def get_html(sleep_times):
	print("waiting")
	await asyncio.sleep(sleep_times)
	print("done after {}s".format(sleep_times))


if __name__ == '__main__':
	t_1 = get_html(3)
	t_2 = get_html(4)
	t_3 = get_html(5)
	tasks = [t_1, t_2, t_3]

	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(asyncio.wait(tasks))
	except KeyboardInterrupt as e:
		all_tasks = asyncio.Task.all_tasks()
		for task in all_tasks:
			print('cancel task')
			print(task.cancel())
		loop.stop()
		loop.run_forever()
	finally:
		loop.close()
