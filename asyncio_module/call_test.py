"""
@author: tony-tan
@time: 2019/6/21 14:24
@file: call_test.py
@site:
@describe: asyncio 的call
"""
import asyncio


def callback(sleep_time):
	print("sleep {} s".format(sleep_time))


def stop_loop(loop):
	loop.stop()


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.call_soon(callback, 2)
	# loop.call_soon(stop_loop, loop)

	loop.call_later(0, callback, 1)  # 延迟执行
	# loop.call_later(2, callback, 1)
	# loop.call_later(3, callback, 1)
	loop.call_at(loop.time() + 1, callback, 3)  # 指定事件执行,基于内部基准时钟
	loop.call_soon_threadsafe(callback, 2)  # 马上执行线程安全的
	loop.run_forever()
# 1. call_soon 2. call_later(0,,) 3. call_at()
