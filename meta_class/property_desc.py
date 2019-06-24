"""
@author: tony-tan
@time: 2019/6/15 16:54
@file: property_desc.py
@site: 
@describe: python 属性描述符
"""
import numbers


# data describe
class IntField:
	"""
		实现了__get__/__set__/__del__ 的类可以称为属性描述符,
		属性描述符相当于这个类只是用于描述一个属性
	"""

	def __get__(self, instance, owner):
		return self.value

	def __set__(self, instance, value):
		if not isinstance(value, numbers.Integral):
			raise TypeError
		self.value = value

	def __delete__(self, instance):
		pass


class User:
	user = IntField()


if __name__ == '__main__':
	user = User()
	user.user = 30  # 相当于进入了IntField的__set__方法
	print(user.user)
