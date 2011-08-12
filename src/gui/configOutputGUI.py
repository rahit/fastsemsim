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

class OutputCtrlGui():
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		self.panel = self.parentobj.panel
		self.mainbox = self.parentobj.outputctrlbox
#------------------------------------------------------------------------------------------------------------------
		self.destinationboxline = wxStaticBox(self.panel, wxID_ANY, 'Output destination')
		self.destinationbox= wxStaticBoxSizer(self.destinationboxline, wxHORIZONTAL)
		self.outputtypes = ['output field','file']
		self.radio_field = wxRadioButton(self.panel, wxID_ANY, self.outputtypes[0], (10, 10), style=wxRB_GROUP)
		self.radio_file = wxRadioButton(self.panel, wxID_ANY, self.outputtypes[1], (10, 10))
		self.destinationbox.Add(self.radio_field,wxEXPAND)
		self.destinationbox.Add(self.radio_file,wxEXPAND)
		self.parentobj.Bind(EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_field.GetId())
		self.parentobj.Bind(EVT_RADIOBUTTON, self.OnTypeSelect, id=self.radio_file.GetId())
		self.parentobj.output_type = 0
		self.parentobj.output_ok = True

		self.commandsline  = wxStaticBox(self.panel, wxID_ANY, 'Output file')
		self.commands = wxStaticBoxSizer(self.commandsline, wxVERTICAL)
		self.outputlabel = wxStaticText(self.panel, label = 'Not selected')
		self.outputlabel.SetFont(self.parentobj.font)
		self.filechooser = wxButton(self.panel, wxID_ANY, 'Choose file...')
		self.filechooser.Disable()
		self.parentobj.Bind(EVT_BUTTON, self.OnFileBrowse, id=self.filechooser.GetId())
		self.commands.Add(self.outputlabel, flag=wxBOTTOM|wxTOP, border=10)
		self.commands.Add(self.filechooser)
		
		self.mainbox.Add(self.destinationbox)
		self.mainbox.Add(self.commands)
#------------------------------------------------------------------------------------------------------------------

	def OnFileBrowse(self, event):
		dialog = wxFileDialog(None, style = wxSAVE|wxOVERWRITE_PROMPT)
		if dialog.ShowModal() == wxID_OK:
			self.parentobj.output_file = dialog.GetPath()
			self.outputlabel.SetLabel(self.parentobj.output_file)
			self.parentobj.output_ok = True

	def OnTypeSelect(self, event):
		if self.radio_field.GetValue():
			self.parentobj.output_type = 0 # text field
			self.filechooser.Disable()
			self.parentobj.output_ok = True
			#self.fromaccmd.Disable()
		elif self.radio_file.GetValue():
			self.parentobj.output_type = 1 # file 
			if self.parentobj.output_file == None:
				self.parentobj.output_ok = False
			self.filechooser.Enable()
