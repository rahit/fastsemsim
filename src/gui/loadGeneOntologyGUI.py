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
#from GO import AnnotationCorpus

class loadGO(wxFrame):
	
	def __init__(self, parent):
		self.parentobj = parent
		super(loadGO, self).__init__(self.parentobj, title="Load Gene Ontology", size=(500,200))
		self.InitUI()
	
	def InitUI(self):
		self.Bind(EVT_CLOSE, self.OnQuit, id=self.GetId())
		font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
		font.SetPointSize(9)
        
		panel = wxPanel(self)
		#panel.SetBackgroundColour('#4f5049')
		mainbox = wxBoxSizer(wxVERTICAL)
		descbox = wxFlexGridSizer(rows = 4, cols = 2, vgap = 6, hgap = 20)
		commanbox = wxBoxSizer(wxHORIZONTAL)
		statusbox = wxBoxSizer(wxHORIZONTAL)
		panel.SetSizer(mainbox)
		mainbox.Add(statusbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		mainbox.Add(descbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		mainbox.Add(commanbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)

		
		# Descbox
		self.filename_label = wxStaticText(panel, label='GO File')
		self.filename_label.SetFont(font)
		self.filename = wxStaticText(panel, label='')
		self.gonodes_label = wxStaticText(panel, label='Nodes')
		self.gonodes_label.SetFont(font)
		self.gonodes = wxStaticText(panel, label='')
		self.gonodes.SetFont(font)
		self.goedges_label = wxStaticText(panel, label='Edges')
		self.goedges_label.SetFont(font)
		self.goedges = wxStaticText(panel, label='')
		self.goedges.SetFont(font)
		descbox.AddMany([(self.filename_label), (self.filename), (self.gonodes_label), (self.gonodes), (self.goedges_label), (self.goedges)])

		# commanbox
		self.gochooser = wxButton(panel, wxID_ANY, 'Select file...')
		self.goload = wxButton(panel, wxID_ANY, 'Load...')
		self.goload.Hide()
		self.Bind(EVT_BUTTON, self.OnGOBrowse, id=self.gochooser.GetId())
		self.Bind(EVT_BUTTON, self.OnGOLoad, id=self.goload.GetId())
		self.doneb = wxButton(panel, wxID_ANY, 'Done')
		self.Bind(EVT_BUTTON, self.OnGOBrowseDone, id=self.doneb.GetId())
		commanbox.Add(self.gochooser, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		commanbox.Add(self.doneb, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		
		#statusbox
		self.status_label = wxStaticText(panel, label='No Ontology loaded.')
		self.status_label.SetFont(font)
		#self.status_label.Hide()
		statusbox.Add(self.status_label, border=10)
		

	def OnGOBrowse(self, event):
		dialog = wxFileDialog(None, style = wxOPEN)
		if dialog.ShowModal() == wxID_OK:
			#print 'Selected: ', dialog.GetPath()
			self.filename.SetLabel(dialog.GetPath())
			self.status_label.SetLabel("Loading ontology... Please wait.")
			self.status_label.Show()
			self.gochooser.Disable()
			self.doneb.Disable()
			self.gonodes.SetLabel("")
			self.goedges.SetLabel("")
			self.parentobj.acchooser.Disable()
			event = wxPyCommandEvent(EVT_BUTTON.typeId, self.goload.GetId())
			wxPostEvent(self.GetEventHandler(), event)


	def OnGOLoad(self, event):
		self.tree = GeneOntology.load_GO_XML(open(self.filename.GetLabel(),'r'))
		if self.tree is not None:
			#print "Ontology infos: file name: " + str(self.filename.GetLabel()) + ". Nodes: " + str(self.tree.node_num()) + ". Edges: " + str(self.tree.edge_num())
			self.gochooser.Enable()
			self.doneb.Enable()
			self.gonodes.SetLabel(str(self.tree.node_num()))
			self.goedges.SetLabel(str(self.tree.edge_num()))
			self.parentobj.go = self.tree
			self.parentobj.golabel.SetLabel(self.filename.GetLabel())
			self.status_label.SetLabel("Ontology loaded.")
			self.parentobj.acchooser.Enable()

	def OnGOBrowseDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.Hide()