#! /usr/bin/evn python
# -*- coding: utf-8 -*-
#如果有中文字符,必须加上上面这行声明

import socket

host = ''
port = 51423

#建立一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#将socket设置为可复用的
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
#监听来自客户端的连接，同时设定每次最多只有一个等候处理的连接,真正的服务器会允许一个很高的数字 
s.listen(1)

print "Server is running on port %d;press Ctrl-C to terminate." \
	% port

while 1:
	#当某人客户端连接的时候，accept返回两个信息： clientsock(一个新的连接客户端的socket)和客户端的ip地址、端口号
	clientsock,clientaddr = s.accept()
	clientfile = clientsock.makefile('rw',0)
	#终端上输出
	clientfile.write("welcome, "+ str(clientaddr) + "\n")
	clientfile.write("please enter a string: ")
	#从客户端读一个字符串,显示一个应答
	line = clientfile.readline().strip()
	clientfile.write("You entered %d characters. \n " % len(line))
	clientfile.close()#关闭文件对象
	clientsock.close()#关闭socket对象

'''
#运行结果:
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ telnet localhost 51423
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
welcome, ('127.0.0.1', 49900)
please enter a string: helloxiaopeng
You entered 13 characters.
 Connection closed by foreign host.
'''	