"""
@author: tony-tan
@time: 2019/6/18 9:42
@file: py_thread.py
@site: 
@describe: 对于IO 来说,多线程与多进程性能差距不大
"""

# 通过
import threading
import time


def get_detail_html(url):
	print("get detail html started")
	time.sleep(2)
	print("get detail html end")


def get_detail_url(url):
	print("get detail url started")
	time.sleep(2)
	print("get detail url end")


class GetDetailHtml(threading.Thread):
	"""通过继承类方式"""
	def __init__(self, name):
		super().__init__(name=name)

	def run(self):
		print("get detail html started")
		time.sleep(2)
		print("get detail html end")


class GetDetailUrl(threading.Thread):
	def __init__(self, name):
		super().__init__(name=name)

	def run(self):
		print("get detail url started")
		time.sleep(2)
		print("get detail url end")


if __name__ == '__main__':
	# t1 = threading.Thread(target=get_detail_html, args=("",))
	# t2 = threading.Thread(target=get_detail_url, args=("",))
	# start_time = time.time()
	#
	# t1.start()
	# t2.start()
	#
	# print("spend time {}".format(time.time() - start_time))
	t1 = GetDetailHtml("GetDetailHtml")
	t2 = GetDetailUrl("GetDetailUrl")
	start_time = time.time()

	t1.start()
	t2.start()
	print("spend time {}".format(time.time() - start_time))