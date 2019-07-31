"""简单实现pydantic 里面的base_model"""
from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' + str(self._expected_type))
        instance.__dict__[self._name] = value


class List(Typed):
    _expected_type = list


class Integer(Typed):
    _expected_type = int


class OrderedMeta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        d = dict(cls_dict)
        order = []
        for name, value in cls_dict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d["_order"] = order
        return type.__new__(cls, cls_name, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()


class BaseModel(metaclass=OrderedMeta):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __new__(cls, *args, **kwargs):
        annotate = cls.__dict__["__annotations__"]
        for k, v in kwargs.items():
            if not isinstance(v, annotate[k]):
                raise TypeError("expect {0} , but got {1}".format(annotate[k], type(v)))

        return super().__new__(cls)


class Schema(BaseModel):
    age: int
    name: str


if __name__ == '__main__':
    a = Schema(age=1, name=1)
    print(a.name)
