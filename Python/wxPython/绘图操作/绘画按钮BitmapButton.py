#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 15:04'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------
"""
原型：

wxBitmapButton( wxWindow* parent, wxWindowID id, const wxBitmap& bitmap, const wxPoint& pos = wxDefaultPosition,
const wxSize& size = wxDefaultSize, long style = wxBU_AUTODRAW, const wxValidator& validator = wxDefaultValidator, const wxString& name = "button")

方法：

wxBitmapButton::Create
wxBitmapButton::GetBitmapDisabled
wxBitmapButton::GetBitmapFocus
wxBitmapButton::GetBitmapHover
wxBitmapButton::GetBitmapLabel
wxBitmapButton::GetBitmapSelected
wxBitmapButton::SetBitmapDisabled
wxBitmapButton::SetBitmapFocus
wxBitmapButton::SetBitmapHover
wxBitmapButton::SetBitmapLabel
wxBitmapButton::SetBitmapSelected
"""


import wx

class BitmapButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Bitmap button example",
                          size = (1000, 700))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("blue")

        #创建一个绘图对象
        bmp = wx.Image(u"绘图操作/a.jpg", wx.BITMAP_TYPE_JPEG).ConvertToBitmap()

        #绘图按钮1，默认风格3D
        self.button = wx.BitmapButton(panel, -1, bmp, pos = (50, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        #绘图按钮1，不带边框
        self.button2 = wx.BitmapButton(panel, -1, bmp, style = 0, pos = (350, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

    def OnClick(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = BitmapButtonFrame()
    frame.Show()
    app.MainLoop()