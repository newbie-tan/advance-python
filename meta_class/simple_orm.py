"""
@author: tony-tan
@time: 2019/6/17 13:10
@file: simple_orm.py
@site: 
@describe: 实现一个简单的orm功能
"""


class Field:
    pass


class IntField(Field):
    """int 类型的数据描述符"""

    def __init__(self, min_value: int = 0, max_value: int = None, db_column: str = None):
        self._value = None
        self._min_value = min_value
        self._max_value = max_value
        self._db_column = db_column

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value

    def __delete__(self, instance):
        pass


class CharField(Field):
    """字符串类型的 数据描述符"""

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class ModelMetaClass(type):
    def __new__(cls, name, base, attributions, **kwargs):
        """将字段,表名以及元信息等封住到attr属性中去"""
        fields = {k: v for k, v in attributions.items if isinstance(v, Field)}

        _meta = {}
        attr_meta = attributions.get("Meta", None)
        db_table = name
        if attr_meta is not None:
            table = getattr(attr_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attributions["_meta"] = _meta
        attributions["fields"] = fields
        del attributions["Meta"]  # 封住做单独的判断过滤
        return super().__new__(cls, name, base, attributions, **kwargs)


class User(metaclass=ModelMetaClass):
    """元编程的核心,对象的创建交给元类去做"""

    def __init__(self):
        pass

    name = IntField()

    class Meta:
        db_name = "user"
