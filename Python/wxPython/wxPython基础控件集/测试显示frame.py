#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import sys

class Frame(wx.Frame):

	def __init__(self,parent,id,title):
		print "Frame __init__"
		wx.Frame.__init__(self,parent,id,title)


class App(wx.App):
	
	def __init__(self,redirect=True,filename=None):
		print "App __init__"
		wx.App.__init__(self,redirect,filename)

	def OnInit(self):
		print "OnInit"	#输出到stdout
		self.frame = Frame(parent=None,id=-1,title='Startup') #创建框架
		self.frame.Show()
		self.SetTopWindow(self.frame)
		print >>sys.stderr,"假装的错误信息" #输出到stderr
		return True
	def OnExit(self):
		print "OnExit"

if __name__=='__main__':
	# app = App(redirect = True) #重定向输出到新框架
	# app = App(redirect = False)
	app = App(True,"output")
	print "MainLoop之前"
	app.MainLoop()
	print "MainLoop之后"