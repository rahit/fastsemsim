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
from SemSim import ObjSemSim

class OperationGui:
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		ssmeasure = None
		self.mainbox = self.parentobj.operationbox
		self.panel = self.parentobj.panel
#------------------------------------------------------------------------------------------------------------------
		#SS section
		self.mainsubbox = wxBoxSizer(wxHORIZONTAL)
		
		# SSbox
		self.ssboxline = wxStaticBox(self.panel, wxID_ANY, 'Semantic Similarity')
		self.ssbox = wxStaticBoxSizer(self.ssboxline, wxHORIZONTAL)
		
		# SSbox - SS
		self.tsbox = wxBoxSizer(wxVERTICAL)
		self.availablemeasures = []
		self.requiremixing = []
		for i in SSmeasures:
			self.availablemeasures.append(i[0])
			self.requiremixing.append(i[1])
		self.ss = wxComboBox(self.panel, wxID_ANY, choices=self.availablemeasures, style=wxCB_READONLY)
		self.ss_label = wxStaticText(self.panel, label='Semantic Measure')
		self.tsbox.Add(self.ss_label, flag=wxUP|wxDOWN|wxLEFT|wxRIGHT, border=5)
		self.tsbox.Add(self.ss, flag=wxLEFT|wxRIGHT, border=10)

		# SSbox - MS
		self.msbox = wxBoxSizer(wxVERTICAL)
		self.availablemixing = []
		for i in MixingStrategies:
			self.availablemixing.append(i[0])
		self.mixing = wxComboBox(self.panel, wxID_ANY, choices=self.availablemixing, style=wxCB_READONLY)
		self.mixing_label = wxStaticText(self.panel, label='Mixing Strategy')
		self.msbox.Add(self.mixing_label, flag=wxUP|wxDOWN|wxLEFT|wxRIGHT, border=5)
		self.msbox.Add(self.mixing, flag=wxLEFT|wxRIGHT, border=10)
		self.mixing.Disable()
		
		# GObox
		self.goboxline = wxStaticBox(self.panel, wxID_ANY, 'Ontology')
		self.gobox = wxStaticBoxSizer(self.goboxline, wxVERTICAL)
		#self.go_label = wxStaticText(self.panel, label='Ontology')
		self.gos = ['Molecular Function','Biological Process','Cellular Component']
		self.gocodes = ['MF','BP','CC']
		self.goradius = []
		self.goradius.append(wxRadioButton(self.panel, wxID_ANY, self.gos[0], (10, 10), style=wxRB_GROUP))
		self.goradius.append(wxRadioButton(self.panel, wxID_ANY, self.gos[1], (10, 10)))
		self.goradius.append(wxRadioButton(self.panel, wxID_ANY, self.gos[2], (10, 10)))
		self.parentobj.selectedGO = self.gocodes[0]
		#self.gobox.Add(self.go_label)
		for i in self.goradius:
			self.gobox.Add(i)
		
		#self.ssbox.Add(self.hint, flag=wxEXPAND|wxALL, border=10)
		self.ssbox.Add(self.tsbox, flag=wxEXPAND)
		self.ssbox.Add(self.msbox, flag=wxEXPAND)
		self.mainsubbox.Add(self.ssbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		self.mainsubbox.Add(self.gobox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		
		self.parentobj.Bind(EVT_COMBOBOX, self.OnSelectSS, id=self.ss.GetId())
		self.parentobj.Bind(EVT_COMBOBOX, self.OnSelectMS, id=self.mixing.GetId())
		for i in self.goradius:
			self.parentobj.Bind(EVT_RADIOBUTTON, self.OnSelectGO, id=i.GetId())

#------------------------------------------------------------------------------------------------------------------
		self.mainbox.Add(self.mainsubbox, flag=wxEXPAND)
		#self.mainbox.Add(self.mainsubbox2, flag=wxEXPAND)
		#self.panel.SetSizerAndFit(self.mainbox)
#------------------------------------------------------------------------------------------------------------------
	def OnSelectGO(self, event):
		for i in range(0,len(self.goradius)):
			if self.goradius[i].GetValue():
				self.parentobj.selectedGO = self.gocodes[i]
		
	def OnSelectMS(self, event):
		self.parentobj.mixingstrategy = MixingStrategies[self.mixing.GetSelection()][0]
		self.ok = True
		
	def OnSelectSS(self, event):
		self.ssmeasure = self.ss.GetSelection()
		self.parentobj.ssmeasure = SSmeasures[self.ss.GetSelection()][0]
		#print SSmeasures[self.ss.GetSelection()]
		if SSmeasures[self.ss.GetSelection()][1]:
			self.mixing.Enable()
			self.parentobj.operation_ok = False
		else:
			self.mixing.Disable()
			self.parentobj.operation_ok = True
