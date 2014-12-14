# 一. logging模块常用方法解释

## logger

提供日志接口，供应用代码使用。logger最长用的操作有两类：配置和发送日志消息。

可以通过logging.getLogger(name)获取logger对象，如果不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象。

## handler

将日志记录（log record）发送到合适的目的地（destination），比如文件，socket等。

一个logger对象可以通过addHandler方法添加0到多个handler，每个handler又可以定义不同日志级别，以实现日志分级过滤显示。

## filter

提供一种优雅的方式决定一个日志记录是否发送到handler。

## formatter

指定日志记录输出的具体格式。formatter的构造方法需要两个参数：消息的格式字符串和日期字符串，这两个参数都是可选的。

与log4j类似，logger，handler和日志消息的调用可以有具体的日志级别（Level），只有在日志消息的级别大于logger和handler的级别。
        
        

----
####  微信公众帐号: wirelessqa 
![wirelessqa](../img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----