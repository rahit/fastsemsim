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

class StatusGui:
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		self.panel = self.parentobj.panel
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.parentobj.status_box.Add(self.mainbox)

		self.components_status = wx.FlexGridSizer(rows = 5, cols = 2, vgap = 6, hgap = 20)

		# Descbox
		self.go_status_label = wx.StaticText(self.panel, label='Gene Ontology')
		self.go_status_label.SetFont(self.parentobj.font)
		self.ac_status_label = wx.StaticText(self.panel, label='Annotation Corpus')
		self.ac_status_label.SetFont(self.parentobj.font)
		self.operation_status_label = wx.StaticText(self.panel, label='Operation')
		self.operation_status_label.SetFont(self.parentobj.font)
		self.query_status_label = wx.StaticText(self.panel, label='Query')
		self.query_status_label.SetFont(self.parentobj.font)
		self.output_status_label = wx.StaticText(self.panel, label='Output parameters')
		self.output_status_label.SetFont(self.parentobj.font)
		self.go_status_pic = wx.StaticBitmap(self.parentobj.panel)
		self.ac_status_pic = wx.StaticBitmap(self.parentobj.panel)
		self.query_status_pic = wx.StaticBitmap(self.parentobj.panel)
		self.operation_status_pic = wx.StaticBitmap(self.parentobj.panel)
		self.output_status_pic = wx.StaticBitmap(self.parentobj.panel)
		#self.parentobj.SetGoOk(False)
		self.components_status.AddMany([(self.go_status_label), (self.go_status_pic), (self.ac_status_label), (self.ac_status_pic), (self.operation_status_label), (self.operation_status_pic), (self.query_status_label), (self.query_status_pic), (self.output_status_label), (self.output_status_pic)])

		self.mainbox.Add(self.components_status, flag=wx.UP|wx.DOWN|wx.LEFT|wx.RIGHT, border=5)