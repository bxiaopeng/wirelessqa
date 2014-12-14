#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         字典基础操作.py
#  Description:  
#
#  Date:         14/12/6 下午2:54
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------

"""
字典是另一种可变容器模型，且可存储任意类型对象

字典由键和对应值成对组成。字典也被称作关联数组或哈希表。基本语法如下：

dict = {'a': '1', 'b': '2', 'c': '3'}
"""

def dict_create():
    """
    每个键与值用冒号隔开（:），每对用逗号，每对用逗号分割，整体放在花括号中（{}）
    键必须独一无二，但值则不必
    值可以取任何数据类型，但必须是不可变的，如字符串，数或元组
    :return:
    """
    print ">>>>>dict_create:"
    #空字典
    d = {}
    print d

    #普通方式构造
    d1 = {"a":1, "b": 2}
    print d1 #{'a': 1, 'b': 2}
    #构造
    d2 = dict(a=1, b=2)
    print d2 #{'a': 1, 'b': 2}
    #用两个序列类型构造字典
    print dict((["a", 1], ["b", 2])) #{'a': 1, 'b': 2}
    #同上
    print dict(zip("ab", range(2))) #{'a': 0, 'b': 1}
    #同上
    print dict(map(None, "abc", range(2))) #{'a': 0, 'c': None, 'b': 1}
    #用序列做key,并提供默认value
    print dict.fromkeys("abc", 1) #{'a': 1, 'c': 1, 'b': 1}
    #使用生成表达式构造字典
    print {k:v for k, v in zip("abc", range(3))} #{'a': 0, 'c': 2, 'b': 1}

def dict_operate():
    """
    字典基础操作
    :return:
    """
    print ">>>>>dict_operate: "
    print u" #判断是否包含key"
    d = {"a":1, "b":2}
    print "b" in d #True

    print u"#删除k/v"
    d = {"a":1, "b":2}
    del d["b"]
    print d #{'a': 1}

    print u"#合并dict"
    d = {"a": 1}
    d.update({"e": 3})
    print d #{'a': 1, 'e': 3}

    print u"#弹出value"
    d = {"a":1, "b":2}
    d.pop("b")
    print d #{'a': 1}

    #弹出(key value)
    d = {"a":1, "b":2}
    d.popitem()
    print d #{'b': 2}

    d3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
    print u"#修攺已存在的值"
    d3['Age'] = 8 #{'Age': 8, 'Name': 'Zara', 'Class': 'First'}
    print d3
    print u"#增加新字典"
    d3['School'] = "DPS School" #{'Age': 8, 'Name': 'Zara', 'Class': 'First'}
    print d3

    print u"#删除键是Name的条目"
    del d3['Name'] #{'School': 'DPS School', 'Age': 8, 'Class': 'First'}
    print d3

    print u"#清空字典所有条目"
    d3.clear() #{}
    print d3



def dict_default_return():
    """
    默认返回值
    :return:
    """

    #如果没有对应的key,返回None
    d = {"a":1, "b":2}
    print d.get("c") #None
    #如果没有对应的key,返回缺省值
    print d.get("d", 123) #123
    #key存在,返回value
    print d.setdefault("a", 100)#1

    #key不存在，先设置后返回
    print d.setdefault("c", 200) #200

    print d #{'a': 1, 'c': 200, 'b': 2}


def dict_travel():
    """
    字典遍历操作
    :return:
    """
    print ">>>>>dict_travel:"
    d = {"a":1, "b":2}
    #方法一
    print d.keys() #['a', 'b']
    print d.values() #[1, 2]

    #方法二
    print d.items() #[('a', 1), ('b', 2)]
    #方法三
    for k in d :print k, d[k],  #a 1 b 2
    print ""
    #方法四
    for k, v in d.items(): print k,v ,#a 1 b 2
    print ""
    #方法五
    for k, v in d.iteritems(): print k, v, #a 1 b 2


def dict_compare():
    """
    判断两个字典的差异
    :return:
    """
    print ">>>>>dict_compare:"
    d1 = dict(a=1, b=2)
    d2 = dict(b=2, c=3)

    v1 = d1.viewitems()
    v2 = d2.viewitems()
    # 取交集
    print v1 & v2 #set([('b', 2)])

    #取并集
    print v1 | v2 #set([('a', 1), ('b', 2), ('c', 3)])

    #取差集(仅v1有v2没有)
    print v1 - v2 #set([('a', 1)])

    #对称差集(不会同时出现在v1和v2中)
    print v1 ^ v2 #set([('a', 1), ('c', 3)])

    #判断
    print ('a', 1) in v1 #True
    print ('e', 2) in v1 #False


def dict_update():
    """
    变更字典内容
    :return:
    """

    print ">>>>>dict_update:"

    print u"#在不引入新数据项的情况下更新字典内容"
    a = dict(x=1)
    b = dict(x=10, y=20)
    a.update({k:b[k] for k in a.viewkeys() & b.viewkeys()})
    print a #{'x': 10}

    print u"#视图和字典同步变更"
    d = {"a": 1}
    v = d.viewitems()
    print v #dict_items([('a', 1)])
    d["b"] = 2
    print v #dict_items([('a', 1), ('b', 2)])
    del d["a"]
    print v #dict_items([('a', 1), ('b', 2)])

def dict_defaultdict():
    """
    当访问的key不存在时,defaultdict自动调用factory对象创建所需键值对. factory可以是任何无参数或callable对象
    :return:
    """
    print ">>>>>dict_defaultdict:"
    from collections import defaultdict
    d = defaultdict(list)
    d['a'].append(1) #当key "a"不存在,直接用list()函数创建一个空列表作为value
    print d #defaultdict(<type 'list'>, {'a': [1]})
    d["a"].append(2)
    print d #defaultdict(<type 'list'>, {'a': [1, 2]})
    print d["a"] #[1, 2]

def dict_OrderedDict():
    """
    字典是哈希表,默认迭代是无序的,如果希望按照元素添加顺序输出结果,可以用OrderedDict
    :return:
    """
    print ">>>>>dict_OrderedDict:"
    from collections import OrderedDict
    d = dict()
    d["a"] = 1
    d["b"] = 2
    d["c"] = 3

    print u"#非按添加序列输出"
    for k, v in d.items():print k,v
    #a 1
    #c 3
    #b 2
    od = OrderedDict()
    od["a"] = 1
    od["b"] = 2
    od["c"] = 3

    print u"#按添加序列输出"
    for k, v in od.items():print k, v
    #a 1
    #b 2
    #c 3
    print u"#按LIFO顺序弹出"
    print od.popitem() #('c', 3)
    print od.popitem() #('c', 3)
    print od.popitem() #('a', 1)











def main():
    dict_create()
    dict_operate()
    dict_default_return()
    dict_travel()
    dict_compare()
    dict_update()
    dict_defaultdict()
    dict_OrderedDict()


if __name__=='__main__':
    main()