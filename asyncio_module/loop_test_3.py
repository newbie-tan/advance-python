"""
@author: tony-tan
@time: 2019/6/21 12:19
@file: loop_test_3.py
@site: 
@describe: wait 和 gather的用法
"""
import asyncio
import time


async def get_html(url):
	print("start get html")
	await asyncio.sleep(1)
	print("end get html")


if __name__ == '__main__':
	# gather 和wait 的区别
	# 1. gather
	start_time = time.time()
	loop = asyncio.get_event_loop()
	group_1 = [get_html("http://www.imooc.com") for i in range(10)]
	group_2 = [get_html("http://projectsedu.com") for i in range(10)]
	g_1 = asyncio.gather(*group_1)
	g_2 = asyncio.gather(*group_2)
	loop.run_until_complete(asyncio.gather(g_1, g_2))
	print(time.time() - start_time)
