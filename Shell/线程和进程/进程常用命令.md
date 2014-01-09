## 运行
#### 同时运行多个shell命令



`cmd1 & cmd2 & cmd3`

**说明：** <br/>
当在后台运行程序时，是将keyboard input和所执行的命令分离，shell并不等待命令执行结束就可以接收新的命令，后台命令的输出仍然后显示到屏幕上面。<br/>
**因此我们需要在命令后放一个'&',使得命令在后台运行**







## 查看
#### 查看进程

`ps`

***例子：***

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ ps |grep eclipse
55128 ttys004    0:00.00 grep --color=always eclipse
10709 ttys008  106:07.58 /Users/bixiaopeng/DevelopSoft/eclipse/Eclipse.app/Contents/MacOS/eclipse
```


#### 干掉进程

`kill -9 pid`

-9表示强迫进程立即停止



