"""
@author: tony-tan
@time: 2019/6/21 15:59
@file: async_io_lock.py
@site: 
@describe: ***
"""
import asyncio
import aiohttp
from asyncio import Lock, Queue

cache = {}
lock = Lock()
queue = Queue(maxsize=10)  # queue = [] 非限流情况下


async def get_stuff(url):
	async with lock:  # async 实现协程上下文
		if url in cache:
			return cache[url]
		stuff = await aiohttp.request("GET", url)
		cache[url] = stuff
		return stuff


# 两个协程同时提交了task

async def parse_stuff():
	stuff = await get_stuff("")


async def use_stuff():
	stuff = await get_stuff("")


if __name__ == '__main__':
	tasks = [parse_stuff(), use_stuff()]
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(tasks))
