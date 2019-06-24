"""
@author: tony-tan
@time: 2019/6/13 17:53
@file: duck.py
@site: 
@describe: python 的鸭子类型
"""


class Extend:

	def __init__(self, items):
		self.items = items

	def __getitem__(self, item):
		return self.items[item]


if __name__ == '__main__':
	"""
		list 对象的extend 接受的 是一个可迭代对象
		实现了iter/getitem这种方法的类,pvm就会认为这是一个可迭代对象了 -- duck
	"""
	list_ = list()
	extend = Extend(["tony", "jim", "kim"])
	list_.extend(extend)
	print(list_)
