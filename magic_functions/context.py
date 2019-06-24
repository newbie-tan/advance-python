"""
@author: tony-tan
@time: 2019/6/13 17:18
@file: context.py
@site: 
@describe: python 上下文管理器的测试
"""


class Context:
	def __init__(self, name):
		self.name = name

	def __enter__(self):
		# 获取资源
		print("enter")
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		# 释放资源
		print("exit")


class Connect:

	def __init__(self):
		pass

	@classmethod
	def connect(cls):
		return Context("tony")


if __name__ == '__main__':
	with Connect.connect() as context:
		print(context.name)
	print("over")
