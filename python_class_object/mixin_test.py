"""
@author: tony-tan
@time: 2019/6/14 8:53
@file: mixin_test.py
@site: 
@describe: python mixin 模式的测试
"""


class SupClass:
	"""混入类"""

	def display(self):
		self.say()


class SupClassMixin:
	"""直接父类"""

	def say(self):
		print("say something ")


class SubClass(SupClassMixin, SupClass):
	"""用户需要最终实例化并调用的类"""
	pass


if __name__ == '__main__':
	sub_class = SubClass()
	sub_class.display()
