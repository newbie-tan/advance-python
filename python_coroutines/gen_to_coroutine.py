"""
@author: tony-tan
@time: 2019/6/20 21:35
@file: gen_to_coroutine.py
@site: 
@describe: 生成器实现协程
"""
#
# import inspect
import socket
from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()


def get_socket_data():
	yield "tony"


def downloader(url):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.setblocking(False)

	try:
		client.connect(("127.0.0.1", 80))
	except BlockingIOError:
		pass
	# connect非阻塞,然后注册到文件句柄selector
	selector.register(client.fileno(), EVENT_WRITE, "call_back")
	source = yield from get_socket_data()
	data = source.decode("utf-8")
	html_data = data.split("\r\n\r\n")[1]
	print(html_data)
	return html_data


def download_html():
	"""下载网页的协程"""
	html = yield from downloader("http://www.baidu.com")  # 协程的调度
	print(html)


if __name__ == '__main__':
	# 协程调度 = 事件循环+协程模式
	download_html()
