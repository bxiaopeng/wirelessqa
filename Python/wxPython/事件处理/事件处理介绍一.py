#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:09'
#  Author:       'bixiaopeng'
#  Tags:         from: http://www.cnblogs.com/dyx1024/archive/2012/07/07/2580656.html
#---------------------------------------------------------------------------

"""
事件处理是wxPython程序工作的基本机制，先看几个术语：

事件(event):应该程序期间发生的事情，要求有一个响应。
事件对象(event object)：代表具体一个事件，包括事件的数据属性，为wx.Event或其子类的实例，如wx.CommandEvent/wx.MouseEvent。
事件类型（event type)：wxPython分配给每个事件对象的一个整数ID。

wx.Event的子类：

wx.CloseEvent:框架关闭时触发，事件类型有普通框架关闭和系统关闭事件。
wx.CommandEvent：与窗口部件的简单的交互都会触发此事件，如按钮单击，菜单项选择等。
wx.KeyEvent:按键动作。
wx.MouseEvent：鼠标事件。
wx.PaintEvent:当窗口内容被重画时触发。
wx.SizeEvent:窗口大小或布局改变时触发。
wx.TimerEvent:由类wx.Timer创建，定期事件。
wx.EvtHandler的Bind方法：

  它用来创建事件绑定，原型如下：

  Bind(event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)

  它将一个事件和一个对象与一个事件处理函数绑定。

 看一个菜单项选择事件绑定的实例：

"""


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
        menu_item1 = menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)

        #菜单项事件绑定
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menu_item1)

    #消息对话框
    def OnCloseMe(self, event):
        dlg = wx.MessageDialog(None, u"消息对话框测试", u"标题信息", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()
if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()