"""
@author: tony-tan
@time: 2019/6/18 9:30
@file: py_gil.py
@site: 
@describe: python 全局解释器锁
"""
import threading

# import dis
# def add(a):
# 	a = a + 1
# 	return a
#
#
# print(dis.dis(add))

TOTAL = 0


def add():
	global TOTAL
	for i in range(100000):
		TOTAL += 1


def desc():
	global TOTAL
	for i in range(100000):
		TOTAL -= 1


t1 = threading.Thread(target=add, args=())
t2 = threading.Thread(target=desc, args=())

t1.start()
t2.start()

t1.join()
t2.join()

""""
gil: 全局解释器锁, 同一时间只有一个线程在一个CPU上运行
gil 会根据执行的字节码的行数及时间片释放，或者在遇到io操作的情况下会主动释放(i/o频繁适用性)
"""

print(TOTAL)
