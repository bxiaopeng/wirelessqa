#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:18'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------


import wx

class MyFrame(wx.Frame):
    '''
    创建一个Frame类
    '''
    def __init__(self, image, parent = None, id = -1,
                 pos = wx.DefaultPosition,
                 title = u"Hello wxPython"):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight() #图片的大小用做窗口大小
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent = self, bitmap = temp)

#class MyApp(wx.App):
#    '''
#    创建一个App类
#    '''
#    def OnInit(self):
#        image = wx.Image('back_image.jpg', wx.BITMAP_TYPE_JPEG) #加载国片
#        self.frame = MyFrame(image)
#        self.frame.Show()
#        self.SetTopWindow(self.frame)
#        return True

def main():
    #创建一个PySimpleApp类对象
    app = wx.App()
    image = wx.Image('a.jpg', wx.BITMAP_TYPE_JPEG) #加载国片
    frame = MyFrame(image)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()