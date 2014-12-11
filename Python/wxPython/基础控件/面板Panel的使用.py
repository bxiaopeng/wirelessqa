#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:14'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------

"""
Frame即为框架，可以直接理解为一个窗口。要创建一个Frame的子类，需要调用Frame类的构造函数，原型如下：

 wx.Frame(parent, id=-1, title=””, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name=”frame”)

 各参数含义:

  parent：顶级窗口直接使用None。

  id：标识，有三种赋值方式：1、自己指定一个正数，但确保同一窗体中不能重复；2、取值-1或wx.ID_ANY,表示由系统自动分配,可以通过frame.GetId()来获取此值；3、使用wx.NewId()函数来创建。

  pos:窗口位置。

  size:窗口大小。

  style：样式，其中，wx.DEFAULT_FRAME_STYLE的值为：wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER |   wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX

  增加一个样式使用“|”， 去除一个样式使用"^"

Panel是窗口的容器，通常其大小与Frame一样，在其上放置各种控件，这样可将窗口内容与工具栏及状态栏区分开，能过TAB键可遍历Panel中的元素
"""

import wx

class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, u'测试面板Panel', size = (600, 300))

        #创建面板
        panel = wx.Panel(self)

        #在Panel上添加Button
        button = wx.Button(panel, label = u'关闭', pos = (150, 60), size = (100, 60))

        #绑定单击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)

    def OnCloseMe(self, event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()