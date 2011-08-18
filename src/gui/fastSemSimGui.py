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
from gui import loadGeneOntologyGui
from gui import loadAnnotationCorpusGui
from gui import OperationGui
from gui import OutputCtrlGui
from gui import QueryGui
from SemSim import SemSimMeasures
from SemSim import ObjSemSim
#from loadAnnotationCorpusGUI import *
#from loadGeneOntologyGUI import *
#from configOperationGUI import *
#from configOutputGUI import *
#from pairsGUI import *

class fastSemSimGui(wx.Frame):
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
	update_ac = True
	
	
	def __init__(self, parent):
		super(fastSemSimGui, self).__init__(parent, title="fastSemSim - Copyright 2011, Marco Mina (src version)", size=(800,600))
		self.InitUI()

	def InitUI(self):
		self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(9)
        
		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)

#----------------------------------------------------------------------------------------------------------------------------------
		#GO and GOA Sections
		self.goacbox = wx.BoxSizer(wx.HORIZONTAL)
#		---------------------------------------------------------------------------
		# GO File Section
		self.goboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Gene Ontology')
		self.gobox = wx.StaticBoxSizer(self.goboxline, wx.HORIZONTAL)
		self.golabel = wx.StaticText(self.panel, label='Not loaded')
		self.golabel.SetFont(self.font)
		self.golabel.Hide()
		self.gopicture = wx.StaticBitmap(self.panel)
		self.gopicture.SetBitmap(wx.Bitmap('W_75.png'))
		
		self.gochoosecmd = wx.Button(self.panel, wx.ID_ANY, 'Manage GO...')
		self.gobox.Add(self.golabel,flag=wx.ALL|wx.CENTER, border = 8)
		self.gobox.Add(self.gochoosecmd,flag=wx.ALL|wx.CENTER, border = 8)
		self.gobox.Add(self.gopicture,flag=wx.ALL|wx.CENTER, border = 8)
		self.Bind(wx.EVT_BUTTON, self.OnGOBrowse, id=self.gochoosecmd.GetId())
		
#		---------------------------------------------------------------------------
		## Annotation Corpus File Chooser
		self.acboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus')
		self.acbox = wx.StaticBoxSizer(self.acboxline, wx.HORIZONTAL)
		self.aclabel = wx.StaticText(self.panel, label = 'Not loaded')
		self.aclabel.SetFont(self.font)
		self.aclabel.Hide()
		self.acpicture = wx.StaticBitmap(self.panel)
		self.acpicture.SetBitmap(wx.Bitmap('W_75.png'))
		self.acchoosecmd = wx.Button(self.panel, wx.ID_ANY, 'Manage AC...')
		#self.acchoosecmd.Disable()
		self.acbox.Add(self.aclabel, flag=wx.ALL|wx.CENTER, border = 8)
		self.acbox.Add(self.acchoosecmd, flag=wx.ALL|wx.CENTER, border = 8)
		self.acbox.Add(self.acpicture,flag=wx.ALL|wx.CENTER, border = 8)
		self.Bind(wx.EVT_BUTTON, self.OnACBrowse, id=self.acchoosecmd.GetId())
		
#		---------------------------------------------------------------------------
		self.goacbox.Add ( ( 0, 0 ), 1, wx.EXPAND )
		self.goacbox.Add(self.gobox, flag=wx.EXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wx.EXPAND )
		self.goacbox.Add(self.acbox, flag=wx.EXPAND, border=5)
		self.goacbox.Add ( ( 0, 0 ), 1, wx.EXPAND )

#----------------------------------------------------------------------------------------------------------------------------------
		## Operation Section
		self.operationboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Operation')
		self.operationbox = wx.StaticBoxSizer(self.operationboxline, wx.HORIZONTAL)
		self.oppicture = wx.StaticBitmap(self.panel)
		self.oppicture.SetBitmap(wx.Bitmap('W_75.png'))
		#self.queryoutputctrlbox.Add(self.qocpicture,flag=wx.ALL|wx.CENTER, border = 8)
		self.Operationgui = OperationGui.OperationGui(self)
		self.operationbox.Add(self.oppicture,flag=wx.ALL|wx.CENTER, border = 8)

