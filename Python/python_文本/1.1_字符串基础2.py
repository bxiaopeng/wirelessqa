#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         1.1_字符串基础2.py
#  Description:  
#
#  Date:         14/12/3 上午9:54
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------


import string

def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('', '')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))

        def translate(s):
            return s.translate(trans, delete)
        return translate
