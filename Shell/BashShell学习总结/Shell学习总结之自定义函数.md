#### Shell学习总结之自定义函数.sh

```
#! bin/bash
# -------------------------------------------------------------------------------
# 文件名:  Shell学习总结之自定义函数.sh
# 版 本:   1.0
# 创建日期: 2014/02/12
# 描 述:   shell中可以用户定义函数，然后在脚本中可以随便调用，下面是我总结的自定义函数的一些特性
# 作 者:   毕小朋
# 邮 箱:   wirelessqa.me@gmail.com
# 博 客:   http://blog.csdn.net/wirelessqa
# -------------------------------------------------------------------------------


function get_return_str()
{  
   echo "return \"$1\""
    return $1
}

function get_return_int()
{
    echo "return $(($1+$2))"
    return $(($1+$2))
    
}

function get_no_return()
{
	echo "echo $(($1*2))"
}

#声明全局变量
global_var="website: http://blog.csdn.net/wirelessqa"

function get_global_var()
{
	echo "函数内更改全局变量:global_var=\"name: bixiaopeng\""
	global_var="name: bixiaopeng"
}

function get_local_var()
{
	echo "函数内声明局部变量:local local_var=\"weibo@wirelessqa\""
	local local_var="weibo@wirelessqa"
}

echo "自定义函数需知:"
echo "一.因为shell脚本是逐行运行。不会像其它语言一样先预编译，所以必须在调用函数地方之前，声明函数"
echo "二.各个输入参数直接用空格分隔,命令里面获得参数方法可以通过：$1…$n,$0为脚本名"
echo "三.函数返回值，只能通过$? 系统变量获得"
echo "四.局部变量要特别声明"

echo "================ 测试加return的参数返回值 ================"
echo "注意:1.返回值只能是int,范围在0-255,调用方法和取得返回值之间，不能有任何操作，不然取不到return的值"
echo ""
echo "1. 测试0-255之间的参数返回值"
get_return_int 2 253
echo -e "参数返回值为:$? \n"

echo "2. 测试>255的参数返回值"
get_return_int 10 253
echo -e "参数返回值为:$? \n"

echo "3. 测试<0的参数返回值"
get_return_int -1 -2 
echo -e "参数返回值为:$? \n"

echo "4. 测试参数返回值为字符,会报错"
get_return_str "my name is bixiaopeng" "abc"
echo -e "参数返回值为:$? \n"

echo "================ 测试不加return的参数返回值 ================"
echo "注意:不加return将以最后一条命令运行结果作为返回值,正确为0，错误为1"
echo ""
echo "1. 最后一条命令执行正确，返回值为0"
get_no_return 255
echo -e "参数返回值为:$? \n"

echo "2. 最后一条命令执行不正确，返回值为1"
get_no_return "my name is bixiaopeng"
echo -e "参数返回值为:$? \n"

echo "================ 全局变量 ================ "
echo "global_var=\"website: http://blog.csdn.net/wirelessqa\""
get_global_var
echo "main函数现次调用全局变量: echo \$global_var"
echo $global_var

echo "================ 局部变量 ================ "
get_local_var
echo "main函数现次调用局部变量: echo \$local_var"
echo $local_var


```
#### 运行结果:
```
bixiaopeng@bixiaopengtekiMacBook-Pro Shell备忘录$ bash Shell学习总结之自定义函数.sh
自定义函数需知:
一.因为shell脚本是逐行运行。不会像其它语言一样先预编译，所以必须在调用函数地方之前，声明函数
二.各个输入参数直接用空格分隔,命令里面获得参数方法可以通过：…,Shell自定义函数总结.sh为脚本名
三.函数返回值，只能通过0 系统变量获得
四.局部变量要特别声明
================ 测试加return的参数返回值 ================
注意:1.返回值只能是int,范围在0-255,调用方法和取得返回值之间，不能有任何操作，不然取不到return的值

1. 测试0-255之间的参数返回值
return 255
参数返回值为:255

2. 测试>255的参数返回值
return 263
参数返回值为:7

3. 测试<0的参数返回值
return -3
参数返回值为:253

4. 测试参数返回值为字符,会报错
return "my name is bixiaopeng"
Shell自定义函数总结.sh: line 6: return: my: numeric argument required
参数返回值为:255

================ 测试不加return的参数返回值 ================
注意:不加return将以最后一条命令运行结果作为返回值,正确为0，错误为1

1. 最后一条命令执行正确，返回值为0
echo 510
参数返回值为:0

2. 最后一条命令执行不正确，返回值为1
Shell自定义函数总结.sh: line 18: my name is bixiaopeng*2: syntax error in expression (error token is "name is bixiaopeng*2")
参数返回值为:1

================ 全局变量 ================
global_var="website: http://blog.csdn.net/wirelessqa"
函数内更改全局变量:global_var="name: bixiaopeng"
main函数现次调用全局变量: echo $global_var
name: bixiaopeng
================ 局部变量 ================
函数内声明局部变量:local local_var="weibo@wirelessqa"
main函数现次调用局部变量: echo $local_var

```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----
