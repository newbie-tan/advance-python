"""
@author: tony-tan
@time: 2019/6/20 11:23
@file: gen_yield_from.py
@site: 
@describe: 生成器得yield from(py 3.3)  # yield from [iterable] 对象
"""
from itertools import chain


# def my_chain(*arys, **kwargs):
# 	for ary in arys:
# 		# for value in ary:
# 		# 	yield value
# 		yield from ary
#
#
# for i in my_chain([1, 2, 3], range(4, 10)):
# 	print(i)


# def g_1(iterable):
# 	yield iterable
#
#
# def g_2(iterable):
# 	yield from iterable
#
#
# for i in g_1(range(10)):
# 	print(i)
#
# for i in g_2(range(10)):
# 	print(i)
#
#
# def g_1(gen):
# 	yield from gen
#
#
# def main():
# 	g = g_1()
# 	g.send()

# 1. 调用方main  委托生成器g_1 子生成器gen
# yield from 会在调用者于子生成器之间建立双向通道 ,send()/next()


def sub_gen():
	sum = 0
	while True:
		b = yield
		if not b:  # 子生成器抛出
			break
		sum += b
		print(b)
	# 生成器的return 会raise 一个stopIteration 报错,并且会将返回值封住到e.value属性里面
	return sum


def agent_gen():
	res = yield from sub_gen()
	print(res)


def main():
	a_gen = agent_gen()
	a_gen.send(None)
	for i in range(1, 10):
		a_gen.send(i)
	a_gen.send(None)


# try:
# 	res = a_gen.send(None)
# except StopIteration:
# 	pass


if __name__ == '__main__':
	main()
