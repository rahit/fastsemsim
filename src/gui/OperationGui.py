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
#from SemSim import ObjSemSim
from SemSim import SemSimMeasures

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
		self.mainsubbox = wx.BoxSizer(wx.HORIZONTAL)
		
		# SSbox
		self.ssboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Semantic Similarity')
		self.ssbox = wx.StaticBoxSizer(self.ssboxline, wx.HORIZONTAL)
		
		# SSbox - SS
		self.tsbox = wx.BoxSizer(wx.VERTICAL)
		self.availablemeasures = []
		self.requiremixing = []
		for i in SemSimMeasures.SemSimMeasures:
			self.availablemeasures.append(i[0])
			self.requiremixing.append(i[1])
		self.ss = wx.ComboBox(self.panel, wx.ID_ANY, choices=self.availablemeasures, style=wx.CB_READONLY)
		self.ss_label = wx.StaticText(self.panel, label='Semantic Measure')
		self.tsbox.Add(self.ss_label, flag=wx.UP|wx.DOWN|wx.LEFT|wx.RIGHT, border=5)
		self.tsbox.Add(self.ss, flag=wx.LEFT|wx.RIGHT, border=10)

		# SSbox - MS
		self.msbox = wx.BoxSizer(wx.VERTICAL)
		self.availablemixing = []
		for i in SemSimMeasures.MixingStrategies:
			self.availablemixing.append(i[0])
		self.mixing = wx.ComboBox(self.panel, wx.ID_ANY, choices=self.availablemixing, style=wx.CB_READONLY)
		self.mixing_label = wx.StaticText(self.panel, label='Mixing Strategy')
		self.msbox.Add(self.mixing_label, flag=wx.UP|wx.DOWN|wx.LEFT|wx.RIGHT, border=5)
		self.msbox.Add(self.mixing, flag=wx.LEFT|wx.RIGHT, border=10)
		self.mixing.Disable()
		
		# GObox
		self.goboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Ontology')
		self.gobox = wx.StaticBoxSizer(self.goboxline, wx.VERTICAL)
		#self.go_label = wx.StaticText(self.panel, label='Ontology')
		self.gos = ['Molecular Function','Biological Process','Cellular Component']
		self.gocodes = ['MF','BP','CC']
		self.goradius = []
		self.goradius.append(wx.RadioButton(self.panel, wx.ID_ANY, self.gos[0], (10, 10), style=wx.RB_GROUP))
		self.goradius.append(wx.RadioButton(self.panel, wx.ID_ANY, self.gos[1], (10, 10)))
		self.goradius.append(wx.RadioButton(self.panel, wx.ID_ANY, self.gos[2], (10, 10)))
		self.parentobj.selectedGO = self.gocodes[0]
		#self.gobox.Add(self.go_label)
		for i in self.goradius:
			self.gobox.Add(i)
		
		#self.ssbox.Add(self.hint, flag=wx.EXPAND|wx.ALL, border=10)
		self.ssbox.Add(self.tsbox, flag=wx.EXPAND)
		self.ssbox.Add(self.msbox, flag=wx.EXPAND)
		self.mainsubbox.Add(self.ssbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		self.mainsubbox.Add(self.gobox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		
		self.parentobj.Bind(wx.EVT_COMBOBOX, self.OnSelectSS, id=self.ss.GetId())
		self.parentobj.Bind(wx.EVT_COMBOBOX, self.OnSelectMS, id=self.mixing.GetId())
		for i in self.goradius:
			self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnSelectGO, id=i.GetId())

#------------------------------------------------------------------------------------------------------------------
		self.mainbox.Add(self.mainsubbox, flag=wx.EXPAND)
		#self.mainbox.Add(self.mainsubbox2, flag=wx.EXPAND)
		#self.panel.SetSizerAndFit(self.mainbox)
#------------------------------------------------------------------------------------------------------------------
	def OnSelectGO(self, event):
		for i in range(0,len(self.goradius)):
			if self.goradius[i].GetValue():
				self.parentobj.selectedGO = self.gocodes[i]
		
	def OnSelectMS(self, event):
		self.parentobj.mixingstrategy = SemSimMeasures.MixingStrategies[self.mixing.GetSelection()][0]
		self.ok = True
		self.parentobj.update_ssobject = True
		
	def OnSelectSS(self, event):
		self.ssmeasure = self.ss.GetSelection()
		self.parentobj.ssmeasure = SemSimMeasures.SemSimMeasures[self.ss.GetSelection()][0]
		self.parentobj.update_ssobject = True
		#print SSmeasures[self.ss.GetSelection()]
		if SemSimMeasures.SemSimMeasures[self.ss.GetSelection()][1]:
			self.mixing.Enable()
			self.parentobj.operation_ok = False
		else:
			self.mixing.Disable()
			self.parentobj.operation_ok = True
