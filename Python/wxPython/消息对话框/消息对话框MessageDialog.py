#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 14:38'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------

"""
消息对话框即我们平时说的Messagebox，看看它的原型，下面是wxWidgets中的原型定义，C++风格，

与python风格的区别就是wx前缀与后面名称直接相连，例如wxMessageDialog，在wxpython中使用时就是wx.MessageDialog

wxMessageDialog(wxWindow* parent, const wxString& message, const wxString& caption = "Message box", long style = wxOK | wxCANCEL, const wxPoint& pos = wxDefaultPosition)

其各参数不多做介绍，主要看看ShowModal()方法，它使用应用程序在对话框关闭前不能响应其它窗口的用户事件，返回一个整数，取值如下：
wx.ID_YES, wx.ID_NO, wx.ID_CANCEL, wx.ID_OK。

另外，style的取值主要有以下几种：

wxOK	Show an OK button.
wxCANCEL	Show a Cancel button.
wxYES_NO	Show Yes and No buttons.
wxYES_DEFAULT	Used with wxYES_NO, makes Yes button the default - which is the default behaviour.
wxNO_DEFAULT	Used with wxYES_NO, makes No button the default.
wxICON_EXCLAMATION	Shows an exclamation mark icon.
wxICON_HAND	Shows an error icon.
wxICON_ERROR	Shows an error icon - the same as wxICON_HAND.
wxICON_QUESTION	Shows a question mark icon.
wxICON_INFORMATION	Shows an information (i) icon.
wxSTAY_ON_TOP	The message box stays on top of all other window, even those of the other applications (Windows only).

"""

import wx

class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, u'消息对话框MessageDialog面板', size = (300, 200))
        #创建面板
        panel = wx.Panel(self)

        #在Panel上添加Button
        button = wx.Button(panel, label= u'关闭', pos = (20, 10), size = (100, 60))

        #绑定单击事件
        self.Bind(wx.EVT_BUTTON, self.onclick_button, button)

    def onclick_button(self, event):
        #Yes and No
        # dlg = wx.MessageDialog(None, u"消息对话框测试,点yes关闭,no不关闭", u"是否关闭", wx.YES_NO | wx.ICON_QUESTION)
        #OK and Cancel
        # dlg = wx.MessageDialog(None, u"消息对话框测试,点yes关闭,no不关闭", u"是否关闭", wx.CANCEL | wx.ICON_QUESTION)
        #默认焦点在Yes上
        dlg = wx.MessageDialog(None, u"消息对话框测试,点yes关闭,no不关闭", u"是否关闭", wx.YES_NO|wx.YES_DEFAULT)
        #默认焦点在No上
        # dlg = wx.MessageDialog(None, u"消息对话框测试,点yes关闭,no不关闭", u"是否关闭", wx.YES_NO|wx.NO_DEFAULT)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
