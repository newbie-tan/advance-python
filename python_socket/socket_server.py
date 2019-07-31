"""
@author: tony-tan
@time: 2019/6/17 20:50
@file: socket_server.py
@site: 
@describe: socket 服务端
"""
import socket
import threading

ALLOW_METHOD = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


def handler_sock(sock_):
    """线程socket 处理程序"""
    while True:
        header = sock_.recv(1024).decode("utf-8")

        header_list = header.split("\r\n")
        method = header_list[0].split(" ")[0]

        if not method in ALLOW_METHOD:
            pass


def raise_400():


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8000))
server.listen()

while True:  # 持续监听
    sock, address = server.accept()  # 为每个连接上来的用户创建一个套接字
    # 分配线程
    socket_thread = threading.Thread(target=handler_sock, args=(sock,))
    socket_thread.start()
