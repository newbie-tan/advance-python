"""
@author: tony-tan
@time: 2019/6/13 17:57
@file: abstract_base_class.py
@site: 
@describe: python 的抽象基类
"""
import abc


# from collections import abc


class Company:
	"""
	基于ABC 检查某个类是否具有某种方法
	"""

	def __init__(self):
		pass

	def __len__(self):
		pass


class CacheBase():
	"""
	场景:
		需要强制要求子类实现某些方法
			eg: 定制一个web框架, 集成cache
	实践:
		设计一个抽象基类, 指定之类必须实现一些方法
	"""

	def get(self, key):
		# 实现抽象基类最简单的
		raise NotImplementedError

	def set(self, key, value):
		raise NotImplementedError


class ABCCacheBase(metaclass=abc.ABCMeta):
	"""
	基于abc实现抽象基类，实现向下限制
	"""

	@abc.abstractmethod
	def get(self):
		pass

	@abc.abstractmethod
	def set(self):
		pass


class RedisCache(CacheBase):

	def get(self, key):
		pass

	def set(self, key, value):
		pass


if __name__ == '__main__':
	# from collections.abc import Sized
	#
	# print(isinstance(Company(), Sized))
	a, b, c = [1, 2, 3]
	print(a)
	print(b)
	print(c)
