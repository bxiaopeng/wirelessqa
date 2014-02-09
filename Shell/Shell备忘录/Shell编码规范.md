## Shell代码规范


```
作   者: 毕小朋
用   途: 规范Shell代码书写，方便查看与修改
博   客: http://blog.csdn.net/wirelessqa
参   考: 
http://www.ohlinux.com/archives/191/
http://kodango.com/shell-script-style
```

#### 关于注释

程序头应加注版本与功能说明的注释。但程序第一行不能汉字。

程序体中应包含必要的注释，注释说明如下：

单行注释，可以放在代码行的尾部或代码行的上部；

多行注释，用于注解复杂的功能说明，可以放在程序体中，也可以放在代码块的开始部分

代码修改时，对修改的内容要加必要版本注释及功能说明。


#### 命名约定

```
1.本文档的命名约定是系统配置文件、脚本文件；

2.文件名、变量名、函数名不超过20个字符；

3.命名只能使用英文字母，数字和下划线，只有一个英文单词时使用全拼，有多个单词时，使用下划线分隔，长度较长时，可以取单词前3～4个字母。

4.文件名全部以小写命名，不能大小写混用（通过U盘交换文件时，大小写可能会丢失，即：大写文件名可能会全部变成小写文件名）；

5.避免使用Linux的保留字如true、关键字如PWD等（见附表）；

6.从配置文件导出配置时，要注意过滤空行和注释

```

#### 函数约定

函数名称应该采用小写的形式，并且有一个很好的意义。函数名称应该容易让人理解，比如f1这个名称虽然容易输入但是对调试和其它人阅读代码造成了很大的困难，它说明不了任何东西。好的函数名称可以帮助说明代码，而不需要额外的注释。

一个或多或少有趣的是：如果你无意这样做，不要把函数名称命名为常见的命令名，新手往往比较容易将脚本或者函数名命名成test，这样就和UNIX的test命令冲突了。

* 除非绝对必要，仅使用字母、数字和下划线作为函数名称。

* 每个函数控制在50－100行，超出行数建议分成两个函数

* 多次反复调用的程序最好分成函数，可以简化程序，使程序条理更清楚


* 所有函数定义应该在脚本主要代码执行之前，这样可以给人全局的印象，并且确保所有函数在使用之前它是已知的。

* 你应该使用可移植性高的函数定义形式，即不带function关键字的形式。


#### 代码开头约定

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

####  缩进

由于Shell没有很好的编辑环境，所以，建议用四个空格为基数进行缩进，好处在不同的环境下TAB可能代表的空格数不同，造成代码的错乱。用TAB他的优点是速度快方便，可以在编辑的时候也用TAB，但需要转换。

可以在更改编辑器，Windows的就不说了，主要是VIM

:set softtabstop=4

注意不要使用 :set tabstop=4 上面那个是同时把这一个TAB转换为四个空格，而这一条是定义TAB为四个空格，如果到其它编辑器上就会看到默认8个空格的情况，那就会不美观了。

另外将原有的TAB转换为空格，:retab

如果想让刚才的配置永久生效需要改动vim的配置文件 vim ~/.vimrc,更多详细的有用的配置见“VIM配置总结”

#### 分隔长行

每行不要超过80字，如果超出，建议用“\”折行，有管道的命令行除外。

如果需要分隔过长的代码，你可以使用下面的任意一种方法：

1） 使用与命令宽度相同的缩进

```
activate some_very_long_option \
         some_other_option
```

2） 使用2个空格缩进

```
activate some_very_long_option \
  some_other_option
```
从个人的角度来说，除非有特别的需要，我更倾向于第一种形式，因为它突出“上下两行的内容是一起的”这一联系。


#### 分离复合命令

译者注：其实这里的复合命令就是指块语句，例如for/while循环, if分支结构等等。

```
HEAD_KEYWORD parameters; BODY_BEGIN
  BODY_COMMANDS
BODY_END
```
我习惯于：

* 将HEAD_KEYWORD和初始化命令或者参数放在第一行；
* 将BODY_BEGIN同样放在第一行；
* 复合命令中的BODY部分以2个空格缩进；
* BODY_END部分独立一行放在最后；

