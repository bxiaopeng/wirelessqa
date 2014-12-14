#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         listutils.py
#  Description:  
#
#  Date:         14/12/8 下午4:42
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------



def del_repeat(list):
    """
    列表去重
    :return:
    """
    l = {}.fromkeys(list).keys()
    return l