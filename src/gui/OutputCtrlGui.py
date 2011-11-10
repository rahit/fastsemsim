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
		#self.panel = self.parentobj.panel
		self.InitMainUI()
		
	def InitMainUI(self):
		#------------------------------------------------------------------------------------------------------------------
		self.mainbox = wx.BoxSizer(wx.HORIZONTAL)
		self.parentobj.outputctrl_box.Add(self.mainbox)

		#version 2
		self.output2file = wx.CheckBox(self.parentobj.panel, wx.ID_ANY, 'Redirect output to file', (10,10))
		self.parentobj.Bind(wx.EVT_CHECKBOX, self.OnToFile, id=self.output2file.GetId())
		self.output2file.SetValue(False)
		#self.outputfile_label = wx.StaticText(self.parentobj.panel, label = 'No file selected')
		#self.outputfile_label.SetFont(self.parentobj.font)
		
		#self.fileparams_boxline  = wx.StaticBox(self.panel, wx.ID_ANY, 'Output file parameters')
		#self.fileparams_box = wx.StaticBoxSizer(self.fileparams_boxline, wx.HORIZONTAL)
		#self.choosefile_cmd = wx.Button(self.parentobj.panel, wx.ID_ANY, 'Choose file...')
		#self.choosefile_cmd.Disable()
		#self.parentobj.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.choosefile_cmd.GetId())
		#self.fileparams_box.Add(self.choosefile_cmd, flag=wx.BOTTOM|wx.TOP, border=10)
		self.outputformat_cmd = wx.Button(self.parentobj.panel, wx.ID_ANY, 'Output file...')
		self.outputformat_cmd.Disable()
		self.parentobj.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.outputformat_cmd.GetId())
		#self.fileparams_box.Add(self.outputformat_cmd, flag=wx.BOTTOM|wx.TOP, border=10)
		
		self.mainbox.Add(self.output2file, flag= wx.EXPAND  | wx.RIGHT, border=30)
		#self.mainbox.Add(self.outputfile_label)
		self.mainbox.Add(self.outputformat_cmd)
		#version 1
		#self.destinationboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Output destination')
		#self.destinationbox= wx.StaticBoxSizer(self.destinationboxline, wx.HORIZONTAL)
		#self.outputtypes = ['output field','file']
		#self.radio_field = wx.RadioButton(self.panel, wx.ID_ANY, self.outputtypes[0], (10, 10), style=wx.RB_GROUP)
		#self.radio_file = wx.RadioButton(self.panel, wx.ID_ANY, self.outputtypes[1], (10, 10))
		#self.destinationbox.Add(self.radio_field,wx.EXPAND)
		#self.destinationbox.Add(self.radio_file,wx.EXPAND)
		#self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_field.GetId())
		#self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_file.GetId())
		#self.parentobj.output_type = 0
		#self.parentobj.SetOutputCtrlOk(True)

		#self.commandsline  = wx.StaticBox(self.panel, wx.ID_ANY, 'Output file')
		#self.commands = wx.StaticBoxSizer(self.commandsline, wx.HORIZONTAL)
		#self.outputlabel = wx.StaticText(self.panel, label = 'Not selected')
		#self.outputlabel.SetFont(self.parentobj.font)
		#self.filechooser = wx.Button(self.panel, wx.ID_ANY, 'Choose file...')
		#self.filechooser.Disable()
		#self.parentobj.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		#self.commands.Add(self.outputlabel, flag=wx.BOTTOM|wx.TOP, border=10)
		#self.commands.Add(self.filechooser)
		
		#self.mainbox.Add(self.destinationbox)
		#self.mainbox.Add(self.commands)
		self.parentobj.output_type = 0 # text field
		self.parentobj.SetOutputCtrlOk(True)
#------------------------------------------------------------------------------------------------------------------

	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.SAVE|wx.OVERWRITE_PROMPT)
		if dialog.ShowModal() == wx.ID_OK:
			self.parentobj.output_file = dialog.GetPath()
			#self.outputlabel.SetLabel(self.parentobj.output_file)
			self.parentobj.SetOutputCtrlOk(True)
			#self.parentobj.mainbox.Fit()

	def OnToFile(self, event):
		if self.output2file.GetValue():
			self.outputformat_cmd.Enable()
			#self.parentobj.query_from_ac = True
			self.parentobj.output_type = 1 # to file
			if self.parentobj.output_file == None:
				self.parentobj.SetOutputCtrlOk(False)
			else:
				self.parentobj.SetOutputCtrlOk(True)
		else:
			self.outputformat_cmd.Disable()
			#self.parentobj.query_from_ac = True
			self.parentobj.output_type = 0 # text field
			self.parentobj.SetOutputCtrlOk(True)

#--------------------------------------------------------------
# Utilities to set front-end values
	def set_output_type(self, ot):
		if ot == 1:
			self.output2file.SetValue(True)
		elif ot == 0:
			self.output2file.SetValue(False)
		self.OnToFile(None)
