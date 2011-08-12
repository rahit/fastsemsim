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
		self.Operationgui = OperationGui(self)

#----------------------------------------------------------------------------------------------------------------------------------
		## Query and output Sections
		self.queryoutputctrlbox = wxBoxSizer(wxHORIZONTAL)
#----------------------------------------------------------------------------------
		## Query Chooser
		self.queryboxline = wxStaticBox(self.panel, wxID_ANY, 'Query pairs')
		self.querybox = wxStaticBoxSizer(self.queryboxline, wxVERTICAL)
		self.Querygui = PairsGUI(self)
#----------------------------------------------------------------------------------
		## Output Chooser
		self.outputctrlboxline = wxStaticBox(self.panel, wxID_ANY, 'Output format')
		self.outputctrlbox = wxStaticBoxSizer(self.outputctrlboxline, wxVERTICAL)
		self.OutputCrtlgui = OutputCtrlGui(self)
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
		self.mainbox.Add(self.queryoutputctrlbox, flag=wxEXPAND|wxCENTER, border=5)
		self.mainbox.Add(self.interactionbox, flag=wxEXPAND|wxCENTER|wxALL, border=5)
		self.panel.SetSizerAndFit(self.mainbox)

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
	def OnGOBrowse(self, event):
		if self.LoadGOgui is None:
			self.LoadGOgui = LoadGO(self)
		self.LoadGOgui.Show()

	def OnACBrowse(self, event):
		if self.LoadACgui is None:
			self.LoadACgui = LoadAC(self)
		self.LoadACgui.Show()  

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
		self.skip_checks = False
#----------------------------------------------------------------------------------------------------
		#check if everything is configured
		if not self.skip_checks:
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
		#if not self.operation_ok:
			#self.logfield.AppendText("Semantic Similarity parameters not correctly loaded.\n")
			#self.logfield.AppendText("Aborted.\n")
			#return False
#----------------------------------------------------------------------------------------------------
		#Prepare sem sim object
		self.logfield.AppendText("Trying to setup semantic similarity.\n")
		if not self.buildSSobject():
			return False
#----------------------------------------------------------------------------------------------------
		# Prepare query
		if not self.buildQuery():
			self.logfield.AppendText("Failed to load query.\n")
			self.logfield.AppendText("Aborted.\n")
		else:
			if self.query_type == 0:
				self.logfield.AppendText("\tQuery loaded." + (str(len(self.query))) + " pairs\n")
			elif self.query_type == 1:
				self.logfield.AppendText("Query loaded: " + str(len(self.query)) + " items.\n")
#----------------------------------------------------------------------------------------------------
		# Calculate SS scores
		self.sample_threshold = 100
		if self.output_type==1:
			self.output_file_handle = open(self.output_file, 'w')
			little_sample = 0
		if self.query_type == 1: # list
			for i in range(0,len(self.query)):
				for j in range(i+1, len(self.query)):
					test = self.ssobject.SemSim(self.query[i],self.query[j], self.selectedGO)
					if self.output_type == 0:
						self.outputfield.AppendText(str(self.query[i]) + "\t" + str(self.query[j]) + "\t" + str(test) + "\n")
					else:
						self.output_file_handle.write(str(self.query[i]) + "\t" + str(self.query[j]) + "\t" + str(test) + "\n")
						if little_sample < self.sample_threshold:
							self.outputfield.AppendText(str(self.query[i]) + "\t" + str(self.query[j]) + "\t" + str(test) + "\n")
					little_sample+=1
		elif self.query_type == 0: # pairs
			for i in self.query:
				test = self.ssobject.SemSim(i[0],i[1], self.selectedGO)
				if self.output_type == 0:
					self.outputfield.AppendText(str(i[0]) + "\t" + str(i[1]) + "\t" + str(test) + "\n")
				else:
					self.output_file_handle.write(str(i[0]) + "\t" + str(i[1]) + "\t" + str(test) + "\n")
					if little_sample < self.sample_threshold:
						self.outputfield.AppendText(str(i[0]) + "\t" + str(i[1]) + "\t" + str(test) + "\n")
				little_sample+=1
		if self.output_type==0:
			self.output_file_handle.close()
#----------------------------------------------------------------------------------------------------
		return False

	def buildQuery(self):
		result = True
		self.logfield.AppendText("Loading query...\n")
		if self.query == None or self.update_query:
			if self.query_type == 1 and self.query_from_ac:
				self.logfield.AppendText("\tLoading query list from Annotation Corpus...\n")
				result = self.loadFromAC()
			elif self.query_type == 0 and self.query_from_ac:
				self.logfield.AppendText("Cannot get pairs from Annotation Corpus.\n")
				result = False
			elif self.query_file:
				self.logfield.AppendText("\tLoading query from file " + str(self.query_file) +"...\n")
				result = self.loadFromFile()
			else:
				self.logfield.AppendText("\tLoading query from text field...\n")
				result = self.loadFromField()
			if result:
				self.update_query = False
			else:
				self.update_query = True
				self.query = None
		return result

	def loadFromFile(self):
		h = open(self.query_file,'r')
		self.query = []
		for line in h:
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			if self.query_type == 0: #pairs
				line = line.rsplit('\t')
				self.query.append((line[0], line[1]))
			else: # list
				self.query.append(line)
		inf.close()
		return True

	def loadFromField(self):
		h = self.Querygui.inputfield.GetValue()
		self.query= []
		h = h.splitlines()
		#print h
		for line in h:
			#print line
			if self.query_type == 0: #pairs
				line = line.rsplit(' ')
				#print line
				self.query.append((str(line[0]), str(line[1])))
			else: # list
				self.query.append(str(line))
		print self.query
		return True

	def loadFromAC(self):
		self.query = []
		if self.ac == None:
			return False
		for line in self.ac.annotations:
			self.query.append(line)
		return True
	
	def stop(self):
		return True

	def buildSSobject(self):
		if self.update_ssobject or self.ssobject == None:
			self.ssobject = None
			if self.ssmeasure is None:
				return False
			if SSmeasures[self.Operationgui.ssmeasure][1]:
				if self.mixingstrategy is None:
					return False 
			if self.go is None or self.ac is None:
				return False
			self.ssobject = ObjSemSim.ObjSemSim(self.ac, self.go, self.ssmeasure, self.mixingstrategy, None)
			if not self.ssobject is None:
				self.update_ssobject = False
				if SSmeasures[self.Operationgui.ssmeasure][1]:
					self.logfield.AppendText("Semantic similarity object created: " + str(self.ssmeasure) + " " + str(self.mixingstrategy) + ".\n")
				else:
					self.logfield.AppendText("Semantic similarity object created: " + str(self.ssmeasure) + ".\n")
			else:
				self.logfield.AppendText("Unable to create semantic similarity of type " + str(self.ssmeasure) + " " + str(self.mixingstrategy) + ".\n")
				return False
		else:
			self.logfield.AppendText("Using previous semantic similarity object.\n")
		return True

if __name__ == "__main__":
	app = wxApp()
	window = gui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
