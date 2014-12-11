#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:12'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------

"""
列表选择框就是让用户从提供的列表中选择目标项，原型如下：

  wxSingleChoiceDialog(wxWindow* parent, const wxString& message, const wxString& caption, int n, const wxString* choices, void** clientData = NULL, long style = wxCHOICEDLG_STYLE, const wxPoint& pos = wxDefaultPosition)

 支持的方法如下：

wxSingleChoiceDialog::GetSelection 返回选项的index
wxSingleChoiceDialog::GetSelectionClientData 返回与选项绑定的clientdata内容
wxSingleChoiceDialog::GetStringSelection 返回选择的字符串内容
wxSingleChoiceDialog::SetSelection 设置选项
wxSingleChoiceDialog::ShowModal

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
    def OnCloseMe(self, event):
        dlg = wx.SingleChoiceDialog(None, u"请选择你喜欢的水果:", u"列表选择框标题",
                                    [u"苹果", u"西瓜", u"草莓"])
        if dlg.ShowModal() == wx.ID_OK:
            message = dlg.GetStringSelection() #获取选择的内容
            dlg_tip = wx.MessageDialog(None, message, u"标题信息", wx.OK | wx.ICON_INFORMATION)
            if dlg_tip.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg_tip.Destroy()
        dlg.Destroy()



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()