#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 15:54'
#  Author:       'bixiaopeng'
#  Tags:         
#---------------------------------------------------------------------------



import  wx


def OnOtherColor(self, event):
        '''
        使用颜色对话框
        '''
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)   #创建颜色对象数据
        if dlg.ShowModal() == wx.ID_OK:
            self.paint.SetColor(dlg.GetColourData().GetColour()) #根据选择设置画笔颜色
        dlg.Destroy()