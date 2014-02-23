# Shell学习总结之逻辑运算符及表达式

## 一. 运算符总结说明

### 1. 条件运算符

运算符号|	代表意义|应用|说明
----|----|----|----
=|等于 |整型或字符串比较: str1 = str2	| 字符串str1 和字符串str2 相等时返回真,如果在[]中，只能是字符串
==|等于 |整型或字符串比较: str1 == str2	| 字符串str1 和字符串str2 相等时返回真,如果在[]中，只能是字符串
!=|不等于 |整型或字符串比较: str1 != str2 |字符串str1和字符串str2不相等时返回真,如果在[]中,只能是字符串
<|小于 |整型或字符串比较: str1 < str2|按字典顺序排序，字符串str1 在字符串str2 之前,在[]中,它表示字符串,如需使用请转义\\<
\>	|	大于 |整型和字符串比较 |在[]中,它表示字符串,如需使用请转义\\>
-eq	|	等于 |整型比较: int1 -eq int2|	如果int1 等于int2，则返回真
-ne	|	不等于|整型比较: int1 -ne int2	|如果int1 不等于int2，则返回真
-lt	|	小于 |整型比较: int1 -lt int2	|如果int1 小于int2，则返回真
-gt	|	大于 |整型比较: int1 -gt int2	|如果int1 大于int2，则返回真
-le	|	小于或等于|整型比较: int1 -le int2	|如果int1 小于等于int2，则返回真
-ge	|	大于或等于 |整型比较: int1 -ge int2	|如果int1 大于等于int2，则返回真
-z	|	空字符串|字符串比较: -z string	|字符串string 为空串(长度为0)时返回真
-n	|	非空字符串|字符串比较 :-n string	|字符串string 为非空串时返回真

### 2. 逻辑运算符
运算符号|	代表意义|应用|说明
----|----|----|----|----
-a	|	双方都成立（and） |逻辑表达式 –a 逻辑表达式|在[] 表达式中使用
-o	|	单方成立（or）| 逻辑表达式 –o 逻辑表达式|在[] 表达式中使用
!	|逻辑否，条件为假，结果为真。|
&&	|双方都成立（and）|逻辑表达式 && 逻辑表达式|在[[]] 表达式中使用
\|\||单方成立（or）	|逻辑表达式 \|\| 逻辑表达式|在[[]] 表达式中使用



### 3. 文件和目录的判断
逻辑符号|代表意义|应用|说明
----|----|----|----
-f |判断文件是否存在|-f filename	|当filename 存在并且是正规文件时返回真
-d |判断目录是否存在|-d pathname	|当pathname 存在并且是一个目录时返回真
-b |判断是否为一个【block档案】|-b filename	|当filename 存在并且是块文件时返回真(返回0)
-c |判断是否为一个[character档案]|-c filename	|当filename 存在并且是字符文件时返回真
-S |判断是否为一个[socket 标签档案]|-S filename|当filename 存在并且是socket 时返回真
-L |判断是否为一个[symbolic link 的档案]|-L filename	|当filename 存在并且是符号链接文件时返回真
-e |判断【某个东西】是否存在|-e pathname|当由pathname 指定的文件或目录存在时返回真


### 4. 程序的逻辑卷标判断
逻辑符号|代表意义|应用|说明
----|----|----|----
-G	|判断是否由 GID 所执行的程序所拥有|-G pathname	|当由pathname 存在并且属于当前进程的有效用户id 的用户的用户组时返回真
-O	|判断是否由 UID 所执行的程序所拥有|-O pathname	|当由pathname 存在并且被当前进程的有效用户id 的用户拥有时返回真(字母O 大写)
-p	|判断是否为程序间传送信息的 name pipe 或是 FIFO|-p filename|	当filename 存在并且是命名管道时返回真

### 5. 档案的属性判断

