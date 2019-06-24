"""
@author: tony-tan
@time: 2019/6/20 15:55
@file: async_await.py
@site: 
@describe: pass
"""
from collections import Awaitable
from asyncio import coroutine


async def downloader(url):
	return "tony"


async def download_url(url):
	html = await downloader(url)
	return html


async def download_html():
	html = await download_url("http://www.baidu.com")
	print(html)


if __name__ == '__main__':
	coro = download_html()
	try:
		name = coro.send(None)
	except StopIteration:
		pass
