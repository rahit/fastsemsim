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
import wx

app = wx.PySimpleApp()

win_width = 364
win_height = 478

netlist = wx.Dialog(None, wx.ID_ANY, "Network List", wx.DefaultPosition, wx.Size(win_width-8, win_height-8), wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)

hszr = wx.BoxSizer(wx.HORIZONTAL)
vszr = wx.BoxSizer(wx.VERTICAL)
vszr2 = wx.BoxSizer(wx.VERTICAL)

sszr = wx.StaticBoxSizer(wx.StaticBox(netlist, wx.ID_ANY, "User Information", size=(300,300)), orient=wx.VERTICAL)
#fgszr = wx.FlexGridSizer(2)
prova = wx.Button(netlist, wx.ID_ANY, 'Manage GO...')
#sszr.Add(prova)
sszr.Add(prova, 0, wx.ALL|wx.CENTER, 25)
#fgszr.Add(wx.StaticText(sszr.GetStaticBox(), wx.ID_ANY, "Nick Name: ")) # Segmentation Fault

netlist.ShowModal()
