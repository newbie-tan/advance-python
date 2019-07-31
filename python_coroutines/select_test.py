"""
@author: tony-tan
@time: 2019/6/18 21:21
@file: select_test.py
@site: 
@describe: 通过非阻塞io实现http请求
"""

# 在高并发情况下,连接活跃度不高的情况下,epoll 比select 好
# 并发性不高, 同时连接很活跃情况下,select 比 epoll 要好


# 1. 通过非阻塞io实现http请求
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket 请求一个http 页面数据
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp 请求
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError:
        pass
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except Exception:
            continue
    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    get_url("http://www.baidu.com")
