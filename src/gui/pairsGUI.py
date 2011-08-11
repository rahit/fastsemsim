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
		#self.Bind(EVT_CLOSE, self.OnQuit, id=self.GetId())
		#font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
		#font.SetPointSize(9)
        
		#self.panel = wxPanel(self)
		self.mainbox = self.parentobj.pairsbox
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
				
		#Pairs input src
		self.listsrcboxline = wxStaticBox(self.panel, wxID_ANY, 'Query')
		self.listsrcbox = wxStaticBoxSizer(self.listsrcboxline, wxHORIZONTAL)
		self.inputfield = wxTextCtrl(self.panel, size=(250,150))
		self.listsrcbox.Add(self.inputfield)
		
		self.inputcommands = wxBoxSizer(wxVERTICAL)
		self.clear = wxButton(self.panel, wxID_ANY, 'Clear')
		self.filechooser = wxButton(self.panel, wxID_ANY, 'Load from file...')
		self.fromaccmd = wxButton(self.panel, wxID_ANY, 'From Annotation Corpus')
		self.fromaccmd.Disable()
		self.parentobj.Bind(EVT_BUTTON, self.OnClear, id=self.clear.GetId())
		self.parentobj.Bind(EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		self.parentobj.Bind(EVT_BUTTON, self.OnFromAC, id=self.fromaccmd.GetId())
		self.inputcommands.Add(self.listchooserbox, flag=wxBOTTOM|wxTOP, border=10)
		self.inputcommands.Add(self.filechooser)
		self.inputcommands.Add(self.fromaccmd)
		self.inputcommands.Add(self.clear)
		#self.pairinputsource = ['text field','file','annotation corpus']
		#self.radio_field = wxRadioButton(self.panel, wxID_ANY, self.pairinputsource[0], (10, 10), style=wxRB_GROUP)
		#self.radio_file = wxRadioButton(self.panel, wxID_ANY, self.pairinputsource[1], (10, 10))
		#self.radio_ac = wxRadioButton(self.panel, wxID_ANY, self.pairinputsource[2], (10, 10))
		#self.listsrcbox.Add(self.radio_field)
		#self.listsrcbox.Add(self.radio_file)
		#self.listsrcbox.Add(self.radio_ac)
		#self.parentobj.Bind(EVT_RADIOBUTTON, self.OnSrcSelect, id=self.radio_field.GetId())
		#self.parentobj.Bind(EVT_RADIOBUTTON, self.OnSrcSelect, id=self.radio_file.GetId())
		#self.parentobj.Bind(EVT_RADIOBUTTON, self.OnSrcSelect, id=self.radio_ac.GetId())
			
		#self.mainsubbox.Add(self.listchooserbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		#self.mainsubbox.Add(self.listsrcbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		
		##Pairs input field
		##self.inputboxline = wxStaticBox(self.panel, wxID_ANY, '')
		##self.inputbox = wxStaticBoxSizer(self.inputboxline, wxHORIZONTAL)
		#self.inputbox = wxBoxSizer(wxHORIZONTAL)
		#self.inputfield = wxTextCtrl(self.panel, size=(250,150))
		#self.filename = wxStaticText(self.panel, label='')
		#self.filename.SetFont(self.parentobj.font)
		#self.filechooser = wxButton(self.panel, wxID_ANY, 'Select file...')
		#self.parentobj.Bind(EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		#self.filechooser.Hide()
		#self.filename.Hide()
		#self.inputfield.Hide()
		
		

		
		self.mainsubbox.Add(self.listsrcbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		self.mainsubbox.Add(self.inputcommands, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		#self.mainsubbox.Add(self.listchooserbox, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
#------------------------------------------------------------------------------------------------------------------
		self.mainbox.Add(self.mainsubbox, flag=wxEXPAND)
		#self.panel.SetSizerAndFit(self.mainbox)

#------------------------------------------------------------------------------------------------------------------
	def OnFileBrowse(self, event):
		dialog = wxFileDialog(None, style = wxOPEN)
		if dialog.ShowModal() == wxID_OK:
			#print 'Selected: ', dialog.GetPath()
			self.inputfield.SetValue(dialog.GetPath())
			#self.status_label.SetLabel("Loading annotation corpus... Please wait.")
			#self.status_label.Show()
			#self.acchooser.Disable()
			#self.doneb.Disable()
			#self.acobjs.SetLabel("")
			#self.acterms.SetLabel("")
			##self.parentobj.acchooser.Disable()
			#event = wxPyCommandEvent(EVT_BUTTON.typeId, self.acload.GetId())
			#wxPostEvent(self.GetEventHandler(), event)
	def OnFromAC(self, event):
		self.inputfield.SetValue("From AC")
			
	def OnClear(self, event):
		self.inputfield.SetValue('')
		
	def OnTypeSelect(self, event):
		if self.radio_pairs.GetValue():
			self.parentobj.inputformat = 0
			self.fromaccmd.Disable()
				#self.radio_ac.Disable()
				#if self.radio_ac.GetValue():
					#self.radio_field.SetValue(True)
		elif self.radio_list.GetValue():
			self.parentobj.inputformat = 1
			self.fromaccmd.Enable()
		event = wxPyCommandEvent(EVT_BUTTON.typeId, self.clear.GetId())
		wxPostEvent(self.parentobj.GetEventHandler(), event)
				#self.radio_ac.Enable()

	#def OnSrcSelect(self, event):
		#if self.radio_ac.GetValue():
				#self.inputfield.Hide()
				#self.filename.Hide()
				#self.filechooser.Hide()
		#elif self.radio_field.GetValue():
				#self.inputfield.Show()
				#self.filename.Hide()
				#self.filechooser.Hide()
		#elif self.radio_file.GetValue():
				#self.inputfield.Hide()
				#self.filename.Show()
				#self.filechooser.Show()