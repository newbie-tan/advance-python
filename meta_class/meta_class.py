"""
@author: tony-tan
@time: 2019/6/15 17:42
@file: meta_class.py
@site: 
@describe: python 的元类
"""


# func create class
def create_class(class_name):
	if class_name == "user":
		class User:
			def __str__(self):
				return "user"

		return User
	elif class_name == "company":
		class Company:
			def __str__(self):
				return "company"

		return Company


def __str__(self):
	return str(self.age)


class MetaClass(type):
	def __new__(cls, *args, **kwargs):
		super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
	"""python 中类的实例化的过程中,会首先寻找metaclass(), 通过meta_class指定区创建对应的类"""
	pass

# typing dynamic create class
# User = type("User", (), {"age": 18, "__str__": __str__})

if __name__ == "__main__":
	user = User()
