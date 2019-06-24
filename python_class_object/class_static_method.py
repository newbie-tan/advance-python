"""
@author: tony-tan
@time: 2019/6/14 9:52
@file: class_static_method.py
@site: 
@describe: 类方法和实例方法的测试
"""


class Test:

	@classmethod
	def say(cls):
		Test.hello()

	@staticmethod
	def hello():
		print("hello world")


if __name__ == '__main__':
	Test.say()
