#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 15:39'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------

"""
知识点：

每个不同的sizer基于一套规则管理它的窗口的尺寸和位置。sizer属于一个容器窗口（比如wx.Panel）。在父中创建的子窗口必须被添加给sizer，sizer管理每个窗

口部件的尺寸和位置。

创建一个sizer的步骤：

创建你想用来自动调用尺寸的panel或container(容器)。
创建sizer。
创建你的子窗口。
使用sizer的Add()方法来将每个子窗口添加给sizer。
sizer可以嵌套，这意味你可以像窗口对象一样添加别的sizer到父sizer。
调用容器的SetSizer(sizer)方法。
最常用的wxPython的sizer：

wx.BoxSizer：在一条线上布局子窗口部件。wx.BoxSizer的布局方向可以是水平或坚直的，并且可以在水平或坚直方向上包含子sizer以创建复杂的布局。在项目被添加时传递给sizer的参数控制子窗口部件如何根据box的主体或垂直轴线作相应的尺寸调整。
wx.FlexGridSizer：一个固定的二维网格，它与wx.GridSizer的区别是，行和列根据所在行或列的最大元素分别被设置。
wx.GridSizer：一个固定的二维网格，其中的每个元素都有相同的尺寸。当创建一个grid sizer时，你要么固定行的数量，要么固定列的数量。项目被从左到右的添加，直到一行被填满，然后从下一行开始。
wx.GridBagSizer：一个固定的二维网格，基于wx.FlexGridSizer。允许项目被放置在网格上的特定点，也允许项目跨越多和网格区域。
wx.StaticBoxSizer：等同于wx.BoxSizer，只是在box周围多了一个附加的边框（有一个可选的标签）。
wx.Sizer的方法：

Add(size, proportion=0,flag=0, border=0,userData=None)：第一个添加一个wxWindow，第二个添加一个嵌套的sizer，第三个添加空的空间，用作分隔符。参数proportion管理窗口总尺寸，它是相对于别的窗口的改变而言的，它只对wx.BoxSizer有意义。参数flag是一个位图，针对对齐、边框位置，增长有许多不同的标志。参数border是窗口或sizer周围以像素为单位的空间总量。userData使你能够将对象与数据关联，例如，在一个子类中，可能需要更多的用于尺寸的信息。
Fit(window)
FitInside(window )：调整window尺寸以匹配sizer认为所需要的最小化尺寸。这个参数的值通常是使用sizer的窗口。FitInside()是一个类似的方法，只不过将改变窗口在屏幕上的显示替换为只改变它的内部实现。它用于scroll panel中的窗口以触发滚动栏的显示。
GetSize()：以wx.Size对象的形式返回sizer的尺寸。
GetPosition()：以wx.Point对象的形式返回sizer的位置。
GetMinSize()：以wx.Size对象的形式返回完全填充sizer所需的最小尺寸。
Layout()：强迫sizer去重新计算它的孩子的尺寸和位置。在动态地添加或删除了一个孩子之后调用。
Prepend(...)：与Add()相同（只是为了布局的目的，把新的对象放在sizer列表的开头）。
Remove(window)
Remove(sizer)
Remove(nth)：从sizer中删除一个对象。
SetDimension(x, y, width,height)：强迫sizer按照给定的参数重新定位它的所有孩子。

"""


