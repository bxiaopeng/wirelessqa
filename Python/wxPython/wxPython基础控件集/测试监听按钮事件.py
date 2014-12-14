# -*- coding:utf-8 -*-

#自定义的事 件TwoButtonEvent仅当用户敲击了这两个按钮之后被触发。这个事件包含了一 个关于用户在该部件上敲击次数的计数。

import wx

class TwoButtonEvent(wx.PyCommandEvent): #1.定义事件
	def __init__(self,evtType,id):
		wx.PyCommandEvent.__init__(self,evtType,id)
		self.clickCount = 0

	def GetClickCount(self):
		return self.clickCount

	def SetClickCount(self,count):
		self.clickCount = count

"""
全局函数wx.NewEventType()的作用类似于wx.NewId();它返回一个唯 一的事件类型ID。这个唯一的值标识了一个应用于事件处理系统的事件类型
"""
myEVT_TWO_BUTTON = wx.NewEventType()	#2. 创建一个事件类型	

EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON,1) #3. 创建一个绑定器对象

class TwoButtonPanel(wx.Panel):
	
	def __init__(self,parent,id= -1,leftText="左",rightText="右"):
		wx.Panel.__init__(self,parent,id)
		self.leftButton = wx.Button(self,label = leftText)
		self.rightButton = wx.Button(self,label = rightText,pos = (100,0))
		self.leftClick = False
		self.rightClick = False
		self.clickCount = 0

		#4. 下面两行绑定更低级的事件

		"""
		为了创建这个新的更高级的命令事件,程序必需响应特定的用户事件,
		例如,在每个按钮对象上的鼠标左键按下。依据哪个按钮被敲击,该事件被绑定到OnLeftClick()和OnRightClick()方法。
		处理器设置了布尔值,以表明按键是否被敲击
		"""
		self.leftButton.Bind(wx.EVT_LEFT_DOWN,self.OnLeftClick)
		self.rightButton.Bind(wx.EVT_LEFT_DOWN,self.OnRightClick)

	"""
	#5 #6 Skip()的调用允许在该事件处理完成后的进一步处理。
	在这里,这个 新的事件不需要skip调用;它在事件处理器完成之前被分派了(self.OnClick())。 
	但是所有的鼠标左键按下事件需要调用Skip(),以便处理器不把最后的按钮敲击挂起。
	这个程序没有处理按钮敲击事件,但是由于使用了Skip(),wxPython 在敲击期间使用按钮敲击事件来正确地绘制按钮。
	如果被挂起了,用户将不会 得到来自按钮按下的反馈。
	"""	

	def OnLeftClick(self,event):
		self.leftClick = True
		self.OnClick()
		event.Skip() #5. 继续处理

	def OnRightClick(self,event):
		self.rightClick = True
		self.OnClick()
		event.Skip() #6. 继续处理

	def OnClick(self):
		self.clickCount += 1
		if self.leftClick and self.rightClick:
			self.leftClick = False
			self.rightClick = False
			"""
			如果两个按钮都被敲击了,该代码创建这个新事件的一个实例。
			事件类 型和两个按钮的ID作为构造器的参数。
			通常,一个事件类可以有多个事件类 型,尽管本例中不是这样
			"""
			evt = TwoButtonEvent(myEVT_TWO_BUTTON,self.GetId()) #7. 创建自定义事件
			evt.SetClickCount(self.clickCount) #添加数据到事件
			##8 ProcessEvent()的调用将这个新事件引入到事件处理系统中
			#GetEventHandler()调用返回wx.EvtHandler 的一个实例。
			#大多数情况下,返回的实例是窗口部件对象本身,但是如果其它 的wx.EvtHandler()方法已经被压入了事件处理器堆栈,那么返回的将是堆栈项 的项目。
			self.GetEventHandler().ProcessEvent(evt) #8. 处理事件

class CustomEventFrame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'点击数量:0',size=(300,100))
		panel = TwoButtonPanel(self)
		self.Bind(EVT_TWO_BUTTON,self.OnTwoClick,panel)# 9.绑定自定义事件

	def OnTwoClick(self,event): #10. 定义一个事件处理器函数,用来显示窗口的标题以显示敲击数
		self.SetTitle("Click Count:%s " % event.GetClickCount())

if __name__=='__main__':
	app = wx.App()
	frame = CustomEventFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()

