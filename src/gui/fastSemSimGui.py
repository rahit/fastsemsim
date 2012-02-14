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
import sys
import os
from fastSemSim.GO import GeneOntology
from fastSemSim.GO import AnnotationCorpus
from GeneOntologyGui import GeneOntologyGui
from AnnotationCorpusGui import AnnotationCorpusGui
from OperationGui import OperationGui
from OutputCtrlGui import OutputCtrlGui
from OutputGui import OutputGui
from ConfigGui import *
from ControlGui import ControlGui
from QueryGui import QueryGui
from StatusGui import StatusGui
from fastSemSim.SemSim import SemSimMeasures
from fastSemSim.SemSim import ObjSemSim
#from gui import WorkThread
import WorkProcess
#import threading
import multiprocessing

debugging = False
#debugging = True

class fastSemSimGui(wx.Frame):
	# variables to control exclusive communication between gui and background process
	process_busy = False
	process_busy_lock = None
	process_busy_event = None
	UPDATE_INTERVAL = 500
	# temp variables to be removed
	superconta = 0
	
	debug = True
	#Components handles
	GOGui = None
	ACGui = None
	OperationGui = None
	QueryGui = None
	OutputCtrlGui = None
	OutputGui = None
	
	#data structures
	config_file = None
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
	#Ok_pic = 'gui/V_30.png'
	#Warning_pic = 'gui/W_30.png'

	show_pics = True
	go_status_pic = None
	ac_status_pic = None
	query_status_pic = None
	outputctrl_status_pic = None
	output_status_pic = None
	operation_status_pic = None
	status_pic = None

	# multiprocessing data
	ssprocess = []

	def __init__(self, parent):
		super(fastSemSimGui, self).__init__(parent, title="fastSemSim - Copyright 2011, Marco Mina - beta version", style = wx.RESIZE_BORDER | wx.DEFAULT_FRAME_STYLE)
		self.process_busy = False
		self.process_busy_lock = multiprocessing.Lock()
		self.process_busy_event = multiprocessing.Event()
		
		self.programdirectory = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
		self.Ok_pic = self.programdirectory + '/V_30.png'
		self.Warning_pic = self.programdirectory + '/W_30.png'
		self.Advanced_pic = self.programdirectory + '/advanced.png'
	
		self.InitUI()

	def InitWorkProcess(self):
		self.running = False
		self.ssprocess.append(None)
		
		self.TIMER_ID = 100
		self.timer = wx.Timer(self.panel, self.TIMER_ID)
		wx.EVT_TIMER(self.panel, self.TIMER_ID, self.OnCheckPipes)
   
		self.activateGoCmd()
		self.init_process()
		self.timer.Start(1000)

	def InitUI(self):
		self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(9)

		self.panel = wx.Panel(self)
		self.mainbox = wx.BoxSizer(wx.VERTICAL)
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())

		self.InitWorkProcess()

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
		
		self.panel.SetSizer(self.mainbox)

		#### initialize other components
		self.StatusGui = StatusGui(self)
		self.GOGui = GeneOntologyGui(self)
		self.ACGui = AnnotationCorpusGui(self)
		self.OperationGui = OperationGui(self)
		self.OutputCtrlGui = OutputCtrlGui(self)
		self.QueryGui = QueryGui(self)
		self.OutputGui = OutputGui(self)
		self.ControlGui = ControlGui(self)
		self.OnAnyUpdate()

	def OnAnyUpdate(self):
		#self.statusgridbox.Fit(self)
		#self.gostatsbox.Fit(self)
		#self.commandbox.Fit(self)
		self.mainbox.Fit(self)
		#w,h = self.commandbox.GetSizeTuple()
		#self.mainbox.SetItemMinSize(self.commandbox, w,h)
		#self.GetBestSize()
		self.mainbox.Layout()
		
		#self.InitMenu()
