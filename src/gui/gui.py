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
from loadAnnotationCorpusGUI import *
from loadGeneOntologyGUI import *
from configOperationGUI import *
from configOutputGUI import *
from pairsGUI import *

class gui(wxFrame):
	loadGOgui = None
	loadACgui = None
	OperationGui = None
	OutputGui = None

	def __init__(self, parent):
		super(gui, self).__init__(parent, title="fastSemSim GUI (src version)", size=(800,500))
		self.InitUI()   

	def InitUI(self):
		self.font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
		self.font.SetPointSize(9)
        
		self.panel = wxPanel(self)
		self.mainbox = wxBoxSizer(wxVERTICAL)
		self.goacbox = wxBoxSizer(wxHORIZONTAL)

		# GO File Chooser
		self.goboxline = wxStaticBox(self.panel, wxID_ANY, 'Gene Ontology')
		self.gobox = wxStaticBoxSizer(self.goboxline, wxHORIZONTAL)
		self.golabel = wxStaticText(self.panel, label='Not loaded')
		self.golabel.SetFont(self.font)
		self.gochooser = wxButton(self.panel, wxID_ANY, 'Manage GO...')
		self.gobox.Add(self.golabel,flag=wxALL|wxCENTER, border = 8)
		self.gobox.Add(self.gochooser,flag=wxALL|wxCENTER, border = 8)

		## Annotation Corpus File Chooser
		self.acboxline = wxStaticBox(self.panel, wxID_ANY, 'Annotation Corpus')
		self.acbox = wxStaticBoxSizer(self.acboxline, wxHORIZONTAL)
		self.aclabel = wxStaticText(self.panel, label = 'Not loaded')
		self.aclabel.SetFont(self.font)
		self.acchooser = wxButton(self.panel, wxID_ANY, 'Manage AC...')
		self.acchooser.Disable()
		self.acbox.Add(self.aclabel, flag=wxALL|wxCENTER, border = 8)
		self.acbox.Add(self.acchooser, flag=wxALL|wxCENTER, border = 8)

		## Operation Chooser
		self.operationboxline = wxStaticBox(self.panel, wxID_ANY, 'Operation')
		self.operationbox = wxStaticBoxSizer(self.operationboxline, wxVERTICAL)
		self.operationobj = OperationGui(self)
		#self.olabel = wxStaticText(self.panel, label = 'Not configured')
		#self.olabel.SetFont(self.font)
		#self.ochooser = wxButton(self.panel, wxID_ANY, 'Configure Operation...')
		#self.ochooser.Disable()
		#self.operationbox.Add(self.olabel, flag=wxALL|wxCENTER, border = 8)
		#self.operationbox.Add(self.ochooser, flag=wxALL|wxCENTER, border = 8)
		
		## Query Chooser
		self.pairsboxline = wxStaticBox(self.panel, wxID_ANY, 'Query pairs')
		self.pairsbox = wxStaticBoxSizer(self.pairsboxline, wxVERTICAL)
		self.pairsobj = PairsGUI(self)
		#self.olabel = wxStaticText(self.panel, label = 'Not configured')
		#self.olabel.SetFont(self.font)
		#self.ochooser = wxButton(self.panel, wxID_ANY, 'Configure Operation...')
		#self.ochooser.Disable()
		#self.operationbox.Add(self.olabel, flag=wxALL|wxCENTER, border = 8)
		#self.operationbox.Add(self.ochooser, flag=wxALL|wxCENTER, border = 8)
		
		## Output Chooser
		self.outputboxline = wxStaticBox(self.panel, wxID_ANY, 'Output')
		self.outputbox = wxStaticBoxSizer(self.outputboxline, wxHORIZONTAL)
		self.outputlabel = wxStaticText(self.panel, label = 'Not configured')
		self.outputlabel.SetFont(self.font)
		self.outputchooser = wxButton(self.panel, wxID_ANY, 'Configure Output...')
		#self.outputchooser.Disable()
		self.outputbox.Add(self.outputlabel, flag=wxALL|wxCENTER, border = 8)
		self.outputbox.Add(self.outputchooser, flag=wxALL|wxCENTER, border = 8)

		self.goacbox.Add ( ( 0, 0 ), 1, wxEXPAND )
		self.goacbox.Add(self.gobox, flag=wxEXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wxEXPAND )
		self.goacbox.Add(self.acbox, flag=wxEXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wxEXPAND )
		
		self.mainbox.Add(self.goacbox, 0, flag=wxEXPAND)
		self.mainbox.Add(self.operationbox, flag=wxEXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wxEXPAND )
		self.mainbox.Add(self.pairsbox, flag=wxEXPAND, border=5)
		self.mainbox.Add(self.outputbox, flag=wxEXPAND, border=5)
		self.panel.SetSizerAndFit(self.mainbox)
		
		self.Bind(EVT_BUTTON, self.OnGOBrowse, id=self.gochooser.GetId())
		self.Bind(EVT_BUTTON, self.OnACBrowse, id=self.acchooser.GetId())
		#self.Bind(EVT_BUTTON, self.OnOperationConfig, id=self.ochooser.GetId())
		self.Bind(EVT_BUTTON, self.OnOutputConfig, id=self.outputchooser.GetId())

	def enablebutton(self):
		print self.gopath.GetValue()
		print self.acpath.GetValue()
		if (not self.gopath.GetValue() == "") and (not self.acpath.GetValue() == ""):
			self.filesloader.Enable()
	
	def OnGOBrowse(self, event):
		if self.loadGOgui is None:
			self.loadGOgui = loadGO(self)
		self.loadGOgui.Show()  
		
	def OnACBrowse(self, event):
		if self.loadACgui is None:
			self.loadACgui = loadAC(self)
		self.loadACgui.Show()  

	def OnOperationConfig(self, event):
		if self.OperationGui is None:
			self.OperationGui = OperationGui(self)
		self.OperationGui.Show()  

	def OnOutputConfig(self, event):
		if self.OutputGui is None:
			self.OutputGui = OutputGui(self)
		self.OutputGui.Show()  

	#def OnACBrowse(self, event):
		#dialog = wxFileDialog(None, style = wxOPEN)
		#if dialog.ShowModal() == wxID_OK:
			##print 'Selected: ', dialog.GetPath()
			#self.acpath.SetValue(dialog.GetPath())
			#self.enablebutton()

	def OnQuit(event):
		#print event
		frame.Close()

if __name__ == "__main__":
	app = wxApp()
	window = gui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
