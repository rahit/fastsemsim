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

import wx
from fastSemSim.GO import GeneOntology
from fastSemSim.GO import AnnotationCorpus
from fastSemSim.SemSim import SemSimMeasures

class OperationGui:

	availablemeasures = []
	requiremixing = []
	availablemixing = []
		
	def __init__(self, parent):
		self.parentobj = parent
		self.InitUI()
	
	def InitUI(self):
		ssmeasure = None
		self.mainbox = self.parentobj.operation_box
		self.panel = self.parentobj.panel
#------------------------------------------------------------------------------------------------------------------
		#SS section
		self.mainsubbox = wx.BoxSizer(wx.HORIZONTAL)
		
		# SSbox - SS and MS
		#self.ssboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Semantic Similarity')
		#self.ssbox = wx.StaticBoxSizer(self.ssboxline, wx.HORIZONTAL)
		self.ssbox = wx.BoxSizer(wx.VERTICAL)
		self.tsbox = wx.BoxSizer(wx.VERTICAL)
		self.availablemeasures = []
		self.requiremixing = []
		for i in SemSimMeasures.SemSimMeasures:
			self.availablemeasures.append(i)
			self.requiremixing.append(i[1])
		self.ss = wx.ComboBox(self.panel, wx.ID_ANY, choices=self.availablemeasures, style=wx.CB_READONLY, size=(150,25))
		self.ss_label = wx.StaticText(self.panel, label='Semantic Measure')
		self.ss_advanced_cmd = wx.BitmapButton(self.panel, -1, wx.Bitmap('gui/advanced.png'))
		self.tsbox.Add(self.ss_label, flag=wx.LEFT|wx.RIGHT, border=5)
		self.tssubbox = wx.BoxSizer(wx.HORIZONTAL)
		self.tssubbox.Add(self.ss, flag=wx.LEFT, border=10)
		self.tssubbox.Add(self.ss_advanced_cmd)
		self.tsbox.Add(self.tssubbox)
		
		self.msbox = wx.BoxSizer(wx.VERTICAL)
		self.availablemixing = []
		for i in SemSimMeasures.MixingStrategies:
			self.availablemixing.append(i)
		self.mixing = wx.ComboBox(self.panel, wx.ID_ANY, choices=self.availablemixing, style=wx.CB_READONLY, size=(150,25))
		self.mixing_label = wx.StaticText(self.panel, label='Mixing Strategy')
		self.ms_advanced_cmd = wx.BitmapButton(self.panel, -1, wx.Bitmap('gui/advanced.png'))
		self.msbox.Add(self.mixing_label, flag=wx.UP|wx.LEFT|wx.RIGHT, border=5)
		self.mssubbox = wx.BoxSizer(wx.HORIZONTAL)
		self.mssubbox.Add(self.mixing, flag=wx.LEFT, border=10)
		self.mssubbox.Add(self.ms_advanced_cmd)
		self.msbox.Add(self.mssubbox)
		self.mixing.Disable()
		
		#self.ssadvancedbox = wx.BoxSizer(wx.VERTICAL)
		
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
		self.mainsubbox.Add(self.ssbox, flag=wx.EXPAND|wx.TOP|wx.RIGHT, border=5)
		self.mainsubbox.Add(self.gobox, flag=wx.EXPAND|wx.LEFT, border=10)
		#self.mainsubbox.Add(self.ssadvancedbox, flag=wx.LEFT|wx.RIGHT, border=10)
		
		self.parentobj.Bind(wx.EVT_COMBOBOX, self.OnSelectSS, id=self.ss.GetId())
		self.parentobj.Bind(wx.EVT_COMBOBOX, self.OnSelectMS, id=self.mixing.GetId())
		for i in self.goradius:
			self.parentobj.Bind(wx.EVT_RADIOBUTTON, self.OnSelectGO, id=i.GetId())

		self.mainbox.Add(self.mainsubbox, flag=wx.EXPAND)
		self.parentobj.SetOperationOk(False)
#------------------------------------------------------------------------------------------------------------------
	def OnSelectGO(self, event):
		for i in range(0,len(self.goradius)):
			if self.goradius[i].GetValue():
				self.parentobj.selectedGO = self.gocodes[i]
		
	def OnSelectMS(self, event):
		#self.parentobj.mixingstrategy = SemSimMeasures.MixingStrategies[self.availablemixing[self.mixing.GetSelection()]]
		self.parentobj.mixingstrategy = self.availablemixing[self.mixing.GetSelection()]
		#print self.parentobj.mixingstrategy
		#self.ok = True
		self.parentobj.update_ssobject = True
		if self.parentobj.ssmeasure is None:
			self.parentobj.SetOperationOk(False)
		else:
			self.parentobj.SetOperationOk(True)
		
	def OnSelectSS(self, event):
		self.ssmeasure = self.ss.GetSelection()
		#self.parentobj.ssmeasure = SemSimMeasures.SemSimMeasures[self.availablemeasures[self.ss.GetSelection()]]
		self.parentobj.ssmeasure = self.availablemeasures[self.ss.GetSelection()]
		#print self.parentobj.ssmeasure
		self.parentobj.update_ssobject = True
		#print SSmeasures[self.ss.GetSelection()]
		if SemSimMeasures.SemSimMeasures[self.availablemeasures[self.ss.GetSelection()]][1]:
			self.mixing.Enable()
			if self.parentobj.mixingstrategy is None:
				self.parentobj.SetOperationOk(False)
		else:
			self.mixing.Disable()
			self.parentobj.SetOperationOk(True)
			
#--------------------------------------------------------------
# Utilities to set front-end values
	def set_ss(self, measure):
		self.ss.SetStringSelection(measure)
		self.OnSelectSS(None)

	def set_ms(self, ms):
		self.mixing.SetStringSelection(ms)
		self.OnSelectMS(None)

	def set_go(self, go):
		i = -1
		for j in range(0,len(self.goradius)):
			self.goradius[j].SetValue(False)
			if self.gocodes[j] == go:
				i = j
		self.goradius[i].SetValue(True)
		self.OnSelectGO(None)