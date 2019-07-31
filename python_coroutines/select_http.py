"""
@author: tony-tan
@time: 2019/6/18 21:31
@file: select_http.py
@site: 
@describe: 使用select 完成http请求
"""

"""
select+回调+ 事件循环 流程讲解
1. 创建socket 客户端
2. 将socket 注册到select事件循环器中(register),主要注册文件句柄+读/写事件模式+回调函数
3. selector 内部封住这些参数为一个namedtuple对象
4. 编写对应的读/写回调函数
5. 编写事件循环器, 事件循环器不断轮询是否有读/写就绪的socket,有就通过封装的namedtuple对象执行其回调函数

"""
import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
from urllib.parse import urlparse

selector = DefaultSelector()  # 可以选择io复用的方法

# 全局一个置位符
stop = False  # 解决windows 下由于select第2、3个参数为空列表导致OsError问题
urls = []


class Fetcher:
    """
    selector 包包装了select函数，内部提供了DefaultSelector类，提供不同平台IO复用的方法,

    """

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/" 
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp 请求
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass

        # 注册register socket 到select 里面
        # file_obj文件句柄/描述符 -> socket.fileno,注册到selector 里面，然后让selector监听这个文件描述符
        # events: 事件注册: event_read 或者 event_write
        # data->回调函数
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)  # 示例发送数据, 为写事件,往socket 里面写

    def connected(self, key):
        """回调函数: select监听到文件句柄创建连接了,接下来要做取消注册,并且做对应的操作"""
        selector.unregister(key.fd)
        # select 非阻塞无需轮询try-catch,因为已经 创建连接了
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # time.sleep(1)
        selector.register(self.client.fileno(), EVENT_READ, self.read_able)

    def read_able(self, key):
        """回调函数: 监听到有数据返回,可以读数据的时候异步调用的函数"""
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)  # 数据读完了后
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            global stop
            if not urls:
                stop = True


# 回调+事件循环+select(poll/epoll)
def loop():
    """事件循环器"""
    # select 本身不支持register模式的
    # socket 状态变化以后的回调是由程序员来完成的
    # 不断的循环监听, 手动监听已经准备好的文件句柄
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':
    import time

    start_time = time.time()
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()  # 执行事件循环器来驱动回调
    print(time.time() - start_time)
