"""
@author: tony-tan
@time: 2019/6/13 18:25
@file: mixin.py
@site:
@describe: mixin 基础用法
"""


# python 新式类的多继承中,父类继承调用顺序是从左到右, 广度优先查找
# python 经典类的多继承中,父类继承调用顺序是从左到右, 深度优先查找


class Display:
	def display(self, message):
		print(message)

	def say(self):
		pass

class LoggerMixin:
	def log(self, message, filename='logfile.txt'):
		with open(filename, 'a') as fh:
			fh.write(message)

	def display(self, message):
		super().display(message)
		self.log(message)


class MySubClass(LoggerMixin, Display):
	def log(self, message):
		super().log(message, filename='subclasslog.txt')


subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")
