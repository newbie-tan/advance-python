"""内存映射, 实现随机访问内存和更改内存中的数据内容"""
import mmap
import os


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)
