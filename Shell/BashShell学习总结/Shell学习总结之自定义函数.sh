#! bin/bash

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

