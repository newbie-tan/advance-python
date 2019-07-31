import os

if __name__ == '__main__':
    fd = os.open("1.txt", os.O_WRONLY | os.O_CREAT)
    f = open(fd, "wt")
    print(f.write("hello world"))
    pass
