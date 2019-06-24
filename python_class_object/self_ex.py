"""
@author: tony-tan
@time: 2019/6/14 10:07
@file: self_ex.py
@site: 
@describe: python 自省 ，通过一定的机制查询对象自身的内部结构
"""


class Person:
	name = "user"


class User(Person):
	def __init__(self, name):
		self.name = name

	def say(self):
		print(super())
		print("hello world")


if __name__ == '__main__':
	user = User("tony")
	print(user.__class__)