#----------------------------------------------------------------------------------------------------------------------------------
	#'''
	#Menubar
	#'''
	def InitMenu(self):
		self.ID_NEW=wx.NewId()
		self.ID_OPEN=wx.NewId()
		self.ID_QUIT=wx.NewId()
		self.ID_SAVE=wx.NewId()
		self.ID_SAVE_AS=wx.NewId()
		self.MenuBar = wx.MenuBar()
		self.FileMenu = wx.Menu()
		self.FileMenu.Append(self.ID_NEW, 'New', 'New')
		self.FileMenu.Append(self.ID_OPEN, 'Open Configuration...', 'Open Configuration')
		self.FileMenu.Append(self.ID_SAVE, 'Save Configuration', 'Save Configuration')
		self.FileMenu.Append(self.ID_SAVE_AS, 'Save Configuration As...', 'Save Configuration As')
		self.FileMenu.Append(self.ID_QUIT, 'Quit', 'Quit application')
		self.MenuBar.Append(self.FileMenu,'&File')
		self.SetMenuBar(self.MenuBar)
		self.Bind(wx.EVT_MENU, self.OnMenuQuit, id=self.ID_QUIT)
		self.Bind(wx.EVT_MENU, self.OnMenuOpen, id=self.ID_OPEN)
		self.Bind(wx.EVT_MENU, self.OnMenuSave, id=self.ID_SAVE)
		self.Bind(wx.EVT_MENU, self.OnMenuSaveAs, id=self.ID_SAVE_AS)
		self.Bind(wx.EVT_MENU, self.OnMenuNew, id=self.ID_NEW)
		return True
	
	def OnMenuNew(self, event):
		print "OnMenuNew still to be implemented."

	def OnMenuQuit(self, event):
		print "OnMenuQuit still to be implemented correctly."
		sys.exit()

	def OnMenuOpen(self, event):
		print "OnMenuOpen still to be implemented."
		dialog = wx.FileDialog(None, style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			print 'Loading: ', dialog.GetPath()
			if not self.config_file == None:
				self.OnMenuNew(None)
			self.config_file = dialog.GetPath()
			self.loadConfigGui = LoadConfigGui(self)

	def OnMenuSave(self, event):
		if self.config_file == None:
			return self.OnMenuSaveAs(event)
		self.saveConfigGui = SaveConfigGui(self)

	def OnMenuSaveAs(self, event):
		dialog = wx.FileDialog(None, style = wx.SAVE|wx.OVERWRITE_PROMPT)
		if dialog.ShowModal() == wx.ID_OK:
			self.config_file = dialog.GetPath()
			self.OnMenuSave(event)

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

#################################
#'''
#Following routines start/stop ss computation
#'''

	def stop(self):
		self.stop_process()
		self.SetStatus(1)
		return True

	def init_process(self):
		if not self.running:
			self.gui2ssprocess_queue = multiprocessing.Queue()
			self.ssprocess2gui_queue = multiprocessing.Queue()
			self.gui2ssprocess_pipe, self.ssprocess2gui_pipe = multiprocessing.Pipe()
			self.ssprocess[0] = WorkProcess.WorkProcess(self.gui2ssprocess_queue, self.ssprocess2gui_queue, self.ssprocess2gui_pipe, self.gui2ssprocess_pipe)
			self.running = True
			self.ssprocess[0].start()
			return True
		else:
			print "Already executing"
			return False

	def loadFromField(self):
		h = self.QueryGui.text_query.GetValue()
		self.query= []
		h = h.splitlines()
		for line in h:
			if self.query_type == WorkProcess.QUERY_PAIRS:
				line = line.rsplit(' ')
				self.query.append((str(line[0]), str(line[1])))
			else:
				self.query.append(str(line))
		#print self.query
		return True

	def lock(self, wait = True):
		self.process_busy_lock.acquire()
		if not wait:
			if self.process_busy:
				self.process_busy_lock.release()
				return False
		else:
			while self.process_busy:
				self.process_busy_lock.release()
				self.process_busy_event.wait()
				self.process_busy_lock.acquire()
		self.process_busy = True
		self.process_busy_event.clear()
		self.process_busy_lock.release()
		return True

	def unlock(self):
		self.process_busy_lock.acquire()
		self.process_busy = False
		self.process_busy_event.clear()
		self.process_busy_event.set()
		self.process_busy_lock.release()
		return True
	
	def completed(self):
		self.progress.SetValue(self.progress.GetRange())
		self.running = False
		self.log_field.AppendText("Task completed.\n")
		self.SetStatus(1)
		
		
	def start_process(self):
		self.progress.SetValue(float(0))
		self.lock()
		self.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_SS, self.ssmeasure, None, self.mixingstrategy, None, self.selectedGO))
		data = self.ssprocess2gui_queue.get()
		self.SetStatus(2)
		self.gui2ssprocess_queue.put((WorkProcess.CMD_STATUS, None))
		data = self.ssprocess2gui_queue.get()
		if self.query_from == WorkProcess.QUERY_FROM_GUI:
			self.loadFromField()
		self.gui2ssprocess_queue.put((WorkProcess.CMD_START, self.query))
		data = self.ssprocess2gui_queue.get()
		self.unlock()
		if data[0] == WorkProcess.CMD_START and data[1]:
			self.pairs_to_process = data[2]
		else:
			return False
		return True

	def stop_process(self):
		print "stop called"
		#self.timer.Stop()
		#self.ssprocess[0].terminate()
		#self.ssprocess[0] = None
		#self.gui2ssprocess_queue.close()
		#self.gui2ssprocess_queue = None
		#self.gui2ssprocess_pipe.close()
		#self.gui2ssprocess_pipe = None
		#self.ssprocess2gui_pipe.close()
		#self.ssprocess2gui_pipe = None
		#self.sspdone = None
		#self.sstodo = None
		#self.sscompleted = None
		self.lock()
		print "got lock"
		self.gui2ssprocess_queue.put((WorkProcess.CMD_STOP, None))
		print "data sent"
		#data = self.ssprocess2gui_queue.get()
		print "got answer"
		self.unlock()
		self.running = False
		self.SetStatus(1)
		return True

	def start(self):
		self.log_field.AppendText('\n-------------\n')
		self.skip_checks = False#check if everything is configured
		if not self.skip_checks:
			if not self.go_ok:
				self.log_field.AppendText("Check Gene Ontology.\nAborted\n")
				return False
			if not self.ac_ok:
				self.log_field.AppendText("Check Annotation Corpus.\nAborted.\n")
				return False
			if not self.query_ok:
				self.log_field.AppendText("Check query.\nAborted.\n")
				return False
			if not self.outputctrl_ok:
				self.log_field.AppendText("Check output parameters.\nAborted.\n")
				return False
			if not self.operation_ok:
				self.log_field.AppendText("Check operation parameters.\nAborted.\n")
				return False
		#self.log_field.AppendText("Parameters accepted. Starting computation...\n")
		#self.log_field.AppendText("Evaluating semantic similarity...\n")
		if self.output_type == 0:
			self.OutputGui.output_field.Clear()
			self.OutputGui.Show()
		return self.start_process()

