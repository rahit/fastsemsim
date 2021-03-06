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

#from wx.Python.wx import *
import wx

class OutputGui(wx.Frame):
	def_size = (300,600)
	
	def __init__(self, parent):
		self.parentobj = parent
		super(OutputGui, self).__init__(self.parentobj, title="Output", size=self.def_size)
		self.InitUI()
	
	def InitUI(self):
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.output_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Output')
		self.output_box = wx.StaticBoxSizer(self.output_boxline, wx.VERTICAL)
		self.output_field = wx.TextCtrl(self.panel, size=self.def_size, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
		self.output_box.Add(self.output_field, flag=wx.EXPAND)
		self.mainbox.Add(self.output_box, flag=wx.EXPAND)

	def OnQuit(self, event):
		self.Hide()
		