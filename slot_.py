import pickle


class SlotDemo:
    __slots__ = ["name", "age"]

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


class NoSlotDemo:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


if __name__ == '__main__':
    slot_demo = SlotDemo("tony", 21)
    no_slot_demo = NoSlotDemo("tony", 21)
    print(dir(no_slot_demo))
    print(dir(slot_demo))