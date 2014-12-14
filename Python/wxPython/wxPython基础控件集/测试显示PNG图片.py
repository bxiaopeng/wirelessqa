#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wx  #导入必须的wxPython包

class Frame(wx.Frame): #2. 定义自己的Frame类作为wx.Frame的子类
	#3. 图像参数
	def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title='Hello,老毕!'):
		#4. 显示图像
		temp = image.ConvertToBitmap()
		size = temp.GetWidth(),temp.GetHeight()
		wx.Frame.__init__(self,parent,id,title,pos,size)
		self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)

class App(wx.App): #5. 子类化wxPython应用程序类

	def OnInit(self): #定义一个应用程序初始化方法
		#6. 图像处理
		image = wx.Image('wirelessqa.png',wx.BITMAP_TYPE_PNG)
		self.frame = Frame(image)
		self.frame.Show()
		self.SetTopWindow(self.frame) #可选方法,它让wxPython方法知道哪个框架或对话框将被认为是主要的
		return True

def main(): #7
	app = App()
	app.MainLoop()		

if __name__=='__main__':
	main()