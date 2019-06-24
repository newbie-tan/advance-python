"""
@author: tony-tan
@time: 2019/6/18 14:29
@file: multi_processing_.py
@site: 
@describe: 多进程编程 多个CPU的调用
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# # 1. 对于耗费CPU的操作,计算密集型多进程优势大
# def fib(n):
# 	if n <= 2:
# 		return 1
# 	return fib(n - 1) + fib(n - 2)
#
#
# if __name__ == '__main__':
# 	with ThreadPoolExecutor(3) as executor:
# 		all_task = []

"""
进程间通信: 1. 队列, queue
		  2. 共享内存 Manager
		  3. 管道 pipe
"""

# 队列: 进程间同步, 性能较差
from multiprocessing import Queue

# queue = Queue(maxsize=5)

# 共享内存
from multiprocessing import Manager

# manager_queue = Manager().Queue()

# 管道
from multiprocessing import Pipe, Process


def producer(pipe):
	"""发送者"""
	pipe.send("tony")


def consumer(pipe):
	print(pipe.recv())


if __name__ == '__main__':
	receive_pipe, send_pipe = Pipe()
	my_prod = Process(target=producer, args=(send_pipe,))
	my_cons = Process(target=consumer, args=(receive_pipe,))

	my_prod.start()
	my_cons.start()

	my_prod.join()
	my_cons.join()
