"""
@author: tony-tan
@time: 2019/6/18 9:04
@file: socket_http.py
@site: 
@describe:
"""
import socket
from urllib.parse import urlparse
import time


def get_url(url):
	# 通过socket 请求一个http 页面数据
	url = urlparse(url)
	host = url.netloc
	path = url.path
	if path == "":
		path = "/"
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp 请求
	client.connect((host, 80))
	client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
	# time.sleep(1)
	data = b""
	while True:
		d = client.recv(1024)
		if d:
			data += d
		else:
			break
	data = data.decode("utf-8")
	html_data = data.split("\r\n\r\n")[1]
	print(html_data)
	client.close()


if __name__ == '__main__':
	import time

	start_time = time.time()
	urls = []
	for i in range(20):
		get_url("http://shop.projectsedu.com/goods/{}/".format(i))
	print(time.time() - start_time)
