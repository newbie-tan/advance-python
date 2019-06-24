"""
@author: tony-tan
@time: 2019/6/21 11:14
@file: __init__.py.py
@site: 
@describe: python 的async-io 模块
"""
"""
async-io
1. 包含各种特定的系统实现模块
2. 传输和协议抽象  # tcp/udp
3. 对TCP, UDP, SSL, 子进程, 延时调用以及其他具体的支持
4. 模仿future模块但是适用于时间循环使用的Feture类
5. 基于yield from 的协议和任务, 可以顺序的方式编写并发代码
6. 必须产生一个产生阻塞的IO调用时,有接口可以将这个事件转移到线程池
7. 模仿了threading模块中的同步原语, 可以用在单线程内的协程之间
"""
