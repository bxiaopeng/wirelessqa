#!/usr/bin/python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
#  File:        测试工具栏相关操作.py
#  Description: 工具栏显示
#
#  Date:         14/11/23 下午4:06
#  Author:       bixiaopeng
#  Tags:
#---------------------------------------------------------------------------

import wx
import wx.py.images as images


class ToolbarFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Toolbar",size=(300,200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar() #1. 创建状态栏
        toolbar = self.CreateToolBar() #2. 创建工具栏
        toolbar.AddSimpleTool(wx.NewId(),images.getPyBitmap(),"New","Long help for 'new' ") #3. 给工具栏增加一个工具

        toolbar.Realize() #4 准备显示工具栏
        menuBar = wx.MenuBar() # 创建菜单栏

        menu1 = wx.Menu() #创建两个菜单
        menuBar.Append(menu1,"&File")
        menu2 = wx.Menu()
        #创建菜单的项目
        menu2.Append(wx.NewId(),"Copy","Copy in status bar")
        menu2.Append(wx.NewId(),"Cut","把你剪了哦")
        menu2.Append(wx.NewId(),"Paste","")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"Option...","Display Options")
        menuBar.Append(menu2,"&Edit") #在菜单栏上附上菜单
        self.SetMenuBar(menuBar) #在框架上附上菜单栏

if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
