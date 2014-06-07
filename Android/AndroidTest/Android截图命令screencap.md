# Android截图命令screencap

## 查看帮助命令

```
bixiaopeng@bixiaopeng ~$ adb shell screencap -v
screencap: invalid option -- v
usage: screencap [-hp] [-d display-id] [FILENAME]
   -h: this message
   -p: save the file as a png.
   -d: specify the display id to capture, default 0.
If FILENAME ends with .png it will be saved as a png.
If FILENAME is not given, the results will be printed to stdout.

```
注意: 

如果文件名以.png结尾时，它将保存为png文件

如果文件名没有给出,则结果被会被输出到stdout


## 截图保存到SD卡里再导出

```
$ adb shell screencap -p /sdcard/screen.png
$ adb pull /sdcard/screen.png
$ adb shell rm /sdcard/screen.png
```

这种方法比较麻烦，需要3步：1. 截图保存到sdcard 2.将图片导出 3.删除sdcard中的图片

## 截图直接保存到电脑

```
$ adb shell screencap -p | sed 's/\r$//' > screen.png
```

执行adb shell 将\n转换\r\n, 因此需要用sed删除多余的\r


## 如果直接当命令用还可以用 alias 包裝装起來：

```
$ alias and-screencap="adb shell screencap -p | sed 's/\r$//'"
$ and-screencap > screen.png 
``` 
以后就可以方便的用and-screencap ><FILENAME> 直接将截图保存到电脑上了


----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----