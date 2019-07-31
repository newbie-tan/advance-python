"""连接池的实现"""
from threading import Thread, Lock
from queue import Queue

from _queue import Empty

pool = Queue(maxsize=5)


class Conn:

    def __init__(self):
        pass

    def __enter__(self):
        with Lock() as l:
            try:
                result = pool.get(block=False, timeout=1)
                return result
            except Empty:
                print("创建新的连接")
                return Conn()


if __name__ == '__main__':
    pass
