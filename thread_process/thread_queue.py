"""
@author: tony-tan
@time: 2019/6/18 10:53
@file: thread_queue.py
@site: 
@describe: 线程间通信的方式
"""

# 消息队列通信
import queue
import threading
import time

detail_url_queue = queue.Queue(maxsize=1000)


def get_detail_html(queue_):
	# 具体url 内详情数据

	while True:
		if len(queue_):
			url = queue_.pop()
			print("get detail html started : {url}".format(url=url))
			time.sleep(2)
			print("get detail html end")


def get_detail_url(url):
	# 爬去url 列表
	global detail_url_list
	print("get detail url started")
	time.sleep(2)
	for i in range(20):
		detail_url_list.append("www.baidu.com/{id}".format(id=i))
	print("get detail url end")


if __name__ == '__main__':
	url_thread = threading.Thread(target=get_detail_url, args=("",))
	url_thread.start()
	for i in range(10):
		html_tread = threading.Thread(target=get_detail_html, args=("",))
		html_tread.start()
