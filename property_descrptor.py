class Value:
    def __init__(self, name: int):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            pass
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class TargetClass:
    value = Value(10)

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    t = TargetClass(10)
    print(t.value)
