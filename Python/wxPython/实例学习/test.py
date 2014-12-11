#!/usr/bin/python
# -*- coding:utf-8 -*- 
# ---------------------------------------------------------------------------
#  File:         ''
#  Description:  
#
#  Date:         '14-12-11 16:28'
#  Author:       'bixiaopeng'
#  Tags:         from : http://www.cnblogs.com/xiaowuyi/archive/2012/04/05/2432862.html
#---------------------------------------------------------------------------

'''
eml阅读器 V1.0
小五义：http://www.cnblogs.com/xiaowuyi
仍然存在问题：
1、收件人很多时，窗口格式会发生错乱
2、附件有多个时，只能显示一个
3、eml另存为时，附件只能保存一个
'''


import wx
import wx.html
import os
import email
import re
import shutil

wildcard = "note source (*.eml)|*.eml"
psfname='无'  #附件名

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICLINE1,
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3,wxID_FRAME1TEXTCTRL1, wxID_FRAME1HTMLWINDOW1,wxID_FRAME1BUTTON2
] = [wx.NewId() for _init_ctrls in range(10)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):

        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(269, 142), size=wx.Size(899, 599),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Eml文件阅读器 V1.0')
        self.SetClientSize(wx.Size(891, 565))
        self.Enable(True)
        self.SetIcon(wx.Icon(u'mb_4.ico', wx.BITMAP_TYPE_ICO))  #当前目录下放一个名为mb_4.ico的文件做图标

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(891, 565),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(120, 16), size=wx.Size(632, 23),
              style=0, value=u'')
        self.textCtrl1.SetEditable(False)


        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'浏览',
              name='button1', parent=self.panel1, pos=wx.Point(776, 16),
              size=wx.Size(75, 23), style=0)
        self.button1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'文件名:', name='staticText1', parent=self.panel1,
              pos=wx.Point(45, 16), size=wx.Size(56, 23), style=0)
        self.staticText1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.htmlWindow1 = wx.html.HtmlWindow(id=wxID_FRAME1HTMLWINDOW1,
              name='htmlWindow1', parent=self.panel1, pos=wx.Point(72, 186),
              size=wx.Size(747, 300), style=wx.html.HW_SCROLLBAR_AUTO|wx.DOUBLE_BORDER)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u' 发件人:\n 日    期:\n 收件人:\n 主    题:\n', name='staticText2', parent=self.panel1,
              pos=wx.Point(72, 80), size=wx.Size(747, 90), style=wx.html.HW_SCROLLBAR_AUTO)
        self.staticText2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u' 附    件:', name='staticText3', parent=self.panel1,
              pos=wx.Point(72, 496), size=wx.Size(680, 14), style=0)
        self.staticText3.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(0, 55),
              size=wx.Size(891, 2), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'导出',
              name='button2', parent=self.panel1, pos=wx.Point(776, 496),
              size=wx.Size(75, 23), style=0)
        self.button2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)


    def __init__(self, parent):
        self._init_ctrls(parent)



    def reademail(self):#read email
        global psfname
        checkfile=True
        p=''  #记录邮件html正文
        txtemail=''#记录邮件txt正文
        eto=''

        filename=self.textCtrl1.GetValue()
        try:
            emailfile=open(filename,'rb')
            msg=email.message_from_file(emailfile)
            subject=msg.get('subject')
            head=email.Header.Header(subject)
            dhead=email.Header.decode_header(head)
            subject=dhead[0][0]
            efrom=email.utils.parseaddr(msg.get("from"))[1]
            etime=msg.get("date")
            #判断收件人个数

            print msg.get("to")
            for tolines in msg.get("to").splitlines():
                findst=tolines.find('<')  #从to中找<位置
                if findst==-1:
                    eto=email.utils.parseaddr(msg.get("to"))[1]
                else:
                    eto=eto+tolines[findst:]+'\n'

            #eto=email.utils.parseaddr(msg.get("to"))[1]
            ehead=' 发件人:'+efrom+'\n'+' 日   期:'+etime+'\n'+' 收件人:'+eto+'\n'+' 主   题:'+subject+'\n'

            for bodycheck in msg.walk():
                if not bodycheck.is_multipart():
                    psname = bodycheck.get_param("name")

                    if psname:
                        psh = email.Header.Header(psname)
                        psdh = email.Header.decode_header(psh)
                        psfname = psdh[0][0]

                        data = bodycheck.get_payload(decode=True)

                        try:
                            f = open(psfname, 'wb')
                        except:
        #
                            f = open('tempps', 'wb')

                        f.write(data)
                        f.close()
                    else:
                        data=bodycheck.get_payload(decode=True)
                        p=str(data)

            emailend=ehead
            self.staticText2.SetLabel(emailend)
            self.staticText3.SetLabel(' 附    件：'+psfname)

            self.htmlWindow1.SetPage(p)
            txtemail=emailend+'正文：'+p
            checkfile=False
        except:

            tishi='文件'+'格式错误！'
            wx.MessageBox(tishi,'注意',wx.OK)

        tem=open('temps','w')   # 临时文件存放


        lamp='<DIV>'+txtemail+'</DIV><DIV>'+' 附    件：'+psfname
        lamp=lamp.replace('\n','</DIV><DIV>')
        tem.write(lamp)

        tem.close()

    def OnButton1Button(self, event):  #浏览
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(),"", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            aa=dialog.GetPath().encode('utf-8')
            self.textCtrl1.SetValue(aa.decode('utf-8'))
            self.reademail()
        dialog.Destroy()
        event.Skip()

    def savetotxt(self,filena):#邮件另存为txt文件
        resultfile=''
        read=file('temps').read()
        readf_con=read.replace('&nbsp;','\n')
        readf_con=readf_con.replace('&#187;','\n')
        readf_con=re.sub("<!--.+?-->",'\n',readf_con)
        readf_con=re.sub("<.*?>",'\n',readf_con)
        readf_con=re.sub('\n+','\n',readf_con)
        for tt in readf_con.splitlines():
            tt=tt.rstrip()+'\n'
            resultfile=resultfile+tt  #去除temps文件中多余的空行

        w=open(filena,'w')

        w.write(resultfile)
        w.close()


    def OnButton2Button(self, event):#eml另存为
        wid = "text file (*.txt)|*.txt"
        savedialog = wx.FileDialog(None, "Choose a file", os.getcwd(),"", wid, wx.SAVE)
        if savedialog.ShowModal() == wx.ID_OK:
            fil=savedialog.GetPath().encode('utf-8')
        savef=fil.decode('utf-8')
        savedialog.Destroy()
        savep=os.path.dirname(savef)

        #将附件另存到该目录下
        checkdot=psfname.find('.')
        if checkdot!= -1:#判断是否存在附件
            kzhname='ps'+psfname[checkdot:]
            psfile=os.path.join(savep,kzhname)
            shutil.copy(psfname, psfile)
        self.savetotxt(savef)#存eml正文

        event.Skip()




class App(wx.App):
    def OnInit(self):
        self.main=create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
def main():
    application=App(0)
    application.MainLoop()

if __name__=='__main__':
    main()