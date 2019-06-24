"""
@author: tony-tan
@time: 2019/6/18 13:04
@file: thread_semaphore.py
@site: 
@describe: python 信号量锁 : 用于控制进入数量的锁
"""
# 文件的读/写, 写一般只是用于一个线程, 读可以允许有多少
import threading
import time


class HtmlSpider(threading.Thread):
	def __init__(self, url, sem):
		self.url = url
		self.sem = sem
		super().__init__()

	def run(self):
		time.sleep(2)
		print("got html text success")
		self.sem.release()


class UrlProducer(threading.Thread):

	def __init__(self, sem):
		self.sem = sem
		super().__init__()

	def run(self):
		for i in range(20):
			self.sem.acquire()
			html_thread = HtmlSpider("www.baidu,com/{}".format(i), self.sem)
			html_thread.start()


if __name__ == '__main__':
	sem = threading.Semaphore(3)
	url_producer = UrlProducer(sem=sem)
	url_producer.start()
