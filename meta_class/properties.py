"""
@author: tony-tan
@time: 2019/6/15 16:28
@file: properties.py
@site: 
@describe: python property编程
"""


class User:
	def __init__(self):
		self._age = None

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		self._age = value

	def __getattr__(self, item):
		"""查找属性时候,在查找不到对应属性名称的时候,会进入到这个函数"""
		pass

	def __getattribute__(self, item):
		"""查找属性的时候, 无条件的查找到这个函数内部"""
		pass


if __name__ == '__main__':
	user = User()
	user.age = 10
	print(user.age)
