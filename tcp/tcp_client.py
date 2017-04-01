#! /usr/bin/env python
# -*- coding: utf-8 -*-

'A client which send data to server.'

import socket

#建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.14.209.232', 9999))

#接受欢迎消息
print s.recv(1024)
for data in ['Tom', 'Jerry', 'sosan', '崔军明', '崔奥博', '崔奥冰','李彦']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
