#-*- coding:utf-8 -*-
import wx


class SubclassDialog(wx.Dialog):
    #初始化对话框
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Dialog Subclass', 
                size=(300, 100))
        okButton = wx.Button(self, wx.ID_OK, "OK", pos=(15, 15))
        okButton.SetDefault()
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(115, 15))
        
if __name__ == '__main__':
    app = wx.App()
    app.MainLoop() 
    dialog = SubclassDialog()
    #显示模式对话框
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        print "OK"
    else:
        print "Cancel"
    dialog.Destroy()