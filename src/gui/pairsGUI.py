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

from wxPython.wx import *
from GO import GeneOntology
from GO import AnnotationCorpus
from SSmeasures import *

class PairsGUI:
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		self.parentobj.query_ok = True
		#self.Bind(EVT_CLOSE, self.OnQuit, id=self.GetId())
		#font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
		#font.SetPointSize(9)
        
		#self.panel = wxPanel(self)
		self.mainbox = self.parentobj.querybox
		self.panel = self.parentobj.panel

		#Pairs section
		self.mainsubbox = wxBoxSizer(wxHORIZONTAL)
		
		#Pairs input type
		self.listchooserboxline = wxStaticBox(self.panel, wxID_ANY, 'Input format')
		self.listchooserbox = wxStaticBoxSizer(self.listchooserboxline, wxHORIZONTAL)
		self.pairinputtypes = ['pairs','list']
		self.radio_pairs = wxRadioButton(self.panel, wxID_ANY, self.pairinputtypes[0], (10, 10), style=wxRB_GROUP)
		self.radio_list = wxRadioButton(self.panel, wxID_ANY, self.pairinputtypes[1], (10, 10))
		self.listchooserbox.Add(self.radio_pairs,wxEXPAND)
		self.listchooserbox.Add(self.radio_list,wxEXPAND)
		self.parentobj.Bind(EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_pairs.GetId())
		self.parentobj.Bind(EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_list.GetId())
		self.parentobj.query_type = 0
		
		#Pairs input src
		self.listsrcboxline = wxStaticBox(self.panel, wxID_ANY, 'Query')
		self.listsrcbox = wxStaticBoxSizer(self.listsrcboxline, wxHORIZONTAL)
		self.inputfield = wxTextCtrl(self.panel, size=(200,150), style = wxTE_MULTILINE)
		self.listsrcbox.Add(self.inputfield)
		
		self.inputcommands = wxBoxSizer(wxVERTICAL)
		self.clear = wxButton(self.panel, wxID_ANY, 'Clear')
		self.filechooser = wxButton(self.panel, wxID_ANY, 'Load from file...')

		self.fromaccmd = wxCheckBox(self.panel, wxID_ANY, 'From Annotation Corpus', (10,10))
		#self.fromfile = wxCheckBox(self.panel, wxID_ANY, 'From File', (10,10))
		self.parentobj.Bind(EVT_CHECKBOX, self.OnFromAC, id=self.fromaccmd.GetId())
		#self.parentobj.Bind(EVT_CHECKBOX, self.OnFromFile, id=self.fromfile.GetId())
		self.fromaccmd.SetValue(False)
		self.fromaccmd.Disable()
		#self.fromfile.Hide()
		
		self.parentobj.Bind(EVT_BUTTON, self.OnClear, id=self.clear.GetId())
		self.parentobj.Bind(EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		self.inputcommands.Add(self.listchooserbox, flag=wxBOTTOM|wxTOP, border=10)
		self.inputcommands.Add(self.fromaccmd)
		#self.inputcommands.Add(self.fromfile)
		self.inputcommands.Add(self.filechooser)
		self.inputcommands.Add(self.clear)
		
		self.mainsubbox.Add(self.listsrcbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		self.mainsubbox.Add(self.inputcommands, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
#------------------------------------------------------------------------------------------------------------------
		self.mainbox.Add(self.mainsubbox, flag=wxEXPAND)
#------------------------------------------------------------------------------------------------------------------
	def OnFileBrowse(self, event):
		dialog = wxFileDialog(None, style = wxOPEN)
		if dialog.ShowModal() == wxID_OK:
			self.parentobj.query_file = dialog.GetPath()
			self.inputfield.Disable()
			self.parentobj.query_from_ac = False
			self.fromaccmd.SetValue(False)
			self.inputfield.SetValue("Data will be loaded from " + self.parentobj.query_file)

	def OnFromAC(self, event):
		if self.fromaccmd.GetValue():
			self.inputfield.Disable()
			self.parentobj.query_from_ac = True
			self.inputfield.SetValue("Data will be loaded from Annotation Corpus")
		else:
			self.inputfield.Enable()
			self.inputfield.SetValue("")
			self.parentobj.query_from_ac = False

	def OnClear(self, event):
		self.inputfield.SetValue('')
		self.fromaccmd.SetValue(False)
		self.inputfield.Enable()
		self.parentobj.query_file = None
		self.parentobj.query_from_ac = None

	def OnTypeSelect(self, event):
		if self.radio_pairs.GetValue():
			self.parentobj.query_type = 0
			if self.parentobj.query_from_ac:
				self.parentobj.query_from_ac = False
				self.inputfield.SetValue("")
				self.inputfield.Enable()
			self.fromaccmd.Disable()
			self.fromaccmd.SetValue(False)
		elif self.radio_list.GetValue():
			self.parentobj.query_type = 1
			self.fromaccmd.Enable()
