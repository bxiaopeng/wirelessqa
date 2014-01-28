## Shell代码规范


```
作   者: 毕小朋
用   途: 规范Shell代码书写，方便查看与修改
转载时间: 2014.1.12
参   考: http://www.ohlinux.com/archives/191/（大多出自此次处）
```

### 1 概述
#### 1.1 目的

定义Shell脚本命名和编码规范，统一管理Shell脚本，便于自己和别人查看，提高代码书写速度和美观，暂时只对自己进行约束,其它人只供参考。

#### 1.2 概述

本文主要根据Fedora Core 4.0的特点，描述安装脚本、OS初始脚本、补丁制作等方面的代码编写规范，可能大部分还是根据自己的习惯与反复思考后的结果，同样也参考了PHP代码规范等。

#### 1.3 开发工具

shell脚本是个文件，没有开发环境，FC4图形环境下，可用gedit、vi、vim、joe等，推荐使用vim因为这个最通用，他的功能同样是很强大，如果想在图形化下可以用gvim，并将环境设置为sh高亮显示，方法:1）cp /etc/vim/vimrc ~/.vimrc    2) vim ~/.vimrc   去掉”syntax on,并且；Windows下，可用ultraedit。文件保存时，有汉字提示的Shell脚本文件，文件保存时，字符编码必须为GB18030/GBK/GB2132 (UTF-8) 三种格式之一。

### 2 对象命名规范

#### 2.1 命名约定

```
1.本文档的命名约定是系统配置文件、脚本文件；

2.文件名、变量名、函数名不超过20个字符；

3.命名只能使用英文字母，数字和下划线，只有一个英文单词时使用全拼，有多个单词时，使用下划线分隔，长度较长时，可以取单词前3～4个字母。

4.文件名全部以小写命名，不能大小写混用（通过U盘交换文件时，大小写可能会丢失，即：大写文件名可能会全部变成小写文件名）；

5.避免使用Linux的保留字如true、关键字如PWD等（见附表）；

6.从配置文件导出配置时，要注意过滤空行和注释
```

#### 2.2代码开头约定

```
1、第一行一般为调用使用的语言

2、下面要有这个程序名，避免更改文件名为无法找到正确的文件

3、版本号

4、更改后的时间

5、作者相关信息

6、该程序的作用，及注意事项

7、版权与是否开放共享GNU说明

8、最后是各版本的更新简要说明
```

如下面的例子：

```
#!/bin/bash
# -------------------------------------------------------------------------------
# Filename:    check_mem.sh
# Revision:    1.1
# Date:        2009/02/10
# Author:      Ajian
# Email:       ajian521#gmail.com
# Website:     www.ohlinux.com
# Description: Plugin to monitor the memory of the system
# Notes:       This plugin uses the "" command
# -------------------------------------------------------------------------------
# Copyright:   2009 (c) Ajian
# License:     GPL
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# you should have received a copy of the GNU General Public License
# along with this program (or with Nagios);
#
# Credits go to Ethan Galstad for coding Nagios
# If any changes are made to this script, please mail me a copy of the changes
# -------------------------------------------------------------------------------
#Version 1.0
#The first one , can monitor the system memory
#Version 1.1
#Modify the method of the script ,more fast
```

#### 2.3 缩进

由于Shell没有很好的编辑环境，所以，建议用四个空格为基数进行缩进，好处在不同的环境下TAB可能代表的空格数不同，造成代码的错乱。用TAB他的优点是速度快方便，可以在编辑的时候也用TAB，但需要转换。

可以在更改编辑器，Windows的就不说了，主要是VIM

:set softtabstop=4

注意不要使用 :set tabstop=4 上面那个是同时把这一个TAB转换为四个空格，而这一条是定义TAB为四个空格，如果到其它编辑器上就会看到默认8个空格的情况，那就会不美观了。

另外将原有的TAB转换为空格，:retab

如果想让刚才的配置永久生效需要改动vim的配置文件 vim ~/.vimrc,更多详细的有用的配置见“VIM配置总结”

