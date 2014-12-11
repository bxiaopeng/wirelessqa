#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 15:59'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------


import wx
import wx.py.images

class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, 'Toolbars', size = (300, 200))

        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')

        #创建状态栏
        statusBar = self.CreateStatusBar()

        #创建工具栏
        toolbar = self.CreateToolBar()
        #增加一个工具
        toolbar.AddSimpleTool(wx.NewId(), wx.py.images.getPyBitmap(), "New", "Long help for 'New'")
        toolbar.AddSimpleTool(wx.NewId(), wx.py.images.getPyBitmap(), "Edit", "Long help for 'Edit'")
        #准备显示
        toolbar.Realize()

        #创建菜单
        menuBar = wx.MenuBar()

        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File") #菜单项目1

        menu2 = wx.Menu()

        #菜单内容&表示随后的字符为热键，参数3为在状态栏上显示的菜单项说明
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)

if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()