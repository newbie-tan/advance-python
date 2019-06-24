"""
@author: tony-tan
@time: 2019/6/14 16:34
@file: __init__.py.py
@site: 
@describe: python 序列类型知识 集合运算 & | - 与或非
"""
from collections import abc


class Name:
	def __init__(self):
		pass

	def create_self(self):
		cls = type(self)
		print(cls())


if __name__ == '__main__':
	A = dict(one=1)
	dict.fromkeys()
	from collections import defaultdict