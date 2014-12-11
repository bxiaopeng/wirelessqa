#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:11'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------

"""
wxPython首先在触发对象中查找匹配事件类型的被绑定的处理器函数，
如果找到，刚相应方法被执行。如果没找到，wxPython将检查该事件是否传送到了上一级的容器，如果是，父窗口被检查，如此一级级向上查找，直到找到一个处理函数或到达顶层窗口。
"""
import wx

class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, u'测试面板Panel', size = (600, 300))

        #创建面板
        self.panel = wx.Panel(self)

        #在Panel上添加Button
        self.button = wx.Button(self.panel, label = u'关闭', pos = (150, 60), size = (100, 60))

        #绑定单击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, self.button)

        #绑定鼠标位于按钮上事件
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindows)

        #绑定鼠标离开事件
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindows)

    def OnCloseMe(self, event):
        self.panel.SetBackgroundColour('Red')
        self.panel.Refresh()

    def OnEnterWindows(self, event):
        self.panel.SetBackgroundColour('Blue')
        self.panel.Refresh()
        self.button.SetLabel(u"鼠标在我上面")
        event.Skip()

    def OnLeaveWindows(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()
        self.button.SetLabel(u"鼠标离开我了")
        event.Skip()

#    #消息对话框
#    def OnCloseMe(self, event):
#        dlg = wx.MessageDialog(None, u"消息对话框测试", u"标题信息", wx.YES_NO | wx.ICON_QUESTION)
#        if dlg.ShowModal() == wx.ID_YES:
#            self.Close(True)
#        dlg.Destroy()
#
#    #文本输入对话框
#    def OnCloseMe(self, event):
#        dlg = wx.TextEntryDialog(None, u"请在下面文本框中输入内容:", u"文本输入框标题", u"默认内容")
#        if dlg.ShowModal() == wx.ID_OK:
#            message = dlg.GetValue() #获取文本框中输入的值
#            dlg_tip = wx.MessageDialog(None, message, u"标题信息", wx.OK | wx.ICON_INFORMATION)
#            if dlg_tip.ShowModal() == wx.ID_OK:
#                self.Close(True)
#            dlg_tip.Destroy()
#        dlg.Destroy()
     #列表选择对话框
#    def OnCloseMe(self, event):
#        dlg = wx.SingleChoiceDialog(None, u"请选择你喜欢的水果:", u"列表选择框标题",
#                                    [u"苹果", u"西瓜", u"草莓"])
#        if dlg.ShowModal() == wx.ID_OK:
#            message = dlg.GetStringSelection() #获取选择的内容
#            dlg_tip = wx.MessageDialog(None, message, u"标题信息", wx.OK | wx.ICON_INFORMATION)
#            if dlg_tip.ShowModal() == wx.ID_OK:
#                self.Close(True)
#            dlg_tip.Destroy()
#        dlg.Destroy()



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()