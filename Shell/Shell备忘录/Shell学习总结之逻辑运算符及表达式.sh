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