#----------------------------------------------------------------------------------------------------------------------------------
		## Query and output Sections
		self.queryoutputctrlbox = wx.BoxSizer(wx.HORIZONTAL)
		#self.qocpicture = wx.StaticBitmap(self.panel)
		#self.qocpicture.SetBitmap(wx.Bitmap('W_75.png'))
		#self.queryoutputctrlbox.Add(self.qocpicture,flag=wx.ALL|wx.CENTER, border = 8)
#----------------------------------------------------------------------------------
		## Query Chooser
		self.queryboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Query pairs')
		self.querybox = wx.StaticBoxSizer(self.queryboxline, wx.HORIZONTAL)
		self.Querygui = QueryGui.QueryGui(self)
		self.qpicture = wx.StaticBitmap(self.panel)
		self.qpicture.SetBitmap(wx.Bitmap('W_75.png'))
		self.querybox.Add(self.qpicture,flag=wx.ALL|wx.CENTER, border = 8)
#----------------------------------------------------------------------------------
		## Output Chooser
		self.superoutputctrlboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Output format')
		self.superoutputctrlbox = wx.StaticBoxSizer(self.superoutputctrlboxline, wx.HORIZONTAL)
		self.outputctrlboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Output format')
		self.outputctrlbox = wx.StaticBoxSizer(self.outputctrlboxline, wx.VERTICAL)
		self.superoutputctrlbox.Add(self.outputctrlbox,flag=wx.ALL|wx.CENTER, border = 8)
		self.OutputCrtlgui = OutputCtrlGui.OutputCtrlGui(self)
		self.opicture = wx.StaticBitmap(self.panel)
		self.opicture.SetBitmap(wx.Bitmap('W_75.png'))
		self.superoutputctrlbox.Add(self.opicture,flag=wx.ALL|wx.CENTER, border = 8)
		
#----------------------------------------------------------------------------------
		self.queryoutputctrlbox.Add(self.querybox, flag=wx.EXPAND, border=5)
		self.queryoutputctrlbox.Add(self.superoutputctrlbox, flag=wx.EXPAND, border=5)
		
#----------------------------------------------------------------------------------------------------------------------------------
		## Control and output Section 
		self.interactionboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Controls and Output')
		self.interactionbox = wx.StaticBoxSizer(self.interactionboxline, wx.HORIZONTAL)
		
#----------------------------------------------------------------------------------
		#Control zone
		self.commandlogbox = wx.BoxSizer(wx.VERTICAL)
		self.commandbox = wx.BoxSizer(wx.HORIZONTAL)
		self.gocmd = wx.Button(self.panel, wx.ID_ANY, 'Start')
		self.exitcmd = wx.Button(self.panel, wx.ID_ANY, 'Exit')
		self.commandbox.Add(self.gocmd)
		self.commandbox.Add(self.exitcmd)
		self.Bind(wx.EVT_BUTTON, self.OnGoCmd, id=self.gocmd.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnExitCmd, id=self.exitcmd.GetId())
		
