"""
@author: tony-tan
@time: 2019/6/14 16:20
@file: contextlib_.py
@site: 
@describe: python 上下文管理器 模块 contextlib
"""
from contextlib import contextmanager


@contextmanager
def connect():
	print("create connect")
	yield {}
	print("close connect")


with connect() as conn:
	print("do something")


