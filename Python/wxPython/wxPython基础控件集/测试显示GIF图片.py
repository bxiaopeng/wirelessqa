#!/usr/bin/python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
#  File:
#  Description: 测试显示图片
#
#  Date:         14/11/23 下午4:06
#  Author:       bixiaopeng
#  Tags:
#---------------------------------------------------------------------------
import wx

filenames = [ "img.gif" ]

class DisplayImage(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Loading Images")
        p = wx.Panel(self)

        fgs = wx.FlexGridSizer(cols=2, hgap=10, vgap=10)
        print "sizer"
        for name in filenames:
            #1 从文件载入图像
            img1 = wx.Image(name, wx.BITMAP_TYPE_ANY)

            # Scale the oiginal to another wx.Image
            w = img1.GetWidth()
            h = img1.GetHeight()
            img2 = img1.Scale(w/2, h/2)#2 缩小图像

            #3 转换它们为静态位图部件
            sb1 = wx.StaticBitmap(p, -1, wx.BitmapFromImage(img1))
            sb2 = wx.StaticBitmap(p, -1, wx.BitmapFromImage(img2))

            # and put them into the sizer
            fgs.Add(sb1)
            fgs.Add(sb2)

        p.SetSizerAndFit(fgs)
        self.Fit()


app = wx.App()
frm = DisplayImage()
frm.Show()
app.MainLoop()