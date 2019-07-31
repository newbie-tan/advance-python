"""
@author: tony-tan
@time: 2019/6/15 16:28
@file: __init__.py.py
@site: 
@describe: ***
"""


class ClassMeta(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=ClassMeta):
    def __init__(self):
        print("init")

    def __call__(self, *args, **kwargs):
        print("called class")


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    print(a is b)
