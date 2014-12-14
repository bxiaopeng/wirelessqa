#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         元组基础操作.py
#  Description:  
#
#  Date:         14/12/6 下午1:39
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------

"""
元组是什么?
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

t1 = ('a', 'b', 'c', 1, 2)
t2 = "a", "b", "c"
"""


def tuple_create_empty():
    """
    创建空元组
    :return:
    """
    t = ()
    print ">>>>tuple_create_empty: "
    print t #()


def tuple_only_one_element():
    """
    元组中只包含一个元素时，需要在元素后面添加逗号
    :return:
    """
    t = ("a", )
    print ">>>>tuple_only_one_element:"
    print t #('a',)


def tuple_visit():
    """
    元组与字符串类似，下标索引从0开始，可以进行截取，组合等
    :return:
    """
    print ">>>>>tuple_visit: "
    t = ("a", "b", "c", 1, 2)
    print t[0], t[1] #a b
    print t[0:1] #('a',)


def tuple_create_new():
    """
    元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
    :return:
    """
    print ">>>>>tuple_create_new:"
    t = (u"老", u"毕")
    t2 = (u"是", u"帅", u"哥")
    t3 = t + t2
    print t3 #(u'\u8001', u'\u6bd5', u'\u662f', u'\u5e05', u'\u54e5')


def tuple_del_all():
    """
    元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
    :return:
    """
    print ">>>>>tuple_del_all: "
    t = (u"老", u"毕")
    print t
    del t
    print u"删除后: "
    try:
        print t #因为上面删除了,所以这里会报错
    except Exception, e:
        print e

#######################################元组运算符#######################################
#与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。


def tuple_len():
    """
    计算元素个数
    :return:
    """
    print ">>>>>tuple_len:"
    t = ('a', 'b', 'c', 1, 2)
    print len(t) #5


def tuple_copy():
    """
    复制元组
    :return:
    """
    print ">>>>>tuple_copy: "
    print ['bxp'] * 4 #['bxp', 'bxp', 'bxp', 'bxp']
    print ('bxp', ) * 4 #('bxp', 'bxp', 'bxp', 'bxp')
    print ('bxp') * 4 #bxpbxpbxpbxp


def tuple_element_isexsit():
    """
    判断元素是否存在
    :return:
    """
    print ">>>>>tuple_element_isexsit:"
    print "a" in ("a", "b", "c") #True
    print "f" in ("a", "b", "c") #False

def tuple_count_index():
    """
    元素统计 & 元素索引
    :return:
    """
    print ">>>>>tuple_count_index:"
    t = ("a", "b", "a","a","a","a","c")
    print t.count("a") #5
    print t.index("b") #1


def tuple_nametuple():
    """
    标准库另提供了特别的nametuple,可用名字访问元素项
    其实namedtuple并不是元组,而是利用模板动态创建的自定义类型
    :return:
    """
    print ">>>>>tuple_nametuple:"
    from collections import namedtuple
    user = namedtuple("user", "name age") #"name age"之间的空格用来分隔字段名
    u = user("bixiaopeng", 30)
    print u.name #bixiaopeng
    print u.age #30

def tuple_iteration():
    """
    元组迭代
    :return:
    """
    print ">>>>>tuple_iteration:"
    for x in ("a", "b", "c"):print x,


def tuple_compare():
    """
    cmp(tuple1, tuple2)
    如果比较的元素是同类型的,则比较其值,返回结果。
    如果两个元素不是同一种类型,则检查它们是否是数字。
        如果是数字,执行必要的数字强制类型转换,然后比较。
        如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
        否则,通过类型名字的字母顺序进行比较。
    如果有一个列表首先到达末尾,则另一个长一点的列表"大"。
    如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。
    :return:
    """
    print ">>>>>tuple_compare:"
    t1, t2 = (1, 2), (1, 2)
    print cmp(t1, t2) #0
    t1, t2 = (1, 2), (1, 3)
    print cmp(t1, t2) #-1
    t1, t2 = (1, 3), (1, 2)
    print cmp(t1, t2) #1
    t1, t2 = ("a", 3), (1, 2)
    print cmp(t1, t2) #1


def tuple_max_min():
    """
    元组中的最大值
    :return:
    """
    print ">>>>>tuple_max: "
    t = (1, 2, 3, 4, 5)
    print max(t) #5
    print min(t) #4

def list_to_tuple():
    """
    列表转换为元组
    :return:
    """
    print ">>>>>list_to_tuple:"
    l = list("abcdefg")
    print l #['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print tuple(l) #('a', 'b', 'c', 'd', 'e', 'f', 'g')




def main():
    tuple_create_empty()
    tuple_only_one_element()
    tuple_visit()
    tuple_create_new()
    tuple_del_all()
    tuple_len()
    tuple_copy()
    tuple_element_isexsit()
    tuple_iteration()
    tuple_compare()
    tuple_max_min()
    list_to_tuple()
    tuple_count_index()
    tuple_nametuple()

if __name__ == '__main__':
    main()

