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
from gui.GeneOntologyGui import GeneOntologyGui
from gui.AnnotationCorpusGui import AnnotationCorpusGui
from gui.OperationGui import OperationGui
from gui.OutputCtrlGui import OutputCtrlGui
from gui.OutputGui import OutputGui
from gui.ControlGui import ControlGui
from gui.QueryGui import QueryGui
from gui.StatusGui import StatusGui
from SemSim import SemSimMeasures
from SemSim import ObjSemSim
from gui import WorkThread
import threading

class fastSemSimGui(wx.Frame):
	debug = True
	#Components handles
	GOGui = None
	ACGui = None
	OperationGui = None
	QueryGui = None
	OutputCtrlGui = None
	OutputGui = None
	
	#data structures
	go = None
	ac = None
	selectedGO = None
	mixingstrategy = None
	ssmeasure = None
	output_type = None # 0 = field, 1 = file
	output_file = None
	query_type = None # 0 = pairs, 1 = list
	#query_from_ac = False # True if load from ac <-- obsolete!
	query_from = None # 0 = field, 1 = file, 2 = ac
	query_file = None
	
	#objects required for ss calculation
	query = None # list of pairs or list of objects, depending on query_type variable
	ssobject = None # semantic similarity measure
	
	#control data
	status = 0 # current status: -1 = fatal error, 0 = not running - to configure, 1 = ready to run, 2 = running
	go_ok = False
	ac_ok = False
	query_ok = False
	outputctrl_ok = False
	operation_ok = False
	start_cmd = None # main command to start execution
	
	#flags signaling whether some structures should be updated
	update_query = True
	update_ssobject = True
	update_ac = True
	
	#other data
	Ok_pic = 'gui/V_30.png'
	Warning_pic = 'gui/W_30.png'
	show_pics = True
	go_status_pic = None
	ac_status_pic = None
	query_status_pic = None
	outputctrl_status_pic = None
	output_status_pic = None
	operation_status_pic = None
	status_pic = None

	def __init__(self, parent):
		super(fastSemSimGui, self).__init__(parent, title="fastSemSim - Copyright 2011, Marco Mina (src version)", size=(620,600))
		self.InitUI()
		
	def InitUI(self):
		self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(9)

		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)

		# Define main regions
		self.go_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Gene Ontology')
		self.go_box = wx.StaticBoxSizer(self.go_boxline, wx.HORIZONTAL)
		self.ac_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Annotation Corpus')
		self.ac_box = wx.StaticBoxSizer(self.ac_boxline, wx.HORIZONTAL)
		self.operation_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Semantic Similarity Measure')
		self.operation_box = wx.StaticBoxSizer(self.operation_boxline, wx.HORIZONTAL)
		self.query_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Query')
		self.query_box = wx.StaticBoxSizer(self.query_boxline, wx.HORIZONTAL)
		self.outputctrl_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Output Parameters')
		self.outputctrl_box = wx.StaticBoxSizer(self.outputctrl_boxline, wx.HORIZONTAL)
		self.control_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Controls')
		self.control_box = wx.StaticBoxSizer(self.control_boxline, wx.HORIZONTAL)
		self.status_boxline = wx.StaticBox(self.panel, wx.ID_ANY, 'Status')
		self.status_box = wx.StaticBoxSizer(self.status_boxline, wx.HORIZONTAL)
		
		# Put everything together. Merge AC and GO in the same line
		self.superior_box = wx.BoxSizer(wx.HORIZONTAL)
		self.superior_left_box = wx.BoxSizer(wx.VERTICAL)
		self.goac_box = wx.BoxSizer(wx.HORIZONTAL) #### Draw ac and go on the same line
		self.goac_box.Add(self.go_box, flag=wx.EXPAND, border=5)
		self.goac_box.Add(self.ac_box, flag=wx.EXPAND, border=5)
		self.goac_box.Add ( ( 0, 0 ), 1, flag = wx.EXPAND )
		#self.mainbox.Add(self.go_box, 0, flag=wx.EXPAND)
		#self.mainbox.Add(self.ac_box, 0, flag=wx.EXPAND)

		self.operationoutputctrl_box = wx.BoxSizer(wx.HORIZONTAL)
		self.operationoutputctrl_box .Add(self.operation_box, flag=wx.EXPAND, border=5)
		#self.operationoutputctrl_box .Add(self.outputctrl_box, flag=wx.EXPAND, border=5)
		self.operationoutputctrl_box.Add ( ( 0, 0 ), 1, wx.EXPAND )
		#self.mainbox.Add(self.ss_box, 0, flag=wx.EXPAND)
		#self.mainbox.Add(self.outputctrl_box, 0, flag=wx.EXPAND)
		
		self.superior_left_box.Add(self.goac_box, 0, flag=wx.EXPAND)
		self.superior_left_box.Add(self.operationoutputctrl_box , 0, flag=wx.EXPAND)
		
		self.superior_box.Add(self.superior_left_box, 0, flag=wx.EXPAND)
		self.superior_box.Add(self.status_box, 0, flag=wx.EXPAND)
		
		self.mainbox.Add(self.superior_box, 0, flag=wx.EXPAND)
		self.mainbox.Add(self.query_box, 0, flag=wx.EXPAND)
		self.mainbox.Add(self.outputctrl_box, 0, flag=wx.EXPAND)
		self.mainbox.Add(self.control_box, 0, flag=wx.EXPAND)
		
		self.panel.SetSizerAndFit(self.mainbox)

		#### initialize other components
		self.StatusGui = StatusGui(self)
		self.GOGui = GeneOntologyGui(self)
		self.ACGui = AnnotationCorpusGui(self)
		self.OperationGui = OperationGui(self)
		self.OutputCtrlGui = OutputCtrlGui(self)
		self.QueryGui = QueryGui(self)
		self.OutputGui = OutputGui(self)
		self.ControlGui = ControlGui(self)
		
		
		self.Connect(-1, -1, WorkThread.EVT_PROGRESS_ID, self.OnProgress)
		self.Connect(-1, -1, WorkThread.EVT_COMPLETED_ID, self.OnCompleted)
		self.Connect(-1, -1, WorkThread.EVT_LOGDATA_ID, self.OnLogData)
		self.Connect(-1, -1, WorkThread.EVT_OUTPUTDATA_ID, self.OnOutputData)
		self.running = False
		self.activateGoCmd()
		return

