#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:05'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------

import wx

class PaintFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Panit Frame", size = (800, 600))
        self.paint = PaintWindow(self, -1)

        #状态栏
        self.paint.Bind(wx.EVT_MOTION, self.OnPaintMotion)
        self.statusbar = self.CreateStatusBar()
        #将状态栏分割为3个区域,比例为1:2:3
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])


    def OnPaintMotion(self, event):

        #设置状态栏1内容
        self.statusbar.SetStatusText(u"鼠标位置：" + str(event.GetPositionTuple()), 0)

        #设置状态栏2内容
        self.statusbar.SetStatusText(u"当前线条长度：%s" % len(self.paint.curLine), 1)

        #设置状态栏3内容
        self.statusbar.SetStatusText(u"线条数目：%s" % len(self.paint.lines), 2)

        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = PaintFrame(None)
    frame.Show(True)
    app.MainLoop()