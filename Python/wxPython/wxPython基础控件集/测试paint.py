#-*- coding:utf-8 -*-

import wx


class SketchWindow(wx.Window):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.SetBackgroundColour("White")
        self.color = "Black"
        self.thickness = 1
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)#1 创建一个wx.Pen对象
        self.lines = []
        self.curLine = []
        self.pos = (0, 0)
        self.InitBuffer()

#2 连接事件
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitBuffer(self):
        size = self.GetClientSize()

#3 创建一个缓存的设备上下文
        self.buffer = wx.EmptyBitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)

#4 使用设备上下文
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DrawLines(dc)

        self.reInitBuffer = False

    def GetLinesData(self):
        return self.lines[:]

    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()

    def OnLeftDown(self, event):
        self.curLine = []
        self.pos = event.GetPositionTuple()#5 得到鼠标的位置
        self.CaptureMouse()#6 捕获鼠标

    def OnLeftUp(self, event):
        if self.HasCapture():
            self.lines.append((self.color,
                               self.thickness,
                               self.curLine))
            self.curLine = []
            self.ReleaseMouse()#7 释放鼠标

    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():#8 确定是否在拖动
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)#9 创建另一个缓存的上下文
            self.drawMotion(dc, event)
        event.Skip()
    #10 绘画到设备上下文
    def drawMotion(self, dc, event):
        dc.SetPen(self.pen)
        newPos = event.GetPositionTuple()
        coords = self.pos + newPos
        self.curLine.append(coords)
        dc.DrawLine(*coords)
        self.pos = newPos

    def OnSize(self, event):
        self.reInitBuffer = True #11 处理一个resize事件

    def OnIdle(self, event):#12 空闲时的处理
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)#13 处理一个paint（描绘）请求

    #14 绘制所有的线条
    def DrawLines(self, dc):
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour, thickness, wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawLine(*coords)

    def SetColor(self, color):
        self.color = color
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

    def SetThickness(self, num):
        self.thickness = num
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)


class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame",
                size=(800,600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion) 
        self.statusbar = self.CreateStatusBar()
        
    def OnSketchMotion(self,event):
        self.statusbar.SetStatusText(str(event.GetPositionTuple())) 
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()