"""
@author: tony-tan
@time: 2019/6/18 11:26
@file: thread_synchronous.py
@site: 
@describe: python 的线程同步问题
"""
from threading import Lock
import threading

lock = Lock()
total = 0


def add():
	global lock
	global total
	for i in range(10000):
		lock.acquire()
		# lock.acquire()
		total += 1
		lock.release()


def desc():
	global lock
	global total
	for i in range(10000):
		lock.acquire()
		total -= 1
		lock.release()


t1 = threading.Thread(target=add, args=())
t2 = threading.Thread(target=desc, args=())

t1.start()
t2.start()
print(total)
