#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 15:23'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------
"""
原型：

wxSplashScreen(const wxBitmap& bitmap, long splashStyle, int milliseconds, wxWindow* parent, wxWindowID id,
    const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxDefaultSize, long style = wxSIMPLE_BORDER|wxFRAME_NO_TASKBAR|wxSTAY_ON_TOP)

splashStyle is a bitlist of some of the following:

wxSPLASH_CENTRE_ON_PARENT
wxSPLASH_CENTRE_ON_SCREEN
wxSPLASH_NO_CENTRE
wxSPLASH_TIMEOUT
wxSPLASH_NO_TIMEOUT
milliseconds is the timeout in milliseconds.

方法：

wxSplashScreen::OnCloseWindow
wxSplashScreen::GetSplashStyle
wxSplashScreen::GetSplashWindow
wxSplashScreen::GetTimeout
"""


import wx


class PaintApp(wx.App):
    def OnInit(self):
        bmp = wx.Image("a.jpg").ConvertToBitmap()
        wx.SplashScreen(bmp,
                        wx.SPLASH_CENTER_ON_SCREEN | wx.SPLASH_TIMEOUT,
                        3000,
                        None,
                        -1)
        wx.Yield()
        frame = PaintFrame(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

class PaintFrame(wx.Frame):

      def __init__(self, parent):
        self.title = "Paint Frame"
        wx.Frame.__init__(self, parent, -1, self.title, size = (800, 600))



if __name__ == '__main__':
    app = PaintApp()
    app.MainLoop()