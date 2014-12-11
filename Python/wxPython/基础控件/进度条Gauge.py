#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 15:02'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------

"""
原型：

bool Create(wxWindow* parent, wxWindowID id, int range, const wxPoint& pos = wxDefaultPosition,
const wxSize& size = wxDefaultSize, long style = wxGA_HORIZONTAL, const wxValidator& validator = wxDefaultValidator, const wxString& name = "gauge")

方法：

wxGauge::wxGauge
wxGauge::~wxGauge
wxGauge::Create
wxGauge::GetBezelFace
wxGauge::GetRange
wxGauge::GetShadowWidth
wxGauge::GetValue
wxGauge::IsVertical
wxGauge::SetBezelFace
wxGauge::SetRange
wxGauge::SetShadowWidth
wxGauge::SetValue
wxGauge::Pulse
"""

import wx


class GuageFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size = (600, 300))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 100, (100, 60), (250, 25), style = wx.GA_PROGRESSBAR)
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

    def OnIdle(self, event):
        self.count = self.count + 1
        if self.count >= 80:
            self.count = 0
        self.gauge.SetValue(self.count)

if __name__ == '__main__':
    app = wx.App()
    frame = GuageFrame()
    frame.Show()
    app.MainLoop()