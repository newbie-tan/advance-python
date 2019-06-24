"""
@author: tony-tan
@time: 2019/6/13 16:37
@file: __init__.py.py
@site: 
@describe: python 的一些魔法函数的知识  可认为是pvm 的一些实现协议
"""


class MagicFunctions:

	# 类创建相关
	def __init__(self):
		"""初始化函数,初始化对象的基础属性等"""
		pass

	def __new__(cls, *args, **kwargs):
		"""构造函数"""
		pass

	# 字符串相关表示
	def __repr__(self):
		"""提供给供解释器查看的字符串转换,输出到终端是带有‘’ 的"""
		pass

	def __str__(self):
		"""用于给人查看的字符串输出"""
		pass

	# 集合与序列相关的
	def __len__(self):
		"""求长"""
		pass

	def __getitem__(self, item):
		"""获取元素,可以替代len/iter 等实现, 基本所有序列获取元素的实现"""
		pass

	def __setitem__(self, key, value):
		"""设置某个key 对应的值,可以为index"""
		pass

	def __delitem__(self, key):
		"""删除某个key 对应的值,可以为index"""
		pass

	def __contains__(self, item):
		"""bool 返回, in/not in 的支撑"""
		pass

	# 迭代相关
	def __iter__(self):
		"""成为一个可迭代对象"""
		pass

	def __next__(self):
		"""依次迭代值,生成器作用"""
		pass

	# 可调用
	def __call__(self, *args, **kwargs):
		"""callable 实现
			class A:
				def __call__(self,*args,**kwargs):
					pass
			a = A()
			b = a()
		"""
		pass

	# with 上下文管理器
	def __enter__(self):
		"""上下文实现的管理入口"""
		pass

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""上下文管理器关闭出口"""
		pass

	# 数值转换
	def __abs__(self):
		"""绝对值"""
		pass

	def __bool__(self):
		"""boolean 转换"""
		pass

	def __int__(self):
		"""int 转换"""
		pass

	def __float__(self):
		pass

	def __hash__(self):
		"""可哈希-hashable 并且返回hash值"""
		pass

	def __index__(self):
		"""返回下标"""
		pass

	# 属性相关
	def __getattr__(self, item):
		"""通过属性名获取对象属性"""
		pass

	def __setattr__(self, key, value):
		"""设置属性"""
		pass

	def __getattribute__(self, item):
		"""获取属性"""
		pass


if __name__ == '__main__':
	print(repr("hello world"))
