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
from GO import GeneOntology
from GO import AnnotationCorpus

class OutputCtrlGui():
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		self.panel = self.parentobj.panel
		self.mainbox = self.parentobj.outputctrlbox
		self.commandsbox = wx.BoxSizer(wx.VERTICAL)
#------------------------------------------------------------------------------------------------------------------
		self.destinationboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Output destination')
		self.destinationbox= wx.StaticBoxSizer(self.destinationboxline, wx.VERTICAL)
		self.outputtypes = ['output field','file']
		self.radio_field = wx.RadioButton(self.panel, wx.ID_ANY, self.outputtypes[0], (10, 10), style=wx.RB_GROUP)
		self.radio_file = wx.RadioButton(self.panel, wx.ID_ANY, self.outputtypes[1], (10, 10))
		self.destinationbox.Add(self.radio_field,wx.EXPAND)
		self.destinationbox.Add(self.radio_file,wx.EXPAND)
		self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_field.GetId())
		self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_file.GetId())
		self.parentobj.output_type = 0
		self.parentobj.SetOutputCtrlOk(True)

		self.commandsline  = wx.StaticBox(self.panel, wx.ID_ANY, 'Output file')
		self.commands = wx.StaticBoxSizer(self.commandsline, wx.VERTICAL)
		self.outputlabel = wx.StaticText(self.panel, label = 'Not selected')
		self.outputlabel.SetFont(self.parentobj.font)
		self.filechooser = wx.Button(self.panel, wx.ID_ANY, 'Choose file...')
		self.filechooser.Disable()
		self.parentobj.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		self.commands.Add(self.outputlabel, flag=wx.BOTTOM|wx.TOP, border=10)
		self.commands.Add(self.filechooser)
		
		#Output zone
		self.outputline = wx.StaticBox(self.parentobj.panel, wx.ID_ANY, 'Output')
		self.outputbox = wx.StaticBoxSizer(self.outputline, wx.HORIZONTAL)
		self.parentobj.outputfield = wx.TextCtrl(self.parentobj.panel, size=(450,130), style = wx.TE_MULTILINE|wx.TE_READONLY)
		self.outputbox.Add(self.parentobj.outputfield, flag=wx.EXPAND)
		
		self.commandsbox.Add(self.destinationbox)
		self.commandsbox.Add(self.commands)
		self.mainbox.Add(self.commandsbox)
		self.mainbox.Add(self.outputbox)
#------------------------------------------------------------------------------------------------------------------

	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.SAVE|wx.OVERWRITE_PROMPT)
		if dialog.ShowModal() == wx.ID_OK:
			self.parentobj.output_file = dialog.GetPath()
			self.outputlabel.SetLabel(self.parentobj.output_file)
			self.parentobj.SetOutputCtrlOk(True)
			#self.parentobj.mainbox.Fit()

	def OnTypeSelect(self, event):
		if self.radio_field.GetValue():
			self.parentobj.output_type = 0 # text field
			self.filechooser.Disable()
			self.parentobj.SetOutputCtrlOk(True)
			#self.fromaccmd.Disable()
		elif self.radio_file.GetValue():
			self.parentobj.output_type = 1 # file 
			if self.parentobj.output_file == None:
				self.parentobj.SetOutputCtrlOk(False)
			self.filechooser.Enable()
