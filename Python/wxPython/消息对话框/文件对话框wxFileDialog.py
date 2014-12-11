#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:00'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------


"""
知识点介绍：

wx.FileDialog原型：

wxFileDialog(wxWindow* parent, const wxString& message = "Choose a file", const wxString& defaultDir = "",
    const wxString& defaultFile = "", const wxString& wildcard = "*.*", long style = wxFD_DEFAULT_STYLE, const wxPoint& pos = wxDefaultPosition, const wxSize& sz = wxDefaultSize, const wxString& name = "filedlg")

方法：

wxFileDialog::wxFileDialog
wxFileDialog::~wxFileDialog
wxFileDialog::GetDirectory
wxFileDialog::GetFilename
wxFileDialog::GetFilenames
wxFileDialog::GetFilterIndex
wxFileDialog::GetMessage
wxFileDialog::GetPath
wxFileDialog::GetPaths
wxFileDialog::GetWildcard
wxFileDialog::SetDirectory
wxFileDialog::SetFilename
wxFileDialog::SetFilterIndex
wxFileDialog::SetMessage
wxFileDialog::SetPath
wxFileDialog::SetWildcard
wxFileDialog::ShowModal
参数：

parent
Parent window.
message
Message to show on the dialog.
defaultDir
The default directory, or the empty string.
defaultFile
The default filename, or the empty string.
wildcard
A wildcard, such as "*.*" or "BMP files (*.bmp)|*.bmp|GIF files (*.gif)|*.gif".
                Note that the native Motif dialog has some limitations with respect to wildcards; see the Remarks section above.

style
A dialog style. See wxFD_* styles for more info.
pos
Dialog position. Not implemented.
size
Dialog size. Not implemented.
name
Dialog name. Not implemented.
                                    附:Style取值
wxFD_DEFAULT_STYLE	Equivalent to wxFD_OPEN.
wxFD_OPEN	This is an open dialog; usually this means that the default button's label of the dialog is "Open". Cannot be combined with wxFD_SAVE.
wxFD_SAVE	This is a save dialog; usually this means that the default button's label of the dialog is "Save". Cannot be combined with wxFD_OPEN.
wxFD_OVERWRITE_PROMPT	For save dialog only: prompt for a confirmation if a file will be overwritten.
wxFD_FILE_MUST_EXIST	For open dialog only: the user may only select files that actually exist.
wxFD_MULTIPLE	For open dialog only: allows selecting multiple files.
wxFD_CHANGE_DIR	Change the current working directory to the directory where the file(s) chosen by the user are.
wxFD_PREVIEW	Show the preview of the selected files (currently only supported by wxGTK using GTK+ 2.4 or later).

"""
import wx
import cPickle
import os

"""
有些问题
"""

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



if __name__ == '__main__':
    app = wx.App()
    frame = PaintFrame(None)
    frame.Show(True)
    app.MainLoop()