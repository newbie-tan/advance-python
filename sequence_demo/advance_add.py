"""
@author: tony-tan
@time: 2019/6/14 16:57
@file: advance_add.py
@site: 
@describe: 增强赋值与普通赋值
"""

# 普通赋值 内存更改
a = [1, 2]
print(id(a))

a = a + [3, 4]
print(id(a))

# 增强赋值

b = [1, 2]
print(id(b))
b += [3, 4]
print(id(b))

a = list()