#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         测试剪切版.py
#  Description:  wxPython剪切版
#
#  Date:         14/11/27 下午3:38
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------

import wx

class ClipboardPanel(wx.Panel):
    """
    剪切版
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        lbl = wx.StaticText(self, label=u"输入文本后点复制到剪切版:")
        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        btn_copy = wx.Button(self, label=u"复制")
        btn_copy.Bind(wx.EVT_BUTTON, self.onCopy)

        # self.text.SetValue("jlasjdlfajsdlfjasld")

        btn_copy_flush = wx.Button(self, label=u"复制后关闭")
        btn_copy_flush.Bind(wx.EVT_BUTTON, self.onCopyAndFlush)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(self.text, 1, wx.EXPAND)
        sizer.Add(btn_copy, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btn_copy_flush, 0, wx.ALL|wx.CENTER, 5)
        self.SetSizer(sizer)

    def onCopy(self, event):
        """
        监听复制按钮
        """
        self.data_obj = wx.TextDataObject()
        self.data_obj.SetText(self.text.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.data_obj)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")

    def onCopyAndFlush(self, event):
        """
        监听复制and关闭操作
        :param event:
        :return:
        """
        self.data_obj = wx.TextDataObject()
        self.data_obj.SetText(self.text.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.data_obj)
            wx.TheClipboard.Flush()
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")

        self.GetParent().Close()

########################################################################
class ClipboardFrame(wx.Frame):
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title=u"复制到剪切版")
        panel = ClipboardPanel(self)
        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = ClipboardFrame()
    app.MainLoop()

