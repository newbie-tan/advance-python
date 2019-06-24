"""
@author: tony-tan
@time: 2019/6/19 15:02
@file: python_namedtuple.py
@site: 
@describe: ***
"""
from collections import namedtuple

my_namedtuple = namedtuple("User", ["age", "name"])
obj = my_namedtuple(21, "name")

print(obj.age)

a = [
	{"name": 29},
	{"name": 21},
	{"name": 22},
	{"name": 24}
]

b = sorted(a, key=lambda item: item.get("name"))

print(b)
