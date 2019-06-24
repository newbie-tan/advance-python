"""
@author: tony-tan
@time: 2019/6/17 14:36
@file: __init__.py.py
@site: 
@describe: python 的迭代器和生成器
"""

'''
迭代器?
	1. 迭代器是访问集合内元素的一种方式,一般用于遍历数据
	2. 迭代器和下标访问不一样, 迭代器不能返回 迭代协议: __iter__
'''
from _collections_abc import Iterator