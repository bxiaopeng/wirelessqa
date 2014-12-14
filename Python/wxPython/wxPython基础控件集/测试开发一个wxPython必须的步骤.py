#!/usr/bin/python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
#  File:
#  Description:  开发一个wxPython程序所必须的五个基本步骤
#
#  Date:         14/11/23 下午4:06
#  Author:       bixiaopeng
#  Tags:
#---------------------------------------------------------------------------

import wx  #导入必须的wxPython包

class App(wx.App): #子类化wxPython应用程序类
    def OnInit(self): #定义一个应用程序初始化方法
        frame = wx.Frame(parent=None, id=-1, title='你好,老毕')
        frame.Show()
        return True

app = App() #创建一个应用类的实例
app.MainLoop()	#进入这个应用程序的主事件循环