"""
@author: tony-tan
@time: 2019/6/21 11:36
@file: loop_test_1.py
@site: 
@describe: 事件循环基础的async-io 使用及顺序原理
"""
# 事件循环+生成器/协程驱动(回调)+epoll(io多路复用)

# tornado(实现了web服务器), 可以直接部署(nginx+tornado(驱动问题))

# async-io
import asyncio


async def get_html(url):
    print("start get html")
    await asyncio.sleep(1)
    print("end get html")


if __name__ == '__main__':
    import time

    # 1. 创建事件循环器
    # 2. 将协程任务防止到async-io 调度队列中
    # 3. async-io异步的调度协程任务

    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
