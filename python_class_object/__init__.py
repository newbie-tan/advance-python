"""
@author: tony-tan
@time: 2019/6/13 17:53
@file: __init__.py.py
@site: 
@describe: ***
"""


def exec_try():
	try:
		print("hello 1")
		return 1
	except KeyError as e:
		return 2
	else:
		return 3
	finally:
		return 4


if __name__ == '__main__':
	result = exec_try()
	print(result)
