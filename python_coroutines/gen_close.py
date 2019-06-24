"""
@author: tony-tan
@time: 2019/6/20 11:03
@file: gen_close.py
@site: 
@describe: 生成器关闭
"""


def gen_func():
	try:
		yield "http://projectsedu.com"
	except BaseException:
		pass
	yield 2
	yield 3
	return "bobby"


if __name__ == '__main__':
	gen = gen_func()
	# gen.throw(Exception, "down load error")  # throw  想到于回调异常
	print(next(gen))
	gen.throw(Exception, "down load error")  # throw  相当于回调异常
