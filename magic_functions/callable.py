"""
@author: tony-tan
@time: 2019/6/13 17:15
@file: callable.py
@site: 
@describe: 可调用 __call__ 测试
"""


class CallAble:
	def __init__(self):
		pass

	def __call__(self, *args, **kwargs):
		print("hello world")


if __name__ == '__main__':
	call_ = CallAble()
	call_()
