# ython 提供了两个级别访问的网络服务。：
#     低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
#     高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

# Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
# socket.socket([family[, type[, proto]]])
#
# family: 套接字家族可以使AF_UNIX或者AF_INET
# type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
# protocol: 一般不填默认为0.

import socket

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎访问菜鸟教程！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()