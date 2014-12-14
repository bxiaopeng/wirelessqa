# Linux学习总结之文件类型

在Linux系统中，无论是常见的数据文件、可执行文件，还是一个目录，甚至设备都以文件的形式存在。正因如此，文件在文件系统中的类型也是多样的。

### 1. 文件类型缩写及别称
文件类型的缩写、翻译及别称

文件类型	| 缩写	| 英文	 |其他名称
------|------|------|------
普通文件|	 -	 |Regular file	|
目录文件|	 d	 |Directory file|	
块特殊文件	 |b	 |Block special file|	 块设备文件
字符设备文件	 |c	| Character special file	 |字符设备文件
先进先出	| p	 |FIFO	 |named pipe，命名管道
套接字文件	 |s|	 Socket	|
符号链接|	 l|	 Symbolic link	 |软链接

### 2. 各文件类型简介
各文件类型的主要含义如下：

#### 普通文件(Regular file)
普通意义上的文件，如数据文件、可执行文件等。
#### 目录文件(Directory file)
Linux中目录也是一种文件。目录文件包括了文件夹中所有文件的名字和在分区中的位置。目录文件的权限意义也较特殊，参见文件权限。
#### 块设备文件(Block special file)
一种提供带缓冲的固定大小单元读写的设备文件。如硬盘设备(/dev/sda)及硬盘分区(/dev/hda1)等。
字符设备文件(Character special file)
此种类型文件提供无缓存的变长单元读写。一个设备如果不是块设备，就是字符设备。
#### 命名管道(named pipe或FIFO)
用于系统进程间通信的文件。
#### 套接字文件(Socket)
进程之前通过网络进行通信的文件。多数网络连接都是用Socket建立的。
#### 符号链接(Symbolic link)
此种文件仅是一个链接，详情请参见符号链接。

### 3. 查看文件的类型

ls -l
显示的结果中每行的第一个字符就是文件类型。

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ ls -l
total 16
drwxr-xr-x   3 bixiaopeng  staff   102  1 15 09:49 Applications
drwx------+ 11 bixiaopeng  staff   374  2 16 14:20 Desktop
-rw-r--r--   1 bixiaopeng  staff  1995  1 25 01:13 sm.sh
lrwxr-xr-x     1 root  wheel      3 10 24 11:24 X11R6 -> X11

```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----
