"""
@author: tony-tan
@time: 2019/6/17 16:07
@file: my_generator.py
@site: 
@describe: python 生成器函数
"""


def gen_funcs():
	yield 1
	name = "tony"
	yield 2
	age = 21
	yield 3
	return None


def foo():
	bar()


def bar():
	pass


if __name__ == '__main__':
	# 生成器对象,在python编译字节码的时候就产生了.
	"""
	python 代码执行的过程: python.exe 会用一个叫做PyEval_EvalFrameEx(C函数)的函数去执行代码中的函数,
						执行函数首先会创建一个栈帧对象(stack frame)
	所有的栈帧都是分配在堆内存上的,这就绝决定了栈帧可以独立于调用者存在
	"""
	import dis

	print(dis.dis(foo))
