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
from gui import WorkProcess
import os 

class OutputCtrlGui():
	def __init__(self, parent):
		self.parent = parent
		self.InitUI()
	
	def InitUI(self):
		self.InitMainUI()
		
	def InitMainUI(self):
		#------------------------------------------------------------------------------------------------------------------
		self.mainbox = wx.BoxSizer(wx.HORIZONTAL)
		self.parent.outputctrl_box.Add(self.mainbox)

		self.check_output2file = wx.CheckBox(self.parent.panel, wx.ID_ANY, 'Redirect output to file:', (10,10))
		self.label_outputfile = wx.StaticText(self.parent.panel, label = '')
		self.button_outputfile = wx.Button(self.parent.panel, wx.ID_ANY, 'Select file...')

		self.mainbox.Add(self.check_output2file, flag= wx.EXPAND  | wx.RIGHT| wx.CENTER , border=30)
		self.mainbox.Add(self.label_outputfile, flag= wx.EXPAND  | wx.RIGHT| wx.CENTER , border=30)
		self.mainbox.Add(self.button_outputfile, flag= wx.EXPAND | wx.CENTER | wx.RIGHT, border=30)

		self.parent.Bind(wx.EVT_CHECKBOX, self.OnToFile, id=self.check_output2file.GetId())
		self.parent.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.button_outputfile.GetId())
		
		self.OnReset()

	def OnReset(self):
		self.parent.output_type = WorkProcess.OUTPUT_TO_GUI
		self.check_output2file.SetValue(False)
		self.parent.output_file = None
		self.label_outputfile.SetLabel('None specified')
		self.label_outputfile.Disable()
		self.button_outputfile.Disable()
		self.OnUpdate()
	
	def OnUpdate(self):
		if self.parent.output_type == WorkProcess.OUTPUT_TO_GUI:
			self.parent.SetOutputCtrlOk(True)
		elif self.parent.output_type == WorkProcess.OUTPUT_TO_FILE and not self.parent.output_file == None:
			self.parent.SetOutputCtrlOk(True)
			self.label_outputfile.SetLabel(os.path.basename(self.parent.output_file))
		else:
			self.parent.SetOutputCtrlOk(False)

		self.parent.lock()
		self.parent.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_OUTPUT, self.parent.output_type, self.parent.output_file, None, None))
		data = self.parent.ssprocess2gui_queue.get()
		self.parent.unlock()

#------------------------------------------------------------------------------------------------------------------

	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.SAVE|wx.OVERWRITE_PROMPT)
		if dialog.ShowModal() == wx.ID_OK:
			self.parent.output_file = dialog.GetPath()
		self.OnUpdate()

	def OnToFile(self, event):
		if self.check_output2file.GetValue():
			self.button_outputfile.Enable()
			self.label_outputfile.Enable()
			self.parent.output_type = WorkProcess.OUTPUT_TO_FILE
		else:
			self.button_outputfile.Disable()
			self.label_outputfile.Disable()
			self.parent.output_type = WorkProcess.OUTPUT_TO_GUI
		self.OnUpdate()

#--------------------------------------------------------------
# Utilities to set front-end values
	#def set_output_type(self, ot):
		#if ot == 1:
			#self.check_output2file.SetValue(True)
		#elif ot == 0:
			#self.check_output2file.SetValue(False)
		#self.OnToFile(None)
