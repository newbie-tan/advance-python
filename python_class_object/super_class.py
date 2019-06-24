"""
@author: tony-tan
@time: 2019/6/14 10:28
@file: super_class.py
@site: 
@describe: python 的super 类, 调用类的MRO 顺序
"""


class A:
	def __init__(self):
		print("A")


class B(A):
	def __init__(self):
		print("B")
		super().__init__()


class C(A):
	def __init__(self):
		print("C")
		super().__init__()


class D(B, C):

	def __init__(self):
		print("D")
		super(D, self).__init__()


if __name__ == '__main__':
	D()