import wx
import wx.lib.buttons
import cPickle
import os

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
        self.title = "Paint Frame"
        wx.Frame.__init__(self, parent, -1, self.title, size = (800, 600))
        self.paint = PaintWindow(self, -1)

        #状态栏
        self.paint.Bind(wx.EVT_MOTION, self.OnPaintMotion)
        self.InitStatusBar()

        #创建菜单
        self.CreateMenuBar()

        self.filename = ""

        #创建工具栏使用的面板
        self.CreatePanel()

    def CreatePanel(self):
        controlPanel = ControlPanel(self, -1, self.paint)
        box = wx.BoxSizer(wx.HORIZONTAL) #放置水平的box sizer
        box.Add(controlPanel, 0, wx.EXPAND) #水平方向伸展时不改变尺寸
        box.Add(self.paint, -1, wx.EXPAND)
        self.SetSizer(box)



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
                                       ("&Blue", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Other", "", self.OnOtherColor, wx.ITEM_RADIO))),
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
        '''
        打开开文件对话框
        '''
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open paint file...",
                            os.getcwd(),
                            style = wx.OPEN,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()



    def OnSave(self, event):
        '''
        保存文件
        '''
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):
        '''
        弹出文件保存对话框
        '''
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self,
                            "Save paint as ...",
                            os.getcwd(),
                            style = wx.SAVE | wx.OVERWRITE_PROMPT,
                            wildcard = file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]: #如果没有文件名后缀
                filename = filename + '.paint'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()


    def OnColor(self, event):
        '''
        更改画笔内容
        '''
        menubar = self.GetMenuBar()
        itemid = event.GetId()
        item = menubar.FindItemById(itemid)
        color = item.GetLabel() #获取菜单项内容
        self.paint.SetColor(color)

    def OnOtherColor(self, event):
        '''
        使用颜色对话框
        '''
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)   #创建颜色对象数据
        if dlg.ShowModal() == wx.ID_OK:
            self.paint.SetColor(dlg.GetColourData().GetColour()) #根据选择设置画笔颜色
        dlg.Destroy()

    def OnCloseWindow(self, event):
        self.Destroy()

    def SaveFile(self):
        '''
        保存文件
        '''
        if self.filename:
            data = self.paint.GetLinesData()
            f = open(self.filename, 'w')
            cPickle.dump(data, f)
            f.close()

    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename, 'r')
                data = cPickle.load(f)
                f.close()
                self.paint.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a paint file."
                              % self.filename, "error tip",
                              style = wx.OK | wx.ICON_EXCLAMATION)

class ControlPanel(wx.Panel):
    BMP_SIZE = 16
    BMP_BORDER = 3
    NUM_COLS = 4
    SPACING = 4

    colorList = ('Black', 'Yellow', 'Red', 'Green', 'Blue', 'Purple',
                 'Brown', 'Aquamarine', 'Forest Green', 'Light Blue',
                 'Goldenrod', 'Cyan', 'Orange', 'Navy', 'Dark Grey',
                 'Light Grey')
    maxThickness = 16

    def __init__(self, parent, ID, paint):
        wx.Panel.__init__(self, parent, ID, style = wx.RAISED_BORDER)
        self.paint = paint
        buttonSize = (self.BMP_SIZE + 2 * self.BMP_BORDER,
                      self.BMP_SIZE + 2 * self.BMP_BORDER)
        colorGrid = self.createColorGrid(parent, buttonSize) #创建颜色grid sizer
        thicknessGrid = self.createThicknessGrid(buttonSize) #创建线条grid sizer
        self.layout(colorGrid, thicknessGrid)

    def createColorGrid(self, parent, buttonSize):
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols = self.NUM_COLS, hgap = 2, vgap = 2)
        for eachColor in self.colorList:
            bmp = self.MakeBitmap(eachColor)
            b = wx.lib.buttons.GenBitmapToggleButton(self, -1, bmp, size = buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetColour, b)
            colorGrid.Add(b, 0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid

    def createThicknessGrid(self, buttonSize):
        self.thicknessIdMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols = self.NUM_COLS, hgap = 2, vgap = 2)
        for x in range(1, self.maxThickness + 1):
            b = wx.lib.buttons.GenToggleButton(self, -1, str(x), size = buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetThickness, b)
            thicknessGrid.Add(b, 0)
            self.thicknessIdMap[b.GetId()] = 2
            self.thicknessButtons[x] = b
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid

    def layout(self, colorGrid, thicknessGrid):
        box = wx.BoxSizer(wx.VERTICAL) #使用垂直的box szier放置grid sizer
        box.Add(colorGrid, 0, wx.ALL, self.SPACING) #参数0表示在垂直方向伸展时不改变尺寸
        box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
        self.SetSizer(box)
        box.Fit(self)

    def OnSetColour(self, event):
        color = self.colorMap[event.GetId()]
        if color != self.paint.color:
            self.colorButtons[self.paint.color].SetToggle(False)
        self.paint.SetColor(color)

    def OnSetThickness(self, event):
        thickness = self.thicknessIdMap[event.GetId()]
        if thickness != self.paint.thickness:
            self.thicknessButtons[self.paint.thickness].SetToggle(False)
        self.paint.SetThickness(thickness)

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(16, 15)
        dc = wx.MemoryDC(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

if __name__ == '__main__':
    app = wx.App()
    frame = PaintFrame(None)
    frame.Show(True)
    app.MainLoop()