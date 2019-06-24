"""
@author: tony-tan
@time: 2019/6/14 9:59
@file: private.py
@site: 
@describe: 私有属性和方法
"""


class User:
	__age = 12

	def __init__(self):
		pass

	def __name(self):
		print("hello world")


if __name__ == '__main__':
	user = User()
	print(user._User__age)