逻辑符号|代表意义|应用|说明
----|----|----|----
-r	|判断是否为可读的属性|-r pathname	|当由pathname 指定的文件或目录存在并且可读时返回真
-w	|判断是否为可以写入的属性|-w pathname	|当由pathname 指定的文件或目录存在并且可写时返回真
-x	|判断是否为可执行的属性|-x pathname	|当由pathname 指定的文件或目录存在并且可执行时返回真
-s	|判断是否为『非空白档案』|-s filename	|当filename 存在并且文件大小大于0 时返回真
-u	|判断是否具有『 SUID 』的属性|-u pathname	|当由pathname 指定的文件或目录存在并且设置了SUID 位时返回真
-g	|判断是否具有『 SGID 』的属性|-g pathname	|当由pathname 指定的文件或目录存在并且设置了SGID 位时返回真
-k	|判断是否具有『 sticky bit 』的属性|-k pathname|	当由pathname 指定的文件或目录存在并且设置了"粘滞"位时返回真

### 6.两个档案之间的判断与比较

逻辑符号|代表意义|应用|说明
----|----|----|----
-nt	|第一个档案比第二个档案新|file1 -nt file2	|file1 比file2 新时返回真
-ot	|第一个档案比第二个档案旧|file1 -ot file2	|file1 比file2 旧时返回真
-ef	|第一个档案与第二个档案为同一个档案（ link 之类的档案）|f1 -ef f2|	files f1 and f2 are hard links to the same file

## 二. 逻辑表达式+运算符举例说明


```
#! bin/bash
# -------------------------------------------------------------------------------
# 文件名:  Shell学习总结之逻辑运算符及表达式.sh
# 版 本:   1.0
# 创建日期: 2014/02/23
# 描 述:   逻辑运算符和逻辑表达式学习总结
# 作 者:   毕小朋
# 邮 箱:   wirelessqa.me@gmail.com
# 博 客:   http://blog.csdn.net/wirelessqa
# -------------------------------------------------------------------------------

website="http://blog.csdn.net/wirelessqa"
myname="bixiaopeng"

echo "========= 逻辑表达式 test ========="
#注意：所有字符与逻辑运算符直接用“空格”分开，不能连到一起。
if test 3 -eq 3 -a 3 == 3 ;then echo "true" ;fi

#当3 大于 2 或 4 大于 3 并且 bxp 不等于 bixiaopeng  或 变量website不为空时,为真
if test 3 > 2 -a 4 -gt 2 -a "bxp" != "bixiaopeng" -o -n "$website" ;then echo "true"; else echo "false"; fi

#判断文件是否存在
if test -f "/Users/bixiaopeng/justtest.txt" ;then echo "true"; else echo "false"; fi
#判断目录是否存在
if test -d "/Users/bixiaopeng" ;then echo "true"; else echo "false"; fi

echo "========= 逻辑表达式 [] ========="

#在[] 表达式中，常见的>,<需要加转义字符，表示字符串大小比较，以acill码位置作为比较。
#不直接支持<>运算符，还有逻辑运算符 || 和 && 它需要用-a[and] –o[or]表示。
if [ 3 -eq 3 -a 3 == 3 ];then echo "true" ;fi

#当3 大于 2 或 4 大于 3 并且 bxp 不等于 bixiaopeng  或 变量website不为空时,为真
if [ 3 \> 2 -a 4 -gt 2 -a "bxp" != "bixiaopeng" -o -n "$website" ] ;then echo "true"; else echo "false"; fi

#判断文件是否存在
if [ -f "/Users/bixiaopeng/justtest.txt" ] ;then echo "true"; else echo "false"; fi
#判断目录是否存在
if [ -d "/Users/bixiaopeng" ] ;then echo "true"; else echo "false"; fi

echo "========= 逻辑表达式 [[]] ========="

#[[]] 运算符只是[]运算符的扩充。能够支持<,>符号运算不需要转义符，它还是以字符串比较大小。里面支持逻辑运算符 || 和 &&
if [[ 3 -eq 3 && 3 == 3 ]];then echo "true" ;fi

#当3 大于 2 或 4 大于 3 并且 bxp 不等于 bixiaopeng  或 变量website不为空时,为真
if [[ 3 > 2 && 4 -gt 2 && "bxp" != "bixiaopeng" || -n "$website" ]] ;then echo "true"; else echo "false"; fi

#判断文件是否存在
if [[ -f "/Users/bixiaopeng/justtest.txt" ]] ;then echo "true"; else echo "false"; fi
#判断目录是否存在
if [[ -d "/Users/bixiaopeng" ]] ;then echo "true"; else echo "false"; fi

#[[]] 中可以使用通配符,不需要引号
[[ $myname = b*peng ]] && echo "true"

```
----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----