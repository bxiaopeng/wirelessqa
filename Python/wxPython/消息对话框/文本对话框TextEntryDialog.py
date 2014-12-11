#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 14:56'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------
"""
本节看看单行文本对话框的使用，先看函数原型：

wxTextEntryDialog(wxWindow* parent, const wxString& message,
const wxString& caption = "Please enter text", const wxString& defaultValue = "", long style = wxOK | wxCANCEL | wxCENTRE, const wxPoint& pos = wxDefaultPosition)

其支持的方法有：

wxTextEntryDialog::GetValue  获取文档框中的值
wxTextEntryDialog::SetValue  设置文本框中的值
wxTextEntryDialog::ShowModal 模态显示对话框
"""
import wx


class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, u'测试面板Panel', size = (600,300))

        #创建面板
        panel = wx.Panel(self)
        #在Panel上添加Button
        button = wx.Button(panel, label = u'关闭', pos = (150, 60), size = (100, 60))

        #绑定单击事件
        self.Bind(wx.EVT_BUTTON, self.onclick_button, button)

    def onclick_button(self, event):
        dlg = wx.TextEntryDialog(None, u"请在下面文本框中输入内容:", u"文本输入框标题", u"默认内容")

        if dlg.ShowModal() == wx.ID_OK:
            message = dlg.GetValue() #获取文本框中输入的值
            dlg_tip = wx.MessageDialog(None, message, u"标题信息", wx.OK | wx.ICON_INFORMATION)

            if dlg_tip.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg_tip.Destroy()

        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()