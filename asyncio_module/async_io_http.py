"""
@author: tony-tan
@time: 2019/6/21 14:47
@file: async_io_http.py
@site: 
@describe: async-io  实现http
"""

# async-io目前没有提供http协议的接口, 提供的是最底层的tcp/udp
import socket
import time
from urllib.parse import urlparse
import asyncio


async def get_url(url):
	# 通过socket 请求一个http 页面数据
	url = urlparse(url)
	host = url.netloc
	path = url.path
	if path == "":
		path = "/"
	# 创建socket连接,内部还是selector注册加事件轮询,返回一个读数据流对象和写数据流对象
	reader, writer = await asyncio.open_connection(host, 80)
	writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
	all_lines = []
	async for raw_line in reader:
		data = raw_line.decode("utf-8")
		all_lines.append(data)
	html = "\n".join(all_lines)
	# print(html)
	return html


async def main():
	tasks = []
	for i in range(20):
		tasks.append(asyncio.ensure_future(get_url("http://shop.projectsedu.com/goods/{}/".format(i))))
	for task in asyncio.as_completed(tasks):
		result = await task
		print(result)


if __name__ == '__main__':
	st = time.time()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
	print(time.time() - st)
