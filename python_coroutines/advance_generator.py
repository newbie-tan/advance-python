"""
@author: tony-tan
@time: 2019/6/19 19:05
@file: advance_generator.py
@site: 
@describe: 生成器进阶
"""


def gen_func():
	# 1. 可以产出值  2.可以接受值(调用方法传递进来的值)
	html = yield "http://projectsedu.com"
	yield 2
	yield 3
	yield 4
	return


# 1. 生产器不止可以产出,还可以接受值


if __name__ == '__main__':
	gen = gen_func()
	url = gen.send(None)
	# 1. 启动生成器的方式有两种, next(), send()
	# url = next(gen)  # 第一次产出值
	html = "tony"
	print(gen.send(html))  # send方法可以传递值进入生成器内部, 同时可以重启生成器执行到下一步
	gen.close()
	print("bobby")
