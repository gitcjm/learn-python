#! /usr/bin/env python
# -*- coding: utf-8 -*-

'A server example which send hello to client.'

# 导入socket库
import time, socket, threading

def tcplink(sock, addr):
    print 'Accetp new connection from %s:%s...' % addr
    sock.send('Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr
    
#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
s.bind(('10.14.209.232', 9999))
#开始监听
s.listen(5)
print 'Waiting for connection...'

#服务器通过一个永久循环来接受来自客户端的连接
while True:
    #接受一个新连接
    sock, addr = s.accept()
    #创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()