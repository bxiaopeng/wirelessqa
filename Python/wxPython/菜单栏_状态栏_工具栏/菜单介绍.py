#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 15:58'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------


import wx

class PaintWindow(wx.Window):
        def __init__(self, parent, id):
            wx.Window.__init__(self, parent, id)
            self.SetBackgroundColour("Red")
            self.color = "Green"
            self.thickness = 10

            #创建一个画笔
            self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
            self.lines = []
            self.curLine = []
            self.pos = (0, 0)
            self.InitBuffer()

            #连接事件
            self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
            self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
            self.Bind(wx.EVT_MOTION, self.OnMotion)
            self.Bind(wx.EVT_SIZE, self.OnSize)
            self.Bind(wx.EVT_IDLE, self.OnIdle)
            self.Bind(wx.EVT_PAINT, self.OnPaint)

        def InitBuffer(self):
            size = self.GetClientSize()

            #创建缓存的设备上下文
            self.buffer = wx.EmptyBitmap(size.width, size.height)
            dc = wx.BufferedDC(None, self.buffer)

            #使用设备上下文
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

            #获取鼠标位置
            self.pos = event.GetPositionTuple()
            self.CaptureMouse()

        def OnLeftUp(self, event):
            if self.HasCapture():
                self.lines.append((self.color,
                                   self.thickness,
                                   self.curLine))
                self.curLine = []
                self.ReleaseMouse()

        def OnMotion(self, event):
            if event.Dragging() and event.LeftIsDown():
                dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
                self.drawMotion(dc, event)
            event.Skip()

        def drawMotion(self, dc, event):
            dc.SetPen(self.pen)
            newPos = event.GetPositionTuple()
            coords = self.pos + newPos
            self.curLine.append(coords)
            dc.DrawLine(*coords)
            self.pos = newPos

        def OnSize(self, event):
            self.reInitBuffer = True

        def OnIdle(self, event):
            if self.reInitBuffer:
                self.InitBuffer()
                self.Refresh(False)

        def OnPaint(self, event):
            dc = wx.BufferedPaintDC(self, self.buffer)

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

class PaintFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Panit Frame", size = (800, 600))
        self.paint = PaintWindow(self, -1)

        #状态栏
        self.paint.Bind(wx.EVT_MOTION, self.OnPaintMotion)
        self.InitStatusBar()

        #创建菜单
        self.CreateMenuBar()


    def InitStatusBar(self):
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

    def MenuData(self):
        '''
                   菜单数据
        '''
        #格式：菜单数据的格式现在是(标签, (项目))，其中：项目组成为：标签, 描术文字, 处理器, 可选的kind
        #标签长度为2，项目的长度是3或4
        return [("&File", (             #一级菜单项
                           ("&New", "New paint file", self.OnNew),             #二级菜单项
                           ("&Open", "Open paint file", self.OnOpen),
                           ("&Save", "Save paint file", self.OnSave),
                           ("", "", ""),                                       #分隔线
                           ("&Color", (
                                       ("&Black", "", self.OnColor, wx.ITEM_RADIO),  #三级菜单项，单选
                                       ("&Red", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Green", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Blue", "", self.OnColor, wx.ITEM_RADIO))),
                           ("", "", ""),
                           ("&Quit", "Quit", self.OnCloseWindow)))
               ]
    def CreateMenuBar(self):
        '''
        创建菜单
        '''
        menuBar = wx.MenuBar()
        for eachMenuData in self.MenuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.CreateMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def CreateMenu(self, menuData):
        '''
        创建一级菜单
        '''
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.CreateMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu) #递归创建菜单项
            else:
                self.CreateMenuItem(menu, *eachItem)
        return menu

    def CreateMenuItem(self, menu, label, status, handler, kind = wx.ITEM_NORMAL):
        '''
        创建菜单项内容
        '''
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler,menuItem)

    def OnNew(self, event):
        pass

    def OnOpen(self, event):
        pass

    def OnSave(self, event):
        pass

    def OnColor(self, event):
        '''
        更改画笔内容
        '''
        menubar = self.GetMenuBar()
        itemid = event.GetId()
        item = menubar.FindItemById(itemid)
        color = item.GetLabel() #获取菜单项内容
        self.paint.SetColor(color)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = PaintFrame(None)
    frame.Show(True)
    app.MainLoop()