#----------------------------------------------------------------------------------------------------------------------------------

	# routines to manage flags, status, and variables in general
	def SetGoOk(self, status):
		self.go_ok = status
		if self.show_pics:
			if self.go_ok:
				self.StatusGui.go_status_pic.SetBitmap(wx.Bitmap(self.Ok_pic))
			else:
				self.StatusGui.go_status_pic.SetBitmap(wx.Bitmap(self.Warning_pic))
		self.activateGoCmd()
		
	def SetAcOk(self, status):
		self.ac_ok = status
		if self.show_pics:
			if self.ac_ok:
				self.StatusGui.ac_status_pic.SetBitmap(wx.Bitmap(self.Ok_pic))
			else:
				self.StatusGui.ac_status_pic.SetBitmap(wx.Bitmap(self.Warning_pic))
		self.activateGoCmd()
		
	def SetQueryOk(self, status):
		self.query_ok = status
		if self.show_pics:
			if self.query_ok:
				self.StatusGui.query_status_pic.SetBitmap(wx.Bitmap(self.Ok_pic))
			else:
				self.StatusGui.query_status_pic.SetBitmap(wx.Bitmap(self.Warning_pic))
		self.activateGoCmd()
		
	def SetOutputCtrlOk(self, status):
		self.outputctrl_ok = status
		if self.show_pics:
			if self.outputctrl_ok:
				self.StatusGui.output_status_pic.SetBitmap(wx.Bitmap(self.Ok_pic))
			else:
				self.StatusGui.output_status_pic.SetBitmap(wx.Bitmap(self.Warning_pic))
		self.activateGoCmd()

	def SetOperationOk(self, status):
		self.operation_ok = status
		if self.show_pics:
			if self.operation_ok:
				self.StatusGui.operation_status_pic.SetBitmap(wx.Bitmap(self.Ok_pic))
			else:
				self.StatusGui.operation_status_pic.SetBitmap(wx.Bitmap(self.Warning_pic))
		self.activateGoCmd()

	def activateGoCmd(self): # should not be called if status is 2
		if self.status == -1:
			return
		if self.debug or (self.go_ok and self.ac_ok and self.query_ok and self.outputctrl_ok and self.operation_ok):
			self.SetStatus(1) # set to 0
		else:
			self.SetStatus(0)

	def SetStatus(self, status):
		self.status = status
		if self.show_pics:
			if self.status == -1: # Fatal error
				if not self.start_cmd is None:
					self.start_cmd.Disable()
					self.start_cmd.SetLabel("Start")
			if self.status == 0: # Not running. Not Ready
				if not self.start_cmd is None:
					self.start_cmd.Disable()
					self.start_cmd.SetLabel("Start")
			if self.status == 1: # Not Running. Ready
				if not self.start_cmd is None:
					self.start_cmd.SetLabel("Start")
					self.start_cmd.Enable()
			if self.status == 2: # Running. (Completed)
				if not self.start_cmd is None:
					self.start_cmd.SetLabel("Stop")
					#self.statuspicture.SetBitmap(wx.Bitmap(self.s0_pic))
					self.start_cmd.Enable()

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

	def buildSSobject(self):
		if self.update_ssobject or self.ssobject == None:
			self.ssobject = None
			if self.ssmeasure is None:
				return False
			#if SemSimMeasures.SemSimMeasures[self.Operationgui.ssmeasure][1]:
				#if self.mixingstrategy is None:
					#return False 
			if self.go is None or self.ac is None:
				return False
			##print self.ssmeasure
			#print self.mixingstrategy
			self.ssobject = ObjSemSim.ObjSemSim(self.ac, self.go, self.ssmeasure, self.mixingstrategy, None)
			if not self.ssobject is None:
				self.update_ssobject = False
				if not self.mixingstrategy is None:
					self.log_field.AppendText("Semantic similarity object created: " + str(self.ssmeasure) + " " + str(self.mixingstrategy) + ".\n")
				else:
					self.log_field.AppendText("Semantic similarity object created: " + str(self.ssmeasure) + ".\n")
			else:
				#self.log_field.AppendText("Unable to create semantic similarity of type " + str(self.ssmeasure) + " " + str(self.mixingstrategy) + ".\n")
				return False
		else:
			self.log_field.AppendText("Using previous semantic similarity object.\n")
		return True

	def buildQuery(self):
		#self.SetQueryOk(False)
		result = True
		if self.query_from == 0: # from field
			result = False
			self.log_field.AppendText("\tLoading query from text field...\n")
			result = self.loadFromField()
			self.update_query = False
			result = True
		elif self.update_query: 
			self.query = None
			if self.query_from == 1: # from file
				self.log_field.AppendText("\tLoading query from file " + str(self.query_file) +"...\n")
				result = self.loadFromFile()
			elif self.query_from == 2: # from ac
				if self.query_type == 0:
					self.log_field.AppendText("Cannot get pairs from Annotation Corpus.\n")
				elif self.query_type == 1:
					self.log_field.AppendText("\tLoading query list from Annotation Corpus...\n")
					result = self.loadFromAC()
		else:
			self.log_field.AppendText("Using previous query...\n")
			result = True
		if result:
			self.update_query = False
		else:
			self.update_query = True
			self.query = None
		#self.SetQueryOk(result)
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
		if self.running:
			print "Stop"
		return True

	def start(self):
		#if not self.running:
		self.log_field.AppendText("Evaluating semantic similarity...\n")
		self.OutputGui.output_field.Clear()
		self.OutputGui.Show()
		#self.ssthread = WorkThread.WorkThread(self)
		#self.running = True
		#self.ssthread.start()
		self.skip_checks = False
		self.log_field.AppendText('--------------------------------------\n')
			#----------------------------------------------------------------------------------------------------
		#check if everything is configured
		if not self.skip_checks:
			if not self.go_ok:
				self.log_field.AppendText("Check Gene Ontology. Aborted\n")
				#self.logfield.AppendText("Aborted.\n")
				return False
			if not self.ac_ok:
				self.log_field.AppendText("Check Annotation Corpus. Aborted.\n")
				return False
			if not self.query_ok:
				self.log_field.AppendText("Check query. Aborted.\n")
				#self.logfield.AppendText("Aborted.\n")
				return False
			if not self.outputctrl_ok:
				self.log_field.AppendText("Check output parameters. Aborted.\n")
				#self.logfield.AppendText("Aborted.\n")
				return False
			if not self.operation_ok:
				self.log_field.AppendText("Check operation parameters. Aborted.\n")
			#self.logfield.AppendText("Aborted.\n")
				return False
		#----------------------------------------------------------------------------------------------------
		self.log_field.AppendText("Data seems to be ok. Inizializing structures...\n")
		#Prepare sem sim object
		self.log_field.AppendText("-> Setting up semantic similarity...\n")
		if not self.buildSSobject():
			self.log_field.AppendText("-> Failed to initialize semantic similarity measure. Aborted.\n")
			return False
		#----------------------------------------------------------------------------------------------------
		# Prepare query
		self.log_field.AppendText("-> Setting up query...\n")
		if not self.buildQuery():
			self.log_field.AppendText("Failed to load query. Aborted.\n")
		else:
			if self.query_type == 0:
				self.log_field.AppendText("\tQuery loaded:" + (str(len(self.query))) + " pairs\n")
			elif self.query_type == 1:
				self.log_field.AppendText("Query loaded: " + str(len(self.query)) + " items.\n")
				print self.query
		#----------------------------------------------------------------------------------------------------
		# Calculate SS scores
		self.log_field.AppendText("Evaluating semantic similarity...\n")
		self.ssthread = WorkThread.WorkThread(self)
		self.update_event = threading.Event()
		self.running = True
		self.ssthread.start()
		print "Done"
		return True



#################################################################################################################################

	def OnProgress(self, msg):
		print "Updating progress bar..."
		t = msg.data
		gaugerange = self.progress.GetRange()
		self.progress.SetValue(t*gaugerange)
		self.OnUpdateDone()

	def OnCompleted(self, msg):
		t = msg.data
		self.log_field.AppendText("Completed\n")
		self.running = False
		self.OnUpdateDone()
		
	def OnOutputData(self, msg):
		print "Printing output data"
		t = msg.data
		#print t
		for i in t: #range(t[0], t[1] + 1):
			#frase = self.ssthread.buffer[i][0] + "\t" + self.ssthread.buffer[i][1] + "\t" + self.ssthread.buffer[i][2] + "\n"
			frase = str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n"
			self.OutputGui.output_field.AppendText(frase)
		print "Output data printed"
		self.OnUpdateDone()

	def OnLogData(self, msg):
		t = msg.data
		self.log_field.AppendText(t)
		self.OnUpdateDone()
		
	def OnUpdateDone(self):
		print "Update done"
		self.update_event.set()

#################################################################################################################################

if __name__ == "__main__":
	app = wx.App()
	window = fastSemSimGui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
