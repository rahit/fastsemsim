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
	#Windows handles
	LoadGOgui = None
	LoadACgui = None
	Operationgui = None
	Querygui = None
	OutputCtrlgui = None
	#Interactiongui = None
	
	#primary data
	go = None
	ac = None
	selectedGO = None
	mixingstrategy = None
	ssmeasure = None
	output_type = None
	output_file = None
	query_type = None
	query_from_ac = False
	query_file = None
	
	
	#derived data
	query = None
	ssobject = None
	
	#control data
	status = 0
	go_ok = False
	ac_ok = False
	query_ok = False
	output_ok = False
	operation_ok = False
	
	#flags
	update_query = True
	update_ssobject = True
	
	
	def __init__(self, parent):
		super(gui, self).__init__(parent, title="fastSemSim - Copyright 2011, Marco Mina (src version)", size=(800,600))
		self.InitUI()

	def InitUI(self):
		self.font = wxSystemSettings_GetFont(wxSYS_SYSTEM_FONT)
		self.font.SetPointSize(9)
        
		self.panel = wxPanel(self)
		self.mainbox = wxBoxSizer(wxVERTICAL)

#----------------------------------------------------------------------------------------------------------------------------------
		#GO and GOA Sections
		self.goacbox = wxBoxSizer(wxHORIZONTAL)
#		---------------------------------------------------------------------------
		# GO File Section
		self.goboxline = wxStaticBox(self.panel, wxID_ANY, 'Gene Ontology')
		self.gobox = wxStaticBoxSizer(self.goboxline, wxHORIZONTAL)
		self.golabel = wxStaticText(self.panel, label='Not loaded')
		self.golabel.SetFont(self.font)
		self.gochoosecmd = wxButton(self.panel, wxID_ANY, 'Manage GO...')
		self.gobox.Add(self.golabel,flag=wxALL|wxCENTER, border = 8)
		self.gobox.Add(self.gochoosecmd,flag=wxALL|wxCENTER, border = 8)
		self.Bind(EVT_BUTTON, self.OnGOBrowse, id=self.gochoosecmd.GetId())
		
#		---------------------------------------------------------------------------
		## Annotation Corpus File Chooser
		self.acboxline = wxStaticBox(self.panel, wxID_ANY, 'Annotation Corpus')
		self.acbox = wxStaticBoxSizer(self.acboxline, wxHORIZONTAL)
		self.aclabel = wxStaticText(self.panel, label = 'Not loaded')
		self.aclabel.SetFont(self.font)
		self.acchoosecmd = wxButton(self.panel, wxID_ANY, 'Manage AC...')
		self.acchoosecmd.Disable()
		self.acbox.Add(self.aclabel, flag=wxALL|wxCENTER, border = 8)
		self.acbox.Add(self.acchoosecmd, flag=wxALL|wxCENTER, border = 8)
		self.Bind(EVT_BUTTON, self.OnACBrowse, id=self.acchoosecmd.GetId())
		
#		---------------------------------------------------------------------------
		self.goacbox.Add ( ( 0, 0 ), 1, wxEXPAND )
		self.goacbox.Add(self.gobox, flag=wxEXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wxEXPAND )
		self.goacbox.Add(self.acbox, flag=wxEXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wxEXPAND )

#----------------------------------------------------------------------------------------------------------------------------------
		## Operation Section
		self.operationboxline = wxStaticBox(self.panel, wxID_ANY, 'Operation')
		self.operationbox = wxStaticBoxSizer(self.operationboxline, wxVERTICAL)
		self.operationobj = OperationGui(self)

#----------------------------------------------------------------------------------------------------------------------------------
		## Query and output Sections
		self.queryoutputctrlbox = wxBoxSizer(wxHORIZONTAL)
#----------------------------------------------------------------------------------
		## Query Chooser
		self.queryboxline = wxStaticBox(self.panel, wxID_ANY, 'Query pairs')
		self.querybox = wxStaticBoxSizer(self.queryboxline, wxVERTICAL)
		self.querygui = PairsGUI(self)
#----------------------------------------------------------------------------------
		## Output Chooser
		self.outputctrlboxline = wxStaticBox(self.panel, wxID_ANY, 'Output format')
		self.outputctrlbox = wxStaticBoxSizer(self.outputctrlboxline, wxVERTICAL)
		self.outputCrtlgui = OutputCtrlGui(self)
#----------------------------------------------------------------------------------
		self.queryoutputctrlbox.Add(self.querybox, flag=wxEXPAND, border=5)
		self.queryoutputctrlbox.Add(self.outputctrlbox, flag=wxEXPAND, border=5)
		
#----------------------------------------------------------------------------------------------------------------------------------
		## Control and output Section 
		self.interactionboxline = wxStaticBox(self.panel, wxID_ANY, 'Controls and Output')
		self.interactionbox = wxStaticBoxSizer(self.interactionboxline, wxHORIZONTAL)
		
#----------------------------------------------------------------------------------
		#Control zone
		self.commandbox = wxBoxSizer(wxVERTICAL)
		self.gocmd = wxButton(self.panel, wxID_ANY, 'Start')
		self.exitcmd = wxButton(self.panel, wxID_ANY, 'Exit')
		self.commandbox.Add(self.gocmd)
		self.commandbox.Add(self.exitcmd)
		self.Bind(EVT_BUTTON, self.OnGoCmd, id=self.gocmd.GetId())
		self.Bind(EVT_BUTTON, self.OnExitCmd, id=self.exitcmd.GetId())
		