#################################

#'''
#Following routines handle communications with other processes 
#'''


	def OnCheckPipes(self,event):
		#print "timer elapsed"
		if self.ssprocess2gui_pipe.poll():
			#print "data!"
			tmp = self.ssprocess2gui_pipe.recv()
			self.OnOutputData(tmp)
			gaugerange = self.progress.GetRange()
			self.progress.SetValue((float(self.superconta)/self.pairs_to_process)*gaugerange)
			
		if self.lock(wait = False):
			#print "THIS CHECK"
			if not self.ssprocess2gui_queue.empty():
				data = self.ssprocess2gui_queue.get()
				#print data
				if data[0] == WorkProcess.CMD_STOP:
					if data[1]:
						self.completed()
					else:
						self.completed()
			self.unlock()
		else:
			pass
			#print "Busy"
		
		#self.OnProgress()
		#self.OnCompleted()

	#def OnProgress(self):
		##print "Updating progress bar..."
		#gaugerange = self.progress.GetRange()
		#self.progress.SetValue(self.sspdone.value*gaugerange)
		##self.OnUpdateDone()

	#def OnCompleted(self):
		#if self.sscompleted.value == 1:
			#self.log_field.AppendText("Finished.\n")
			#print self.superconta
			##self.running = False
			#self.stop()
		
	def OnOutputData(self, t):
		#print "Printing output data"
		#print t
		
		#for i in t: #range(t[0], t[1] + 1):
			##frase = self.ssprocess[0].buffer[i][0] + "\t" + self.ssprocess[0].buffer[i][1] + "\t" + self.ssprocess[0].buffer[i][2] + "\n"
			#self.superconta += 1
			#frase = str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n"
			#self.OutputGui.output_field.AppendText(frase)
		frase = ""
		for i in t: #range(t[0], t[1] + 1):
			#frase = self.ssprocess[0].buffer[i][0] + "\t" + self.ssprocess[0].buffer[i][1] + "\t" + self.ssprocess[0].buffer[i][2] + "\n"
			self.superconta += 1
			frase = frase + str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n"
		self.OutputGui.output_field.AppendText(frase)
		#print "Output data printed"
		#self.OnUpdateDone()

	def OnLogData(self, msg):
		t = msg.data
		self.log_field.AppendText(t)
		#self.OnUpdateDone()
		
	def OnUpdateDone(self):
		pass
		#print "Update done"
		#self.update_event.set()

	def OnQuit(self, event):
		self.ssprocess[0].terminate()
		sys.exit()

#################################################################################################################################
def go():
	multiprocessing.freeze_support()
	app = wx.App()
	window = fastSemSimGui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
