"""
@author: tony-tan
@time: 2019/6/17 17:42
@file: read_file.py
@site: 
@describe: 大文件读取
"""
## 500G大文件,只有一行的情况下

"""
多行数据可以用
f = open(file)
f.read()
"""


# solution

def read_lines(f, newline):
	buffer = ""  # 创建一个字符串缓冲区
	while True:
		while newline in buffer:
			position = buffer.index(newline)
			yield buffer[:position]
			buffer = buffer
		chunk = f.read(4096*10)
		if not chunk:
			pass

if __name__ == '__main__':
	string = "abcd"
	print(string.index("bd"))
