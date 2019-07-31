"""
python built-in operator
"""
from operator import attrgetter, itemgetter

# attrgetter 需要获取属性的时候
# itemgettet 需要对k/v对进行操作的时候

a = [
    {"age": 4},
    {"age": 3},
    {"age": 2},
    {"age": 1}]

a = sorted(a, key=itemgetter("age"))
print(a)
print(a[0])
