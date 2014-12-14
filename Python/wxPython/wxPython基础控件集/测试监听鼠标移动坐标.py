#!/usr/bin/python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
#  File:        测试监听鼠标移动坐标.py
#  Description: 监听鼠标移动坐标
#
#  Date:         14/11/23 下午4:06
#  Author:       bixiaopeng
#  Tags:
#---------------------------------------------------------------------------

import wx


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "MyFrame", size=(300, 300))
        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_MOTION, self.on_move)
        wx.StaticText(panel, -1, u"坐标:", pos=(10, 12))
        self.pos_ctrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))

    def on_move(self, event):
        #获取坐标
        pos = event.GetPosition()
        #更攺坐标的值
        self.pos_ctrl.SetValue("%s,%s" % (pos.x, pos.y))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()

