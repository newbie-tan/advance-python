"""
@author: tony-tan
@time: 2019/6/13 17:34
@file: index_.py
@site: 
@describe: __index__ 魔法函数
"""


class Index:
	def __init__(self):
		self.items = [1, 2, 3]

	def __index__(self):
		return self.items.__index__()


if __name__ == '__main__':
	pass
