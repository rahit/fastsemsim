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
#from SSmeasures import *

class QueryGui:
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		self.parentobj.query_ok = True
		#self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
		#font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		#font.SetPointSize(9)
        
		#self.panel = wx.Panel(self)
		self.mainbox = self.parentobj.query_box
		self.panel = self.parentobj.panel

		#Pairs section
		self.mainsubbox = wx.BoxSizer(wx.HORIZONTAL)
		
		#Pairs input type
		self.listchooserboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Input format')
		self.listchooserbox = wx.StaticBoxSizer(self.listchooserboxline, wx.HORIZONTAL)
		self.pairinputtypes = ['pairs','list']
		self.radio_pairs = wx.RadioButton(self.panel, wx.ID_ANY, self.pairinputtypes[0], (10, 10), style=wx.RB_GROUP)
		self.radio_list = wx.RadioButton(self.panel, wx.ID_ANY, self.pairinputtypes[1], (10, 10))
		self.listchooserbox.Add(self.radio_pairs,wx.EXPAND)
		self.listchooserbox.Add(self.radio_list,wx.EXPAND)
		self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_pairs.GetId())
		self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_list.GetId())
		self.parentobj.query_type = 0 # from field
		
		#Pairs input src
		self.listsrcboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Query')
		self.listsrcbox = wx.StaticBoxSizer(self.listsrcboxline, wx.HORIZONTAL)
		self.inputfield = wx.TextCtrl(self.panel, size=(250,150), style = wx.TE_MULTILINE)
		#self.parentobj.Bind(wx.wx.EVT_COMMAND_TEXT_UPDATED, self.OnTextChange(), self.inputfield.GetId())
		self.listsrcbox.Add(self.inputfield)
		
		self.inputcommands = wx.BoxSizer(wx.VERTICAL)
		self.clear = wx.Button(self.panel, wx.ID_ANY, 'Clear')
		self.filechooser = wx.Button(self.panel, wx.ID_ANY, 'Load from file...')

		self.fromaccmd = wx.CheckBox(self.panel, wx.ID_ANY, 'From Annotation Corpus', (10,10))
		#self.fromfile = wx.CheckBox(self.panel, wx.ID_ANY, 'From File', (10,10))
		self.parentobj.Bind(wx.EVT_CHECKBOX, self.OnFromAC, id=self.fromaccmd.GetId())
		#self.parentobj.Bind(wx.EVT_CHECKBOX, self.OnFromFile, id=self.fromfile.GetId())
		self.fromaccmd.SetValue(False)
		self.fromaccmd.Disable()
		#self.fromfile.Hide()
		
		self.parentobj.Bind(wx.EVT_BUTTON, self.OnClear, id=self.clear.GetId())
		self.parentobj.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		self.parentobj.Bind(wx.EVT_TEXT, self.OnFieldChange, id=self.inputfield.GetId())
		self.inputcommands.Add(self.listchooserbox, flag=wx.BOTTOM|wx.TOP, border=10)
		self.inputcommands.Add(self.fromaccmd)
		#self.inputcommands.Add(self.fromfile)
		self.inputcommands.Add(self.filechooser)
		self.inputcommands.Add(self.clear)
		
		self.mainsubbox.Add(self.listsrcbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainsubbox.Add(self.inputcommands, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
#------------------------------------------------------------------------------------------------------------------
		self.mainbox.Add(self.mainsubbox, flag=wx.EXPAND)
		self.parentobj.query_from = 0
		self.parentobj.SetQueryOk(False)
#------------------------------------------------------------------------------------------------------------------
	def OnFieldChange(self, event):
		if str(self.inputfield.GetValue()) == "":
			pass
		self.CheckIfOk()
		#print "a"

	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.inputfield.Disable()
			self.parentobj.query_file = dialog.GetPath()
			self.inputfield.SetValue("Data will be loaded from " + str(self.parentobj.query_file))
			self.parentobj.query_from = 1 # from file
			self.fromaccmd.SetValue(False)
			self.parentobj.upload_query = True
		self.CheckIfOk()

	def OnFromAC(self, event):
		if self.fromaccmd.GetValue():
			self.inputfield.Disable()
			self.parentobj.query_from = 2 # from ac
			self.inputfield.SetValue("Data will be loaded from Annotation Corpus")
		else:
			self.inputfield.Enable()
			self.inputfield.SetValue("")
			self.parentobj.query_from = 0 # from field
		self.parentobj.upload_query = True
		self.CheckIfOk()

	def OnClear(self, event):
		self.inputfield.SetValue('')
		self.fromaccmd.SetValue(False)
		self.inputfield.Enable()
		self.parentobj.query_file = None
		#self.parentobj.query_from_ac = False
		self.parentobj.query_from = 0 # field
		self.parentobj.upload_query = True
		self.CheckIfOk()

	def OnTypeSelect(self, event):
		self.parentobj.upload_query = True
		if self.radio_pairs.GetValue():
			self.parentobj.query_type = 0
			if self.parentobj.query_from == 2:
				self.parentobj.query_from_ac = False
				self.parentobj.query_from = 0
				self.inputfield.SetValue("")
				self.inputfield.Enable()
			self.fromaccmd.Disable()
			self.fromaccmd.SetValue(False)
		elif self.radio_list.GetValue():
			self.parentobj.query_type = 1
			self.fromaccmd.Enable()
		self.CheckIfOk()

	def OnTextChange(self, event):
		self.parentobj.upload_query = True
	
	def CheckIfOk(self):
		if self.parentobj.query_from == 2:
			self.parentobj.SetQueryOk(True)
		elif self.parentobj.query_from == 0:
			print "A"
			if str(self.inputfield.GetValue()) == "":
				print "B"
				self.parentobj.SetQueryOk(False)
			else:
				print "C"
				self.parentobj.SetQueryOk(True)
		elif self.parentobj.query_from == 1:
			if self.parentobj.query_file is None:
				self.parentobj.SetQueryOk(False)
			else:
				 self.parentobj.SetQueryOk(True)
		else:
			self.parentobj.SetQueryOk(False)
 