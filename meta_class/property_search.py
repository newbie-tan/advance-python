"""
@author: tony-tan
@time: 2019/6/15 17:24
@file: property_search.py
@site: 
@describe: 属性查找顺序
"""


class Descriptor:
	def __get__(self, instance, owner):
		return self.value

	def __set__(self, instance, value):
		self.value = value


class User:
	name = Descriptor()

	def __init__(self, name):
		self.name = name


if __name__ == "__main__":
	User.name = "tony"
	user = User("mark")
	print("class dict: " + str(User.__dict__) + "\n")
	print("object dict: " + str(user.__dict__) + "\n")
	print(user.name)
