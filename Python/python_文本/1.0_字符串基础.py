#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         1.0_字符串基础.py
#  Description:  字符串的一些基础操作
#
#  Date:         14/11/23 下午4:06
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------


def print_line(number=None):
    if number:
        print "------------------------%s-----------------------" %number
    else:
        print "-----------------------------------------------------"


def how2display():
    """
    问题1: Python中文本字符串是如何展现的?
    ##### 2种展现方式: 单引号和双引号 ,两者无区别
    """
    print "my name is bixiaopeng"
    print 'my name is bixiaopeng'

print "---------------------------------------------------------------------------------------------"


def how2wrap():
    """
    问题2: 文本字符串如何换行输出?
    ##### 2种方法: 1. 加换行符\n  2. 三引号引起来
    """
    print "my name is \nbixiaopeng"

    print """my
    name
    is
    bixiaopeng
    """

print "---------------------------------------------------------------------------------------------"


def how2ignore_escape_char():
    """
    问题3: 如何忽略转义字符？
    #### 2种方法: r 或 R
    """
    print "我就是\n不换行"
    print r"我就是\n不换行"
    print R"我就是\n不换行"


def how2get_sigle_char():
    """
    问题4: 如何查看单个字符?
    ##### 通过索引
    """
    str_a = "bi xiao peng"
    print str_a[0]
    print str_a[1]
    print str_a[2]

print "---------------------------------------------------------------------------------------------"


def how2get_part_char():
    """
    问题5: 如何查看部分字符?
    ##### 使用切片
    """
    str_b = "bi xiao peng"
    print str_b[-4:]
    print str_b[3:]
    print str_b[1:8]
    print str_b[1::2] #步长是2,所以结果是ixa eg

print "---------------------------------------------------------------------------------------------"


def how2travel_char():
    """
    问题6: 如何遍历整个字符?
    ##### for循环
    """
    str_b = "bi xiao peng"
    for i in str_b:
        print u"遍历整个字符: %s" %i

print "---------------------------------------------------------------------------------------------"


def how2splice_char():
    """
    问题7: 如何实现字符拼接?
    ##### 两个字符相加
    """
    str_a = "bi xiao peng"
    str_b = "bi xiao peng"
    print u"实现字符拼接: %s" %(str_a + str_b)

print "---------------------------------------------------------------------------------------------"


def how2repeat_char():
    """
    问题8: 如何实现字符串多次重复?
    ##### 字符串*重复次数
    """

    print u"实现字符串重复 %s" %("justtest "* 3)

print "---------------------------------------------------------------------------------------------"


def how2change2list():
    """
    问题9: 字符串如何转成list
    ##### list(字符串)
    """

    list_a = list("laobi")
    print list_a

print "---------------------------------------------------------------------------------------------"


def how2judge_digit():
    """
    问题10: 如何判断字符串全是数字？
    ##### 字符串.isdigit()
    """

    print "123".isdigit()
    print "ab3".isdigit()


def how2change_upper_lower():
    """
    问题11: 如何将字符串转成大写或小写?
    ##### 字符串.upper()  字符串.lower
    """

    print "abc".upper()
    print "ABC".lower()

print "---------------------------------------------------------------------------------------------"


def how2judge_char_display_times():
    """
    问题12: 如何查看字符串中某字符出现的次数？
    ##### 字符串.count('字符')
    """

    print "bixiaopeng".count('i')

print "---------------------------------------------------------------------------------------------"


def how2multichar_change2siglechar():
    """
    问题13: 如何将一个多行字符串分成多个单行,并装入一个列表中?
    ##### 多行字符串.splitlines()
    """

    print "abc\ndef\nghij\nklm".splitlines()

    """
    结果: ['abc', 'def', 'ghij', 'klm']
    """

print "---------------------------------------------------------------------------------------------"


def how2_list2char():
    """
    问题14: 如何将一个列表字符串转成单个字符？
    ##### 分隔符.join(列表字符串)
    """
    s = ['abc', 'def']
    str_now = "iiiiii".join(s)
    print str_now

    """
    结果: abciiiiiidef
    """
print "---------------------------------------------------------------------------------------------"


