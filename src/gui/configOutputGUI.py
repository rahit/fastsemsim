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

class OutputGui(wxFrame):
	
	def __init__(self, parent):
		self.parentobj = parent
		super(OutputGui, self).__init__(self.parentobj, title="Load Annotation Corpus", size=(500,200))
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
		panel.SetSizerAndFit(mainbox)
		mainbox.Add(statusbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		mainbox.Add(descbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)
		mainbox.Add(commanbox, flag=wxEXPAND|wxLEFT|wxRIGHT|wxTOP, border=10)

		
		# Descbox
		self.filename_label = wxStaticText(panel, label='AC File')
		self.filename_label.SetFont(font)
		self.filename = wxStaticText(panel, label='')
		self.acobjs_label = wxStaticText(panel, label='Objects')
		self.acobjs_label.SetFont(font)
		self.acobjs = wxStaticText(panel, label='')
		self.acobjs.SetFont(font)
		self.acterms_label = wxStaticText(panel, label='Go Terms involved')
		self.acterms_label.SetFont(font)
		self.acterms = wxStaticText(panel, label='')
		self.acterms.SetFont(font)
		descbox.AddMany([(self.filename_label), (self.filename), (self.acobjs_label), (self.acobjs), (self.acterms_label), (self.acterms)])

		# commanbox
		self.acchooser = wxButton(panel, wxID_ANY, 'Select file...')
		self.acload = wxButton(panel, wxID_ANY, 'Load...')
		self.acload.Hide()
		self.Bind(EVT_BUTTON, self.OnACBrowse, id=self.acchooser.GetId())
		self.Bind(EVT_BUTTON, self.OnACLoad, id=self.acload.GetId())
		self.doneb = wxButton(panel, wxID_ANY, 'Done')
		self.Bind(EVT_BUTTON, self.OnACBrowseDone, id=self.doneb.GetId())
		commanbox.Add(self.acchooser, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		commanbox.Add(self.doneb, flag=wxLEFT|wxRIGHT|wxTOP, border=10)
		
		#statusbox
		self.status_label = wxStaticText(panel, label='No Annotation Corpus loaded.')
		self.status_label.SetFont(font)
		#self.status_label.Hide()
		statusbox.Add(self.status_label, border=10)
		

	#def OnACBrowse(self, event):
		#dialog = wxFileDialog(None, style = wxOPEN)
		#if dialog.ShowModal() == wxID_OK:
			##print 'Selected: ', dialog.GetPath()
			#self.filename.SetLabel(dialog.GetPath())
			#self.status_label.SetLabel("Loading annotation corpus... Please wait.")
			#self.status_label.Show()
			#self.acchooser.Disable()
			#self.doneb.Disable()
			#self.acobjs.SetLabel("")
			#self.acterms.SetLabel("")
			##self.parentobj.acchooser.Disable()
			#event = wxPyCommandEvent(EVT_BUTTON.typeId, self.acload.GetId())
			#wxPostEvent(self.GetEventHandler(), event)


	#def OnACLoad(self, event):
		#self.ac = AnnotationCorpus.AnnotationCorpus(self.parentobj.go) 
		#self.ftype = "GOA"
		#self.ac.parse(str(self.filename.GetLabel()), self.ftype)
		#self.ac.sanitize()
		#if True: # replace with control code
			##print "Ontology infos: file name: " + str(self.filename.GetLabel()) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())
			#self.acchooser.Enable()
			#self.doneb.Enable()
			#self.acobjs.SetLabel(str(len(self.ac.annotations)))
			#self.acterms.SetLabel(str(len(self.ac.reverse_annotations)))
			#self.parentobj.ac = self.ac
			#self.parentobj.aclabel.SetLabel(self.filename.GetLabel())
			#self.status_label.SetLabel("Annotation Corpus loaded.")
			##self.parentobj.acchooser.Enable()
				
	def OnACBrowseDone(self, event):
		self.Hide()
		
	def OnQuit(self, event):
		self.Hide()