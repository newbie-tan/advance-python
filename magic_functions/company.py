"""
@author: tony-tan
@time: 2019/6/13 16:38
@file: company.py
@site: 
@describe: test
"""

from typing import List


class Company:
	def __init__(self, employs: List):
		self.employs = employs

	def __getitem__(self, item):
		return self.employs[item]


alibaba = Company(["tony", "jim", "mark"])

for em in alibaba:
	print(em)