#----------------------------------------------------------------------------------
		#Log zone
		self.logboxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Log')
		self.logbox = wx.StaticBoxSizer(self.logboxline, wx.VERTICAL)
		self.logfield = wx.TextCtrl(self.panel, size=(300,120), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
		self.logbox.Add(self.logfield, flag=wx.EXPAND)
		
		self.commandlogbox.Add(self.commandbox, flag=wx.EXPAND)
		self.commandlogbox.Add(self.logbox, flag=wx.EXPAND)
#----------------------------------------------------------------------------------
		#Output zone
		self.outputline = wx.StaticBox(self.panel, wx.ID_ANY, 'Output')
		self.outputbox = wx.StaticBoxSizer(self.outputline, wx.HORIZONTAL)
		self.outputfield = wx.TextCtrl(self.panel, size=(350,150), style = wx.TE_MULTILINE|wx.TE_READONLY)
		self.outputbox.Add(self.outputfield, flag=wx.EXPAND)
		
#----------------------------------------------------------------------------------
		self.interactionbox.Add(self.commandlogbox, flag=wx.EXPAND|wx.CENTER|wx.TOP, border=10)
		#self.interactionbox.Add(self.logbox, flag=wx.EXPAND|wx.CENTER|wx.ALL, border=10)
		self.interactionbox.Add(self.outputbox, flag=wx.EXPAND|wx.CENTER|wx.ALL, border=10)

#----------------------------------------------------------------------------------------------------------------------------------
		## Put everything together
		self.mainbox.Add(self.goacbox, 0, flag=wx.EXPAND)
		self.mainbox.Add(self.operationbox, flag=wx.EXPAND, border=5)
		self.mainbox.Add(self.queryoutputctrlbox, flag=wx.EXPAND, border=5)
		self.mainbox.Add(self.interactionbox, flag=wx.EXPAND|wx.CENTER|wx.ALL, border=5)
		self.panel.SetSizerAndFit(self.mainbox)

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
	def OnGOBrowse(self, event):
		if self.LoadGOgui is None:
			self.LoadGOgui = loadGeneOntologyGui.LoadGO(self)
		self.LoadGOgui.Show()

	def OnACBrowse(self, event):
		if self.LoadACgui is None:
			self.LoadACgui = loadAnnotationCorpusGui.LoadAC(self)
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
		self.outputfield.Clear()
		self.logfield.AppendText('--------------------------------------------------')
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
				print self.query
#----------------------------------------------------------------------------------------------------
		# Calculate SS scores
		self.sample_threshold = 100
		little_sample = 0
		if self.output_type==1:
			self.output_file_handle = open(self.output_file, 'w')
			self.outputfield.AppendText("Preview text. Complete output can be found here: "+str(self.output_file)+".\n")
		if self.query_type == 1: # list
			for i in range(0,len(self.query)):
				for j in range(i+1, len(self.query)):
					test = self.ssobject.SemSim(self.query[i],self.query[j], self.selectedGO)
					if type(test) is float:
						test = str('%.4f' %test)
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
		if self.output_type==1:
			self.outputfield.AppendText("Preview text. Complete output can be found here: "+str(self.output_file)+".\n")
			self.output_file_handle.close()
#----------------------------------------------------------------------------------------------------
		return False

	def buildQuery(self):
		result = True
		from_field = False
		if self.query_file == None and not self.query_from_ac: # from field
			self.logfield.AppendText("\tLoading query from text field...\n")
			result = self.loadFromField()
		elif self.query == None or self.update_query:
			self.query = None
			if self.query_type == 1 and self.query_from_ac:
				self.logfield.AppendText("\tLoading query list from Annotation Corpus...\n")
				result = self.loadFromAC()
			elif self.query_type == 0 and self.query_from_ac:
				self.logfield.AppendText("Cannot get pairs from Annotation Corpus.\n")
				result = False
			elif not self.query_file == None:
				self.logfield.AppendText("\tLoading query from file " + str(self.query_file) +"...\n")
				result = self.loadFromFile()
		else:
			self.logfield.AppendText("Using previous query...\n")
			result = True
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
			if SemSimMeasures.SemSimMeasures[self.Operationgui.ssmeasure][1]:
				if self.mixingstrategy is None:
					return False 
			if self.go is None or self.ac is None:
				return False
			self.ssobject = ObjSemSim.ObjSemSim(self.ac, self.go, self.ssmeasure, self.mixingstrategy, None)
			if not self.ssobject is None:
				self.update_ssobject = False
				if SemSimMeasures.SemSimMeasures[self.Operationgui.ssmeasure][1]:
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
	app = wx.App()
	window = fastSemSimGui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