def how2_char2value():
    """
    问题15: 字符和字符值之间如何转换?
    ##### ord(字符) 、chr(字符值)
    """

    print ord('a') # 97
    print chr(97) # a

print "---------------------------------------------------------------------------------------------"


def how2_judge_obj_is_char():
    """
    问题16: 如何判断一个对象是否是类字符串?
    ##### isinstance and basestring
    """

    # 方法一:
    print isinstance(1, basestring) # False
    print isinstance("a", basestring) #True
    # 方法二:
    print _is_string_like(1) #False
    print _is_string_like("abc") #True

# 方法二:
def _is_string_like(anobj):
    try:anobj + ''
    except: return False
    else: return True


print "---------------------------------------------------------------------------------------------"


def how2align():
    """
    问题17: 如何实现字符串对齐？
    ##### ljust  rjust center
    """

    print "|", u"我".ljust(20), "|", u"是".rjust(20), "|", u"帅哥".center(20), "|"
    #| 我                    |                    是 |          帅哥          |

    #也可以填充字符
    print "|", u"我".ljust(20, "*"), "|", u"是".rjust(20, "%"), "|", u"帅哥".center(20, "#"), "|"
    #| 我******************* | %%%%%%%%%%%%%%%%%%%是 | #########帅哥######### |

print "---------------------------------------------------------------------------------------------"

def how2remove_space():
    """
    问题18: 如何移动字符串两端的空格或字符?
    ##### strip  lstrip  rstrip
    """

    str_c = "  邓丽君  "
    print str_c.strip() #移除两边的空格
    print str_c.lstrip() #移除左边的空格
    print str_c.rstrip() #移除右边的空格

    str_d = "abbbaaa  小朋友  bbaaaa"
    print str_d.strip("ab")#移除两边的字符a和b
    print str_d.lstrip("ab")
    print str_d.rstrip("ab")

print "---------------------------------------------------------------------------------------------"


def how2meger_char():
    """
    问题19: 合并字符串的方法?
    #####
    """

    #将一个字符串列表中的字符拼接成一个字符串
    str_e = {"my", "name", "is", "bixiaopeng"}
    print " ".join(str_e)

    #字符串变量替换
    print u"我是%s" %u"帅哥"

    #直接相加进行字符串拼接
    print "my blog address " + "blog.csdn.net/wirelessqa"

print "---------------------------------------------------------------------------------------------"


def how2reversal():
    """
    问题20: 如何逐字或逐词反转？
    :return:
    """
    astring = "my name is onceler"

    #方法一: 使用步长为-1的切片方法
    print astring[::-1] ##relecno si eman ym

    #方法二: 将字符串分割成字符列表,然后反转,再通过join连接
    revwords = astring.split()
    revwords.reverse()
    revwords = " ".join(revwords)
    print revwords  #onceler is name my

    #方法三: 一行解决法
    print ' '.join(astring.split()[::-1]) #onceler is name my

how2reversal()

print "---------------------------------------------------------------------------------------------"


def _contains_any(seq, aset):
    """
    检查序列seq是否含有aset中的项
    :param seq:
    :param aset:
    :return:
    """

    for c in seq:
        if c in aset:return True
    return False


def _contains_any2(seq, aset):
    """
    检查序列seq是否含有aset中的项
    :param seq:
    :param aset:
    :return:
    """
    import itertools
    for item in itertools.ifilter(aset.__contains__,seq):
        return True
    return False

def how2check_contains():
    """
    问题21: 如何检查字符串中是否包含某字符集合中的字符？
    :return:
    """
    seq = u"老毕是一个帅哥"
    aset = u"老毕"
    #方法一:
    print _contains_any(seq, aset) #True
    print _contains_any(seq, "www.baidu.com") #False
    print _contains_any2(seq, aset) #True
    print _contains_any2(seq, "www.baidu.com") #False

how2check_contains()

print "---------------------------------------------------------------------------------------------"


def _contains_all(seq, aset):
    return not set(aset).difference(seq)


def how2check_contains_all():
    """
    问题22: 如何检查某个序列是否含有另一个序列的所有项?
    :return:
    """
    seq = [1, 2, 3, 3]
    aset = [1, 2, 3, 4]
    print _contains_all(seq, aset) #False
    print _contains_all(seq, [1, 2]) #True

how2check_contains_all()



