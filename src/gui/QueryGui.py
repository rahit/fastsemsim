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

import os
import wx
#from GO import GeneOntology
#from GO import AnnotationCorpus
from gui import WorkProcess

class QueryGui:
	def __init__(self, parent):
		self.parent = parent
		self.InitUI()
	
	def InitUI(self):
		self.parent.query_ok = True
		self.mainbox = self.parent.query_box
		self.panel = self.parent.panel

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
		
		#Pairs input src
		self.listsrcboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Query')
		self.listsrcbox = wx.StaticBoxSizer(self.listsrcboxline, wx.HORIZONTAL)
		self.text_query = wx.TextCtrl(self.panel, size=(250,150), style = wx.TE_MULTILINE)
		#self.parent.Bind(wx.wx.EVT_COMMAND_TEXT_UPDATED, self.OnTextChange(), self.text_query.GetId())
		self.listsrcbox.Add(self.text_query)
		
		self.inputcommands = wx.BoxSizer(wx.VERTICAL)
		self.clear = wx.Button(self.panel, wx.ID_ANY, 'Clear')
		self.filechooser = wx.Button(self.panel, wx.ID_ANY, 'Load from file...')

		self.check_fromac = wx.CheckBox(self.panel, wx.ID_ANY, 'From Annotation Corpus', (10,10))
		self.inputcommands.Add(self.listchooserbox, flag=wx.BOTTOM|wx.TOP, border=10)
		self.inputcommands.Add(self.check_fromac)
		self.inputcommands.Add(self.filechooser)
		self.inputcommands.Add(self.clear)
		
		self.mainsubbox.Add(self.listsrcbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainsubbox.Add(self.inputcommands, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
#------------------------------------------------------------------------------------------------------------------
		self.mainbox.Add(self.mainsubbox, flag=wx.EXPAND)

		self.parent.Bind(wx.EVT_CHECKBOX, self.OnFromAC, id=self.check_fromac.GetId())
		self.parent.Bind(wx.EVT_BUTTON, self.OnClear, id=self.clear.GetId())
		self.parent.Bind(wx.EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		self.parent.Bind(wx.EVT_TEXT, self.OnFieldChange, id=self.text_query.GetId())
		self.parent.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_pairs.GetId())
		self.parent.Bind(wx.EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_list.GetId())
		
		#self.parent.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_QUERY, WorkProcess.QUERYFROMGUI))

		self.OnReset()
#------------------------------------------------------------------------------------------------------------------

	def OnReset(self):
		self.parent.query_from = WorkProcess.QUERY_FROM_GUI
		self.parent.query_type = WorkProcess.QUERY_LIST
		self.parent.query_file = None
		self.parent.query = None
		self.check_fromac.SetValue(False)
		self.radio_list.SetValue(True)
		self.text_query.Enable()
		self.text_query.SetValue("")
		self.CheckIfOk()

	def OnClear(self, event):
		self.OnReset()
		
	def OnFieldChange(self, event):
		if str(self.text_query.GetValue()) == "":
			pass
		self.CheckIfOk()

	def OnFileBrowse(self, event):
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.parent.query_file = dialog.GetPath()
			self.OnFromFile(None)

	def OnFromFile(self, event):
		self.text_query.Disable()
		self.text_query.SetValue("The query will be loaded from " + str(self.parent.query_file))
		self.parent.query_from = WorkProcess.QUERY_FROM_FILE
		self.check_fromac.SetValue(False)
		self.CheckIfOk()
		
	def OnFromAC(self, event):
		if self.check_fromac.GetValue():
			self.parent.query_from = WorkProcess.QUERY_FROM_AC
			self.radio_list.SetValue(True)
			self.text_query.Disable()
			self.text_query.SetValue("The query will be loaded from the Annotation Corpus.")
			self.parent.query_file = None
			self.CheckIfOk()
		else:
			self.text_query.Enable()
			self.text_query.SetValue("")
			self.parent.query_from = WorkProcess.QUERY_FROM_GUI
		self.CheckIfOk()

	def OnTypeSelect(self, event):
		if self.radio_pairs.GetValue():
			self.parent.query_type = WorkProcess.QUERY_PAIRS
			if self.parent.query_from == WorkProcess.QUERY_FROM_AC:
				self.check_fromac.SetValue(False)
				self.OnFromAC(None)
			else:
				pass
			self.check_fromac.SetValue(False)
		elif self.radio_list.GetValue():
			self.parent.query_type = WorkProcess.QUERY_PAIRS
		self.CheckIfOk()

	def OnTextChange(self, event):
		self.CheckIfOk()
	
	def CheckIfOk(self):
		good = True
		if self.parent.query_from == WorkProcess.QUERY_FROM_AC:
			self.parent.SetQueryOk(True)
		elif self.parent.query_from == WorkProcess.QUERY_FROM_GUI:
			if str(self.text_query.GetValue()) == "":
				self.parent.SetQueryOk(False)
				good = False
			else:
				self.parent.SetQueryOk(True)
		elif self.parent.query_from == WorkProcess.QUERY_FROM_FILE:
			if self.parent.query_file is None:
				self.parent.SetQueryOk(False)
				good = False
			else:
				 self.parent.SetQueryOk(True)
		else:
			self.parent.SetQueryOk(False)
			good = False
		if good:
			self.parent.lock()
			self.parent.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_QUERY, self.parent.query_from, self.parent.query_type, self.parent.query_file))
			self.parent.unlock()
 
 #--------------------------------------------------------------
# Utilities to set front-end values
	def set_query_format(self, qform):
		if qform == 0: #pairs
			self.radio_pairs.SetValue(True)
			self.radio_list.SetValue(False)
		elif qform == 1:
			self.radio_pairs.SetValue(False)
			self.radio_list.SetValue(True)
		self.OnTypeSelect(None)

	def set_query_from(self, qfrom):
		if qfrom == 2: # from ac
			self.check_fromac.Enable()
			self.check_fromac.SetValue(True)
			self.OnFromAC(None)
		elif qfrom == 0: # from field
			self.check_fromac.Enable()
			self.check_fromac.SetValue(False)
		elif qfrom == 1: # from file
			self.check_fromac.Enable()
			self.check_fromac.SetValue(False)
			self.OnFromFile(None)