#----------------------------------------------------------------------------------
		#Log zone
		self.logboxline = wxStaticBox(self.panel, wxID_ANY, 'Log')
		self.logbox = wxStaticBoxSizer(self.logboxline, wxHORIZONTAL)
		self.logfield = wxTextCtrl(self.panel, size=(300,150), style = wxTE_MULTILINE|wxTE_READONLY|wxTE_AUTO_URL)
		self.logbox.Add(self.logfield, flag=wxEXPAND)
		
#----------------------------------------------------------------------------------
		#Output zone
		self.outputline = wxStaticBox(self.panel, wxID_ANY, 'Output')
		self.outputbox = wxStaticBoxSizer(self.outputline, wxHORIZONTAL)
		self.outputfield = wxTextCtrl(self.panel, size=(300,150), style = wxTE_MULTILINE|wxTE_READONLY)
		self.outputbox.Add(self.outputfield, flag=wxEXPAND)
		
#----------------------------------------------------------------------------------
		self.interactionbox.Add(self.commandbox, flag=wxEXPAND|wxCENTER|wxTOP, border=15)
		self.interactionbox.Add(self.logbox, flag=wxEXPAND|wxCENTER|wxALL, border=10)
		self.interactionbox.Add(self.outputbox, flag=wxEXPAND|wxCENTER|wxALL, border=10)

#----------------------------------------------------------------------------------------------------------------------------------
		## Put everything together
		self.mainbox.Add(self.goacbox, 0, flag=wxEXPAND)
		self.mainbox.Add(self.operationbox, flag=wxEXPAND, border=5)
		self.mainbox.Add(self.queryoutputctrlbox, flag=wxEXPAND, border=5)
		self.mainbox.Add(self.interactionbox, flag=wxEXPAND|wxCENTER|wxALL, border=5)
		self.panel.SetSizerAndFit(self.mainbox)

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
	def OnGOBrowse(self, event):
		if self.loadGOgui is None:
			self.loadGOgui = loadGO(self)
		self.loadGOgui.Show()

	def OnACBrowse(self, event):
		if self.loadACgui is None:
			self.loadACgui = loadAC(self)
		self.loadACgui.Show()  

	def OnExitCmd(self, event):
		self.Close()

	def OnGoCmd(self, event):
		if self.status == 0:
			if self.start():
				self.gocmd.SetLabel("Stop")
				self.status = 1
			# add code to disable all controls
		elif self.status == 1:
			if self.stop():
				self.gocmd.SetLabel("Start")
				self.status = 0
			# add code to enable all controls

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

	def start(self):
		if not self.go_ok:
			self.logfield.AppendText("Gene Ontology not correctly loaded.\n")
			self.logfield.AppendText("Aborted.\n")
			return False
		if not self.ac_ok:
			self.logfield.AppendText("Annotation Corpus not correctly loaded.\n")
			self.logfield.AppendText("Aborted.\n")
			return False
		if not self.query_ok:
			self.logfield.AppendText("Query not correctly loaded.\n")
			self.logfield.AppendText("Aborted.\n")
			return False
		if not self.output_ok:
			self.logfield.AppendText("Output parameters not correctly loaded.\n")
			self.logfield.AppendText("Aborted.\n")
			return False
		if not self.operation_ok:
			self.logfield.AppendText("Semantic Similarity parameters not correctly loaded.\n")
			self.logfield.AppendText("Aborted.\n")
			return False
		
		
		print self.go
		print self.ac
		print self.selectedGO
		print self.mixingstrategy
		print self.ssmeasure
		print self.ssobject
		print self.output_type
		print self.output_file
		print self.query_type
		print self.query_from_ac
		print self.query
		print self.query_file
		print self.status
		self.operationobj.buildSSobject()
		self.buildQuery()
		#for pairs, get list in self.query_pairs
		#for list, get list in self.query_list

		return False

	def buildQuery(self):
		if self.query_type == 0: # Pairs
			if self.query_from_ac:
				print "Annotation Corpus cannot be used as pairs input source"
			elif not self.query_file == None:
				self.pairsobj.loadPairs()
			else:
				self.pairsobj.loadPairsfromField()
		elif self.query_type == 1: # List
			if self.query_from_ac:
				self.loadListFromAC()
			elif not self.query_file == None:
				self.pairsobj.loadList()
			else:
				self.pairsobj.loadListfromField()
		
		if self.query_type == 0:
			print self.query_pairs
		elif self.query_type == 1:
			print self.query_list
		
	def loadListFromAC(self):
		self.parentobj.query_list = []
		for line in self.ac.annotations:
			self.parentobj.query_list.append(line)
	
	def stop(self):
		return True

	def buildSSobject(self):
		self.parentobj.ssobject = None
		if self.parentobj.ssmeasure is None:
			return
		if SSmeasures[self.ssmeasure][1]:
			if self.parentobj.mixingstrategy is None:
				return
		if self.parentobj.go is None or self.parentobj.ac is None:
			return
		self.parentobj.ssobject = ObjSemSim.ObjSemSim(self.parentobj.ac, self.parentobj.go, self.parentobj.ssmeasure, self.parentobj.mixingstrategy, None)
		if not self.parentobj.ssobject is None:
			print "SS object created"
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
			
if __name__ == "__main__":
	app = wxApp()
	window = gui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
