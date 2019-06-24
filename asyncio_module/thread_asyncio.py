"""
@author: tony-tan
@time: 2019/6/21 14:34
@file: thread_asyncio.py
@site: 
@describe: 多线程模式的async-io  # 协程里面使用多线程
"""
# 在协程中集成阻塞IO,可以使用协程集成多线程模式解决
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
import socket
from urllib.parse import urlparse


def get_url(url):
	# 通过socket 请求一个http 页面数据
	url = urlparse(url)
	host = url.netloc
	path = url.path
	if path == "":
		path = "/"
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp 请求
	client.connect((host, 80))
	client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
	# time.sleep(1)
	data = b""
	while True:
		d = client.recv(1024)
		if d:
			data += d
		else:
			break
	data = data.decode("utf-8")
	html_data = data.split("\r\n\r\n")[1]
	print(html_data)
	client.close()


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	executor = ThreadPoolExecutor(10)  # 线程池模式
	tasks = []
	st = time.time()
	for i in range(20):
		url = "http://shop.projectsedu.com/goods/{}/".format(i)
		# get_url(url)
		task = loop.run_in_executor(executor, get_url, url)
		tasks.append(task)
	loop.run_until_complete(asyncio.wait(tasks))
	print(time.time() - st)
