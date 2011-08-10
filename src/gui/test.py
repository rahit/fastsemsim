# -*- coding: iso-8859-1 -*-
'''
Copyright 2011 Marco Mina. All rights reserved.

This file is part of fastSemSim

fastSemSim is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fastSemSim is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fastSemSim.  If not, see <http://www.gnu.org/licenses/>.
'''

#!/usr/bin/python

# staticbox.py

import wx

class MyDialog(wx.Frame):
    def __init__(self, parent, id, title):
        super(MyDialog,self).__init__(parent, id, title, size=(260, 250))
       
        wx.StaticBox(self, -1, 'Personal Info', (5, 5), size=(240, 170))
       
        wx.CheckBox(self, -1 ,'Male', (15, 30))
        wx.CheckBox(self, -1 ,'Married', (15, 55))
        wx.StaticText(self, -1, 'Age', (15, 95))
        wx.SpinCtrl(self, -1, '1', (55, 90), (60, -1), min=1, max=120)
        wx.Button(self, 1, 'Ok', (90, 185), (60, -1))

        self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)

        self.Centre()
        #self.ShowModal()
        self.Show()
        #self.Destroy()

    def OnClose(self, event):
        self.Close()

app = wx.App(0)
MyDialog(None, -1, 'staticbox.py')
app.MainLoop()

#import wx

#frame = None

#def OnQuit(event):
	##print event
	#frame.Close()


#app = wx.App()
#frame = wx.Frame(None, -1, "fastSemSim src", size=(500,500))
#frame.Show()
#menubar = wx.MenuBar()
#file = wx.Menu()
#quit = wx.MenuItem(file, 1, '&Quit\tCtrl+Q')
##quit.SetBitmap(wx.Bitmap('icons/exit.png'))
#file.AppendItem(quit)
#menubar.Append(file, '&File')
#frame.SetMenuBar(menubar)
#frame.Bind(wx.EVT_MENU, OnQuit, id=1)
#dialog = wx.FileDialog(None, style = wx.OPEN)
#if dialog.ShowModal() == wx.ID_OK:
	#print 'Selected: ', dialog.GetPath()
#dialog.Destroy()
#app.MainLoop()

