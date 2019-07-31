class LazyProperty:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):

        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Demo:

    def __init__(self, order_id):
        self.loan_order_id = order_id

    @LazyProperty
    def name(self):
        first = "tony"
        middle = "tan"
        last = "tony"
        print("text")
        return first + middle + last


if __name__ == '__main__':
    demo = Demo(order_id=123)

    print(demo.name)
    print(demo.name)
    print(demo.name)
    del demo
    print(demo.name)
    print(demo.name)