```
1）if/then/elif/else分支语句

if ...; then
  ...
elif ...; then
  ...
else
  ...
fi
2）for循环

for f in /etc/*; do
  ...
done
3） while/until循环

while [[ $answer != [YyNn] ]]; do
  ...
done
4） case分支语句

case $input in
  hello)
    echo "You said hello"
  ;;
  bye)
    echo "You said bye"
    if foo; then
      bar
    fi
  ;;
  *)
    echo "You said something weird..."
  ;;
esac
```

几点注意的地方：

* 如果不是100%需要，匹配部分左右的括号不需要写（译者注：例如写成hello)而不是(hello)）；
* 匹配模式与分支的终止符号;;位于同一缩进级别
* 分支内部的命令多缩进一层；
* 尽管是可选的，这里还是把最后一个分支的终止符号也写上了；

#### 参数展开

除非你知道自己做的事情，请在参数展开的地方使用双引号

当然，也有一些地方并不需要使用双引号，例如：

* [[ ]]测试表达式内部是不会展开的；
* 在case $WORD in语法中WORD也不会展开的；
* 在变量赋值var=$WORD的地方也是不会展开的
但是在这些地方使用引号并不会出错，如果你习惯于在每个可能展开参数的地方使用引号，你写得代码会很安全。

如果你要传递一个参数作为一个单词列表，你可以不使用引号，例如：

```
list="one two three"

# you MUST NOT quote $list here
for word in $list; do
  ...
done
```


#### 命令替换

正如文章the article about command substitution [Bash Hackers Wiki]中提及的，你应该使用$( .. )形式。

不过，如果可移植性是一个问题，你可能必须使用反引号的形式`...`。

在任何情况，如果其它展开或者单词分隔并不是你期望的，你应该将命令替换用双引号引起来。

#### 环境变量

变量：全部是大写字母

变量引用：全部以变量名加双引号引用，如”$TERMTYPE”，或“${TERMTYPE}”，如果变量类型是数值型不引用，如:

如果需要从配置文件导出变量，则在变量前加一大写字母，以识别导出变量与自定义环境变量的区别，如：

变量值的引用尽量以$开头，如$(ls inst_*.sh)，避免使用`ls inst_*。sh`

循环控制变量可以命名为单个字母， 比如 i、j等。 也可以是更有意义的名称， 比如 UserIndex。

环境变量和全局变量 在脚本开头定义。

函数中使用较多的文件，以环境变量的形式在文件开头定义，仅函数中使用的变量在函数开头定义

#### 配置变量

在这里，我将这一类变量——可以被用户更改的——叫做配置变量。

让这类变量容易找到，一般放在脚本的头部，给它们有意义的名称并且加上注释说明。正如上面说的，仅当你知道你为什么这么做的时候，才用大写的变量名形式，否则小写形式更加安全。

#### 语句

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


#### 脚本的基本结构

一个脚本的基本结构是这样的：

```

#!SHEBANG

CONFIGURATION_VARIABLES

FUNCTION_DEFINITIONS

MAIN_CODE
Shebang
```
如果可能，请不要忘记shebang。

请小心使用/bin/sh作为shebang，在Linux系统中，/bin/sh就是Bash这是一个错误的观点。

于我而言，shebang有两个目的：

* 说明直接执行时以哪个解释器来执行；
* 明确该脚本应该以哪个解释器来执行；

#### 脚本行为和健壮性

当脚本检测到问题时尽早退出，以免执行潜在的问题；
如果你需要用到的命令可能并没有安装在系统上，在脚本执行的时候最好检查命令是否存在并且提醒用户缺少什么；
采用有意义的脚本返回值，例如0代码成功，1代码错误或者失败；

#### 其它

##### 输出内容

if the script is interactive, if it works for you and if you think this is a nice feature, you can try to save the terminal content and restore it after execution；（译者注：不理解这一点是什么意思）
在屏幕中输出简单易理解的消息；
使用颜色或者特别的前缀区分错误和警告信息；
输出正常的内容到STDOUT，而输出错误、警告或者诊断的信息到STDERR；
在日志文件中输出所有详细的信息；

##### 输入

不要盲目地假设任何事情，如果你希望用户输入一个数字，请在脚本中主动检查它是否真得是一个数字，检查头部是否包含0，等等。我们都应该知道这一点，用户仅仅是用户而不是程序员，他们会做他们想要的，而不是程序想要的。


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
