"""
@author: tony-tan
@time: 2019/6/17 20:51
@file: socket_client.py
@site: 
@describe: socket client
"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000))
client.send("hello world".encode("utf-8"))
client.close()
