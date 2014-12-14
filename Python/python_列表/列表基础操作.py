#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         列表基础操作.py
#  Description:  
#
#  Date:         14/12/5 下午3:51
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------

def create_list_empty():
    """
    创建空列表
    :return:
    """
    empty_list = []
    print empty_list


def create_list_repeat():
    """
    创建重复列表
    :return:
    """
    repeat_list = ['a', 'b'] * 3
    print repeat_list  #['a', 'b', 'a', 'b', 'a', 'b']


def create_list_connect():
    """
    连接两个list
    :return:
    """
    print ['a', 'b'] + ['c', 'd'] #['a', 'b', 'c', 'd']


def create_list_str2list():
    """
    字符序列转为列表
    :return:
    """
    print list("abcd") #['a', 'b', 'c', 'd']


def create_list_express():
    """
    表达式生成
    :return:
    """
    print [x for x in range(3)] #[0, 1, 2]

def list_read_by_index():
    """
    按序号读写
    :return:
    """
    l = list("abcd")
    l[1] = 2
    print l #['a', 2, 'c', 'd']


def list_sliced():
    """
    使用切片截取list
    :return:
    """
    l = list(range(10))
    print l[2:-2] #[2, 3, 4, 5, 6, 7]


def list_count():
    """
    统计某个元素在列表中有多少个
    :return:
    """
    l = list("aabbcdefbcdb")
    print l.count("b") #4
    print l.count("d") #2
    print l.count("m") #0

def list_index():
    """
    从指定位置查找元素，返回序号,返回最近的一个序号
    :return:
    """
    l = list("abcabddefg")
    print l.index("b", 2) #4
    print l.index("b", 0) #1


def list_append():
    """
    追加元素到列表
    :return:
    """
    l = list("abc")
    print l #['a', 'b', 'c']
    l.append("d") #['a', 'b', 'c', 'd']
    print l


def list_insert():
    """
    在指定位置插入元素
    :return:
    """
    l = list("abc")
    print l
    l.insert(1, 100)
    print l #['a', 100, 'b', 'c']


def list_merger():
    """
    合并列表
    :return:
    """
    l = list("abc")
    l.extend(range(3)) #['a', 'b', 'c', 0, 1, 2]
    print l
    l.extend("def") #['a', 'b', 'c', 0, 1, 2]
    print l


def list_remove():
    """
    移除第一个指定元素
    :return:
    """
    l = list("abcdeccc")
    l.remove("c")
    print l #['a', 'b', 'd', 'e', 'c', 'c', 'c']


def list_pop():
    """
    弹出指定位置的元素
    :return:
    """
    l = list("abc")
    l.pop(1) #指出b
    print l #['a', 'c']


def list_sort():
    """
    列表内元素排序
    :return:
    """
    print ">>>>>list_sort:"
    l = list("aaabbbccdefgggg")
    l.sort()
    print l #['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'e', 'f', 'g', 'g', 'g', 'g']


def list_revert():
    """
    列表内排序反转
    :return:
    """
    print ">>>>>list_revert:"
    l = list("abcdefg")
    l.reverse()
    print l #['g', 'f', 'e', 'd', 'c', 'b', 'a']


def list_del_repeat_by_set():
    """
    列表去重
    :return:
    """
    l = list("aaabbbccdefgggg")
    l = list(set(l)) #排序会乱掉
    print l #['a', 'c', 'b', 'e', 'd', 'g', 'f']
    l.sort() #重新排序
    print l #['a', 'b', 'c', 'd', 'e', 'f', 'g']
    l.reverse() #反转
    print l #['g', 'f', 'e', 'd', 'c', 'b', 'a']


def list_del_repeat_by_itertools():
    """
    列表去重   itertools.groupby
    :return:
    """
    import itertools
    l = list("aaaaaccccccddddddbbbbbbb")
    l.sort()
    l = itertools.groupby(l)
    for k, g in l:
        print k


def list_del_repeat_byfromkeys():
    """
    去重
    :return:
    """
    l = list("aaaaaccccccddddddbbbbbbb")
    l = {}.fromkeys(l).keys()
    print l #['a', 'c', 'b', 'd']


def list_del_repeat_keep_order():
    """
    去重，保持原有的顺序
    :return:
    """
    print ">>>>>list_del_repeat_keep_order:"
    l = ["a","a","a","d","d","c","b","b"]
    l = list(set(l))
    print l

    # l.sort(key=l.index)
    # print l #['a', 'c', 'b', 'd']



def list_insert_by_biset():
    """
    使用biset插入元素
    :return:
    """
    import bisect
    l = list("adef")
    print l #['a', 'd', 'e', 'f']
    bisect.insort(l, "b")
    print l #['a', 'b', 'd', 'e', 'f']
    bisect.insort(l, "d")
    print l #['a', 'b', 'd', 'd', 'e', 'f']


def main():
    create_list_empty()
    create_list_repeat()
    create_list_connect()
    create_list_str2list()
    create_list_express()
    list_read_by_index()
    list_sliced()
    list_count()
    list_index()
    list_append()
    list_insert()
    list_merger()
    list_remove()
    list_pop()
    list_sort()
    list_del_repeat_by_set()
    list_revert()
    list_insert_by_biset()
    list_del_repeat_by_itertools()
    list_del_repeat_byfromkeys()
    list_del_repeat_keep_order()

if __name__=="__main__":
    main()
