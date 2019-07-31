"""基于itertools.compress与boolean选择器实现的boolean 过滤器"""

from itertools import compress

a = ["a", "b", "c", "d", "e", "f", "g"]
b = [9, 2, 1, 3, 6, 7, 8]

boolean_result = list(compress(a, [n > 4 for n in b]))
"""
> boolean_selector = [t,f,f,f,t,t,t]

"""
print(boolean_result)

import  typing
