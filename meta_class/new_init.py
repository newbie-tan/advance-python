"""
@author: tony-tan
@time: 2019/6/15 17:37
@file: new_init.py
@site: 
@describe: python 的new 和init 这两个函数的区别
"""


class User:
	def __init__(self):
		"""控制对象的属性的初始化"""
		print("init")
		self.name = "tony"

	def __new__(cls, *args, **kwargs):
		"""控制对象的生成"""
		print("new")
		return super().__new__(cls, *args, **kwargs)


if __name__ == '__main__':
	user = User()
