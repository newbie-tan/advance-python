"""python 弱引用"""
import weakref


class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    demo = Demo("tony", 24)
    weak_demo = weakref.ref(demo)
    print(weak_demo().name)
    print(demo)