#### 2.4 页宽

每行不要超过80字，如果超出，建议用“\”折行，有管道的命令行除外。

#### 2.5 环境变量

变量：全部是大写字母

变量引用：全部以变量名加双引号引用，如”$TERMTYPE”，或“${TERMTYPE}”，如果变量类型是数值型不引用，如:

如果需要从配置文件导出变量，则在变量前加一大写字母，以识别导出变量与自定义环境变量的区别，如：

变量值的引用尽量以$开头，如$(ls inst_*.sh)，避免使用`ls inst_*。sh`

循环控制变量可以命名为单个字母， 比如 i、j等。 也可以是更有意义的名称， 比如 UserIndex。

环境变量和全局变量 在脚本开头定义。

函数中使用较多的文件，以环境变量的形式在文件开头定义，仅函数中使用的变量在函数开头定义

#### 2.6 函数

函数以动名词形式存储，且第二个单词首字母要大写，如updateConfig()

每个函数控制在50－100行，超出行数建议分成两个函数

多次反复调用的程序最好分成函数，可以简化程序，使程序条理更清楚

#### 2.7 语句

**if 语句**

if/then/else 语句中最可能被执行的部分应该放在 then 子句中， 不太可能被执行的部分应该放在 else 子句中。

如果可能， 尽量不要使用一连串的 if 语句， 而应该以 case 语句替代。

不要使 if 语句嵌套超过5层以上， 尽量以更清楚的代码替代。

**case 语句**

概要

case 语句中的单个子句应该以 case 常数的数字顺序或字母顺序排列。 子句中的执行语句应该尽量保持简单， 一般不要超过4到5行代码。 如果执行语句过于复杂， 应该将它放置在独立的函数中。

case 语句的 *) 子句应该只在正常的默认情况或检测到错误的情况下使用。

格式

case 语句遵循同样的缩进和命名约定。

while 语句

使用 Exit 过程退出 while 循环是不好的; 如果可能， 应该只使用循环条件来结束循环。

while 循环的所有初始化代码应该紧贴在进入 while 循环之前， 不要被其他无关语句分隔开。

循环结束后的处理应该紧跟在循环之后。

**for 语句**

如果需要执行确定次数的增量循环， 应该用 for 语句替代 while 语句。

#### 2.8 信号捕捉

如果在进行重要配置修改时，应捕捉用户按键，如果用户按下Ctrl+C等重要操作终止程序，则调用回退程序，如：

#### 2.9 关于注释

程序头应加注版本与功能说明的注释。但程序第一行不能汉字。

程序体中应包含必要的注释，注释说明如下：

单行注释，可以放在代码行的尾部或代码行的上部；

多行注释，用于注解复杂的功能说明，可以放在程序体中，也可以放在代码块的开始部分

代码修改时，对修改的内容要加必要版本注释及功能说明。

参考资料：借鉴了仙人掌的规范 http://www.linuxdiyf.com/bbs/thread-106301-1-1.html


完整单词	|缩写
--------|--
A | 	 
average|avg
B|	 
back|	bk
background	|bg
break|	brk
buffer|	buf
C	| 
color|	cr,clr
control|	ctrl
D	| 
data	|dat
delete|	del
document	|doc
E	 |
edit|	edt
error|	err
escape|	esc
F	 |
flag|	flg
form|	frm
G|	 
grid|	grd
I	 |
increment|	inc
information	|info
initial|	init
insert|	ins
image|	img
L	| 
lable	|lab
length|	len
list|	lst
library|	lib
M	 |
manager|	mgr,mngr
message|	msg
O|	 
Oracle|	Ora
P|	 
panorama|	pano
password|	pwd
picture|	pic
point|	pt
position|	pos
print|	prn
program	|prg
S|	 
server|	srv
source|	src
statistic	|stat
string	|str
Sybase	|Syb
T	| 
temp|	tmp
text	|txt
U|	 
user|	usr
W	| 
window	|win,wnd
