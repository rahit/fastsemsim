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
from fastSemSim.GO import GeneOntology
from fastSemSim.GO import AnnotationCorpus
from fastSemSim.SemSim import SemSimMeasures

class ControlGui:
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		self.panel = self.parentobj.panel
		self.mainbox = wx.BoxSizer(wx.HORIZONTAL)
		self.parentobj.control_box.Add(self.mainbox)

		#Control zone
		self.commandbox = wx.BoxSizer(wx.VERTICAL)
		self.parentobj.start_cmd = wx.Button(self.panel, wx.ID_ANY, 'Start')
		self.parentobj.exit_cmd = wx.Button(self.panel, wx.ID_ANY, 'Exit')
		self.commandbox.Add(self.parentobj.start_cmd)
		self.commandbox.Add(self.parentobj.exit_cmd)
		self.parentobj.Bind(wx.EVT_BUTTON, self.OnStartCmd, id=self.parentobj.start_cmd.GetId())
		self.parentobj.Bind(wx.EVT_BUTTON, self.OnExitCmd, id=self.parentobj.exit_cmd.GetId())
		
		# Log Zone
		self.logboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Log')
		self.logbox = wx.StaticBoxSizer(self.logboxline, wx.VERTICAL)
		self.parentobj.log_field = wx.TextCtrl(self.parentobj.panel, size=(470,80), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
		self.logbox.Add(self.parentobj.log_field, flag=wx.EXPAND)
		self.parentobj.progress = wx.Gauge(self.panel, -1, 50, size=(250, 25))
		self.logbox.Add(self.parentobj.progress, flag=wx.EXPAND | wx.TOP, border = 5)
		
		self.mainbox.Add(self.commandbox, flag=wx.EXPAND | wx.ALL, border = 15)
		self.mainbox.Add(self.logbox, flag=wx.EXPAND)

	def OnExitCmd(self, event):
		self.parentobj.Close()

	def OnStartCmd(self, event):
		if self.parentobj.status == 1: # Ready. Not Running
			self.parentobj.start()
		elif self.parentobj.status == 2: # running
			self.parentobj.stop() # set to not running and stops thread
		elif self.parentobj.status == 0: # Not ready. Should not be active.
			self.parentobj.activateGoCmd()