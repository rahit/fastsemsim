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

#### Import basic packages
import sys
import os

#### Import fastSemSim modules
from fastSemSim.GO import GeneOntology
from fastSemSim.GO import AnnotationCorpus
from fastSemSim.SemSim import SemSimMeasures
from fastSemSim.SemSim import ObjSemSim

#### Include this to work with threads. Not really good for GUI
#from gui import WorkThread
#import threading

#### Include this to work with processes
import WorkProcess
import multiprocessing 

#### Import wxWidgets
#from wx.Python.wx import * # old definition
import wx

#### Import modules
#from GeneOntologyGui import GeneOntologyGui
#from AnnotationCorpusGui import AnnotationCorpusGui
#from OperationGui import OperationGui
#from OutputCtrlGui import OutputCtrlGui
#from OutputGui import OutputGui
#from ConfigGui import *
#from ControlGui import ControlGui
#from QueryGui import QueryGui
#from StatusGui import StatusGui

#################################################################################

debugging = False
#debugging = True

class fastSemSimGui(wx.Frame):

	## variables to control exclusive communication between gui and background process
	#process_busy = False
	#process_busy_lock = None
	#process_busy_event = None
	#UPDATE_INTERVAL = 500
	## temp variables to be removed
	#superconta = 0
	
	debug = True # Switch to False when done
	##Components handles
	#GOGui = None
	#ACGui = None
	#OperationGui = None
	#QueryGui = None
	#OutputCtrlGui = None
	#OutputGui = None
	
	##data structures
	#config_file = None
	#go = None
	#ac = None
	#selectedGO = None
	#mixingstrategy = None
	#ssmeasure = None
	#output_type = None # 0 = field, 1 = file
	#output_file = None
	#query_type = None # 0 = pairs, 1 = list
	##query_from_ac = False # True if load from ac <-- obsolete!
	#query_from = None # 0 = field, 1 = file, 2 = ac
	#query_file = None
	
	##objects required for ss calculation
	#query = None # list of pairs or list of objects, depending on query_type variable
	#ssobject = None # semantic similarity measure
	
	##control data
	status = 0 # current status: -1 = fatal error, 0 = not running - to configure, 1 = ready to run, 2 = running
	#go_ok = False
	#ac_ok = False
	#query_ok = False
	#outputctrl_ok = False
	#operation_ok = False
	#start_cmd = None # main command to start execution
	
	##flags signaling whether some structures should be updated
	#update_query = True
	#update_ssobject = True
	#update_ac = True
	
	##other data
	##Ok_pic = 'gui/V_30.png'
	##Warning_pic = 'gui/W_30.png'

	#show_pics = True
	#go_status_pic = None
	#ac_status_pic = None
	#query_status_pic = None
	#outputctrl_status_pic = None
	#output_status_pic = None
	#operation_status_pic = None
	#status_pic = None

	# multiprocessing data
	ssprocess = []
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "fastSemSimGui v.2 - Marco Mina", pos = wx.DefaultPosition, size = wx.Size( 652,471 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		####
		self.process_busy = False
		self.process_busy_lock = multiprocessing.Lock()
		self.process_busy_event = multiprocessing.Event()
		
		self.programdirectory = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
		#self.programdirectory = 'images' # use this with py2exe to build a working binary
		self.Ok_pic = self.programdirectory + '/V_30.png'
		self.Warning_pic = self.programdirectory + '/W_30.png'
		self.Advanced_pic = self.programdirectory + '/advanced.png'
	
		self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(9)
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
		####
		
		self.InitWorkProcess()
		#self.OnAnyUpdate()
		####
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		fastSemSim_sizer_1 = wx.BoxSizer( wx.VERTICAL )
		self.fastSemSim_listbook = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		fastSemSim_sizer_1.Add( self.fastSemSim_listbook, 1, wx.EXPAND |wx.ALL, 5 ) #### This section was in the end
		self.SetSizer( fastSemSim_sizer_1 )
		self.Layout()
		self.fastSemSim_statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.Centre( wx.BOTH )

		#### Panel GO
		self.GO_panel = GOPanel( self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.GO_panel, u"Gene Ontology", False )
		#### Panel AC
		self.AC_panel = ACPanel( self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.AC_panel, u"Annotation Corpus", False )
		#### Panel SS
		self.SS_panel = SSPanel( self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.SS_panel, u"Semantic Similarity", False )
		#### Panel Query
		self.query_panel = QueryPanel( self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.query_panel, u"Query", False )
		#### Panel Output Ctrl
		self.output_ctrl_panel = OutputCtrlPanel( self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.output_ctrl_panel, u"Output Settings", False )
		#### Panel Controls
		self.controls_panel = ControlsPanel( self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.controls_panel, u"Controls", False )
		#### Panel Output
		self.output_panel = OutputPanel( self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.output_panel, u"Output", True )

#############################################################################################
#############################################################################################
#################           PROCESS COMMUNICATION     #######################################
#############################################################################################
#############################################################################################

#### Process Handlers
	def InitWorkProcess(self):
		self.running = False
		self.ssprocess.append(None)
		
		self.TIMER_ID = 100
		self.timer = wx.Timer(self, self.TIMER_ID)
		wx.EVT_TIMER(self, self.TIMER_ID, self.OnCheckPipes)
   
		self.activateGoCmd()
		self.init_process()
		self.timer.Start(1000)

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

#############################################################################################

	def stop(self):
		self.stop_process()
		self.SetStatus(1)
		return True

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

#############################################################################################
#############################################################################################
#################           LOGIC          ##################################################
#############################################################################################
#############################################################################################

	def OnAnyUpdate(self):
		#self.statusgridbox.Fit(self)
		#self.gostatsbox.Fit(self)
		#self.commandbox.Fit(self)
		self.mainbox.Fit(self)
		#w,h = self.commandbox.GetSizeTuple()
		#self.mainbox.SetItemMinSize(self.commandbox, w,h)
		#self.GetBestSize()
		self.mainbox.Layout()

	def activateGoCmd(self): # should not be called if status is 2
		if self.status == -1:
			return
		if self.debug or (self.go_ok and self.ac_ok and self.query_ok and self.outputctrl_ok and self.operation_ok):
			self.SetStatus(1) # set to 0
		else:
			self.SetStatus(0)

	def SetStatus(self, status):
		self.status = status
		return None ## To remove when complete
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

#############################################################################################
#############################################################################################
#################           GUI EVENTS HANDLERS          ####################################
#############################################################################################
#############################################################################################

#### Events Handlers
	def OnQuit(self, event):
		self.ssprocess[0].terminate()
		sys.exit()
		
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
#

#################################################################################################################################
#################################################################################################################################
#################           END                          ########################################################################
#################################################################################################################################
#################################################################################################################################

class GOPanel(wx.Panel):
	def __init__( self, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.GO_panel = self # temporary workaround
		GO_panel_sizer_1 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.GO_panel, wx.ID_ANY, u"Source" ), wx.HORIZONTAL )
		
		self.GO_source_label = wx.StaticText( self.GO_panel, wx.ID_ANY, u"No file loaded", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.GO_source_label.Wrap( -1 )
		sbSizer3.Add( self.GO_source_label, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.GO_load_button = wx.Button( self.GO_panel, wx.ID_ANY, u"Load ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GO_load_button.SetDefault() 
		sbSizer3.Add( self.GO_load_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		GO_panel_sizer_1.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.GO_panel, wx.ID_ANY, u"Statistics" ), wx.HORIZONTAL )
		
		gSizer2 = wx.GridSizer( 6, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self.GO_panel, wx.ID_ANY, u"Terms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.GO_terms_label = wx.StaticText( self.GO_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GO_terms_label.Wrap( -1 )
		gSizer2.Add( self.GO_terms_label, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.GO_panel, wx.ID_ANY, u"Edges", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.GO_edges_label = wx.StaticText( self.GO_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GO_edges_label.Wrap( -1 )
		gSizer2.Add( self.GO_edges_label, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.GO_panel, wx.ID_ANY, u"Categories", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.GO_categories_label = wx.StaticText( self.GO_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GO_categories_label.Wrap( -1 )
		gSizer2.Add( self.GO_categories_label, 0, wx.ALL, 5 )
		
		sbSizer5.Add( gSizer2, 1, wx.ALIGN_CENTER|wx.SHAPED, 2 )
		
		bSizer5.Add( sbSizer5, 0, wx.ALL, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.GO_panel, wx.ID_ANY, u"Additional information" ), wx.VERTICAL )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText8 = wx.StaticText( self.GO_panel, wx.ID_ANY, u"what has been accepted?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer51.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		sbSizer6.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		bSizer5.Add( sbSizer6, 0, wx.ALL, 5 )
		
		GO_panel_sizer_1.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		GO_panel_sizer_1.Add( bSizer4, 0, wx.ALIGN_RIGHT, 5 )
		
		self.GO_panel.SetSizer( GO_panel_sizer_1 )
		self.GO_panel.Layout()
		GO_panel_sizer_1.Fit( self.GO_panel )
#

class ACPanel(wx.Panel):
	def __init__( self, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.AC_panel = self # temporary workaround
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.AC_panel, wx.ID_ANY, u"Source file" ), wx.HORIZONTAL )
		
		self.AC_source_label = wx.StaticText( self.AC_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AC_source_label.Wrap( -1 )
		sbSizer31.Add( self.AC_source_label, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.AC_load_button = wx.Button( self.AC_panel, wx.ID_ANY, u"Load ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AC_load_button.SetDefault() 
		sbSizer31.Add( self.AC_load_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer28.Add( sbSizer31, 6, wx.ALL|wx.EXPAND, 5 )
		
		bSizer31.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self.AC_panel, wx.ID_ANY, u"Statistics" ), wx.HORIZONTAL )
		
		gSizer21 = wx.GridSizer( 6, 2, 0, 0 )
		
		self.m_staticText21 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"Terms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer21.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer21.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"Edges", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		gSizer21.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		gSizer21.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"Categories", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		gSizer21.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		gSizer21.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		sbSizer51.Add( gSizer21, 1, wx.ALIGN_CENTER|wx.SHAPED, 2 )
		
		bSizer52.Add( sbSizer51, 0, wx.ALL, 5 )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.AC_panel, wx.ID_ANY, u"Additional information" ), wx.VERTICAL )
		
		bSizer511 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText18 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"File type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gbSizer1.Add( self.m_staticText18, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		gbSizer1.Add( self.m_staticText19, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"MyLabel", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gbSizer1.Add( self.m_staticText20, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		gbSizer1.Add( self.m_staticText211, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gbSizer1.Add( self.m_staticText22, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.AC_panel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gbSizer1.Add( self.m_staticText23, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		bSizer511.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer61.Add( bSizer511, 1, wx.EXPAND, 5 )
		
		bSizer52.Add( sbSizer61, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer31.Add( bSizer52, 0, wx.EXPAND, 5 )
		
		self.AC_panel.SetSizer( bSizer31 )
		self.AC_panel.Layout()
		bSizer31.Fit( self.AC_panel )
#

class SSPanel(wx.Panel):
	def __init__( self, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.SS_panel = self # temporary workaround

		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.SS_panel, wx.ID_ANY, u"Semantic Measure" ), wx.HORIZONTAL )
		
		SS_measure_boxChoices = []
		self.SS_measure_box = wx.ComboBox( self.SS_panel, wx.ID_ANY, u"Resnik", wx.DefaultPosition, wx.DefaultSize, SS_measure_boxChoices, 0 )
		sbSizer15.Add( self.SS_measure_box, 0, wx.ALL, 5 )
		
		self.SS_measure_settings_button = wx.BitmapButton( self.SS_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		sbSizer15.Add( self.SS_measure_settings_button, 0, wx.ALL, 5 )
		
		bSizer26.Add( sbSizer15, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.SS_panel, wx.ID_ANY, u"Mixing Strategy" ), wx.HORIZONTAL )
		
		SS_mix_boxChoices = []
		self.SS_mix_box = wx.ComboBox( self.SS_panel, wx.ID_ANY, u"BMA", wx.DefaultPosition, wx.DefaultSize, SS_mix_boxChoices, 0 )
		sbSizer16.Add( self.SS_mix_box, 0, wx.ALL, 5 )
		
		self.SS_mix_settings_button = wx.BitmapButton( self.SS_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		sbSizer16.Add( self.SS_mix_settings_button, 0, wx.ALL, 5 )
		
		bSizer26.Add( sbSizer16, 1, wx.EXPAND|wx.RIGHT|wx.TOP, 5 )
		
		bSizer27.Add( bSizer26, 0, 0, 5 )
		
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.SS_panel, wx.ID_ANY, u"Ontology" ), wx.VERTICAL )
		
		self.SS_GO_MF_radio = wx.RadioButton( self.SS_panel, wx.ID_ANY, u"Molecular Function (MF)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.SS_GO_MF_radio, 0, wx.ALL, 5 )
		
		self.SS_GO_CC_radio = wx.RadioButton( self.SS_panel, wx.ID_ANY, u"Cellular Component (CC)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.SS_GO_CC_radio, 0, wx.ALL, 5 )
		
		self.SS_GO_BP_radio = wx.RadioButton( self.SS_panel, wx.ID_ANY, u"Biological Process (BP)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.SS_GO_BP_radio, 0, wx.ALL, 5 )
		
		bSizer27.Add( sbSizer17, 0, wx.LEFT, 5 )
		
		bSizer25.Add( bSizer27, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SS_panel.SetSizer( bSizer25 )
		self.SS_panel.Layout()
		bSizer25.Fit( self.SS_panel )

#

class QueryPanel(wx.Panel):
	def __init__( self, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.query_panel = self # temporary workaround

		bSizer50 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer36 = wx.StaticBoxSizer( wx.StaticBox( self.query_panel, wx.ID_ANY, u"Input method" ), wx.VERTICAL )
		
		self.query_input_method_box = wx.Choicebook( self.query_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.m_panel22 = wx.Panel( self.query_input_method_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer512 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer312 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"Input field" ), wx.VERTICAL )
		
		self.query_field_text = wx.TextCtrl( self.m_panel22, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,250 ), wx.TE_MULTILINE )
		self.query_field_text.SetMinSize( wx.Size( 250,250 ) )
		
		sbSizer312.Add( self.query_field_text, 0, wx.ALL, 5 )
		
		bSizer512.Add( sbSizer312, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer32 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"Input format" ), wx.VERTICAL )
		
		query_field_type_boxChoices = []
		self.query_field_type_box = wx.ComboBox( self.m_panel22, wx.ID_ANY, u"List", wx.DefaultPosition, wx.Size( 120,-1 ), query_field_type_boxChoices, wx.CB_READONLY )
		sbSizer32.Add( self.query_field_type_box, 0, wx.ALL, 5 )
		
		bSizer54.Add( sbSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		sbSizer33 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"Help" ), wx.VERTICAL )
		
		self.m_staticText53 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"You can either specify a list of object or a set of pairs of objects. In the former case, the semantic similarity will be evaluated between each pair of objects in the list. In the latter, each pair will be considered", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText53.Wrap( -1 )
		sbSizer33.Add( self.m_staticText53, 0, wx.ALL, 5 )
		
		bSizer54.Add( sbSizer33, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.query_reset_button = wx.Button( self.m_panel22, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer54.Add( self.query_reset_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer512.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		self.m_panel22.SetSizer( bSizer512 )
		self.m_panel22.Layout()
		bSizer512.Fit( self.m_panel22 )
		self.query_input_method_box.AddPage( self.m_panel22, u"Manual input", False )
		self.m_panel23 = wx.Panel( self.query_input_method_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer521 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer34 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel23, wx.ID_ANY, u"Source file" ), wx.HORIZONTAL )
		
		self.query_input_file_label = wx.StaticText( self.m_panel23, wx.ID_ANY, u"No file selected.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.query_input_file_label.Wrap( -1 )
		sbSizer34.Add( self.query_input_file_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer22.Add( sbSizer34, 1, wx.LEFT|wx.RIGHT, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.query_load_button = wx.Button( self.m_panel23, wx.ID_ANY, u"Select file...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.query_load_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer22.Add( bSizer20, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 5 )
		
		bSizer32.Add( bSizer22, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.TOP, 5 )
		
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer29 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel23, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		fgSizer8 = wx.FlexGridSizer( 3, 3, 15, 5 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText30 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Separator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer8.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		bSizer46 = wx.BoxSizer( wx.VERTICAL )
		
		self.query_sep_tab_radio = wx.RadioButton( self.m_panel23, wx.ID_ANY, u"[tab]  '\\t'", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.query_sep_tab_radio, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		self.query_sep_space_radio = wx.RadioButton( self.m_panel23, wx.ID_ANY, u"[space]", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.query_sep_space_radio, 0, wx.LEFT|wx.RIGHT, 5 )
		
		bSizer47 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.query_sep_custom_radio = wx.RadioButton( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer47.Add( self.query_sep_custom_radio, 0, wx.LEFT|wx.RIGHT, 5 )
		
		self.query_sep_custom_text = wx.TextCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer47.Add( self.query_sep_custom_text, 0, wx.RIGHT, 5 )
		
		bSizer46.Add( bSizer47, 1, wx.EXPAND, 5 )
		
		fgSizer8.Add( bSizer46, 1, wx.EXPAND, 5 )
		
		self.m_staticText48 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Character used to separate fields within each row.", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText48.Wrap( -1 )
		fgSizer8.Add( self.m_staticText48, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText511 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Input type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )
		fgSizer8.Add( self.m_staticText511, 0, wx.ALL, 5 )
		
		query_file_type_boxChoices = [ u"Pairs", u"List" ]
		self.query_file_type_box = wx.ComboBox( self.m_panel23, wx.ID_ANY, u"Pairs", wx.DefaultPosition, wx.Size( 100,-1 ), query_file_type_boxChoices, wx.CB_READONLY )
		fgSizer8.Add( self.query_file_type_box, 0, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Select whether the input is a list of objects or a set of pairs first field of each row is an object or a GO Term.", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText52.Wrap( -1 )
		fgSizer8.Add( self.m_staticText52, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sbSizer29.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		bSizer56.Add( sbSizer29, 1, wx.EXPAND, 5 )
		
		bSizer55.Add( bSizer56, 1, wx.EXPAND, 5 )
		
		bSizer32.Add( bSizer55, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel23, wx.ID_ANY, u"Help" ), wx.VERTICAL )
		
		self.m_staticText311 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Select a file", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText311.Wrap( -1 )
		self.m_staticText311.SetMaxSize( wx.Size( 500,-1 ) )
		
		sbSizer18.Add( self.m_staticText311, 0, wx.ALL, 5 )
		
		bSizer32.Add( sbSizer18, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer521.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		self.m_panel23.SetSizer( bSizer521 )
		self.m_panel23.Layout()
		bSizer521.Fit( self.m_panel23 )
		self.query_input_method_box.AddPage( self.m_panel23, u"Load query from file", True )
		self.m_panel24 = wx.Panel( self.query_input_method_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer53 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer181 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel24, wx.ID_ANY, u"Help" ), wx.VERTICAL )
		
		self.m_staticText3111 = wx.StaticText( self.m_panel24, wx.ID_ANY, u"All the objects in the annotation corpus will be used as input list. Pairwise Semantic Similarity will be evaluated on such list", wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		self.m_staticText3111.Wrap( -1 )
		self.m_staticText3111.SetMaxSize( wx.Size( 500,-1 ) )
		
		sbSizer181.Add( self.m_staticText3111, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer53.Add( sbSizer181, 0, wx.EXPAND, 5 )
		
		self.m_panel24.SetSizer( bSizer53 )
		self.m_panel24.Layout()
		bSizer53.Fit( self.m_panel24 )
		self.query_input_method_box.AddPage( self.m_panel24, u"Annotation Corpus", False )
		sbSizer36.Add( self.query_input_method_box, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer50.Add( sbSizer36, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.query_panel.SetSizer( bSizer50 )
		self.query_panel.Layout()
		bSizer50.Fit( self.query_panel )
#

class OutputCtrlPanel(wx.Panel):
	def __init__( self, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.output_ctrl_panel = self # temporary workaround

		
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer511 = wx.StaticBoxSizer( wx.StaticBox( self.output_ctrl_panel, wx.ID_ANY, u"Output parameters" ), wx.VERTICAL )
		
		sbSizer291 = wx.StaticBoxSizer( wx.StaticBox( self.output_ctrl_panel, wx.ID_ANY, u"Filter Options" ), wx.VERTICAL )
		
		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1081 = wx.StaticText( self.output_ctrl_panel, wx.ID_ANY, u"Remove pairs with Semantic Similarity", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText1081.Wrap( -1 )
		gbSizer9.Add( self.m_staticText1081, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.output_filter_none_check = wx.CheckBox( self.output_ctrl_panel, wx.ID_ANY, u"= 'None'", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.output_filter_none_check, 0, 0, 5 )
		
		self.output_filter_0_check = wx.CheckBox( self.output_ctrl_panel, wx.ID_ANY, u"= 0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.output_filter_0_check, 0, 0, 5 )
		
		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.query_filter_less_check = wx.CheckBox( self.output_ctrl_panel, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.query_filter_less_check, 0, 0, 5 )
		
		self.query_filter_less_text = wx.TextCtrl( self.output_ctrl_panel, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.query_filter_less_text.SetMaxSize( wx.Size( 70,-1 ) )
		
		bSizer112.Add( self.query_filter_less_text, 0, 0, 5 )
		
		bSizer111.Add( bSizer112, 1, wx.EXPAND, 5 )
		
		gbSizer9.Add( bSizer111, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer291.Add( gbSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer511.Add( sbSizer291, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer52 = wx.StaticBoxSizer( wx.StaticBox( self.output_ctrl_panel, wx.ID_ANY, u"Redirect output to" ), wx.VERTICAL )
		
		self.output_to_box = wx.Choicebook( self.output_ctrl_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.m_panel29 = wx.Panel( self.output_to_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer95 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel29.SetSizer( bSizer95 )
		self.m_panel29.Layout()
		bSizer95.Fit( self.m_panel29 )
		self.output_to_box.AddPage( self.m_panel29, u"Output Form", False )
		self.m_panel30 = wx.Panel( self.output_to_box, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer94 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer321 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer221 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer341 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel30, wx.ID_ANY, u"Destination file" ), wx.HORIZONTAL )
		
		self.output_file_label = wx.StaticText( self.m_panel30, wx.ID_ANY, u"No file selected.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_file_label.Wrap( -1 )
		sbSizer341.Add( self.output_file_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer221.Add( sbSizer341, 1, wx.LEFT|wx.RIGHT, 5 )
		
		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.output_file_select_button = wx.Button( self.m_panel30, wx.ID_ANY, u"Select file...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.output_file_select_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer221.Add( bSizer201, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 5 )
		
		bSizer321.Add( bSizer221, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.TOP, 5 )
		
		bSizer551 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer561 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer551.Add( bSizer561, 1, wx.EXPAND, 5 )
		
		bSizer321.Add( bSizer551, 0, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer2911 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel30, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		gbSizer91 = wx.GridBagSizer( 0, 0 )
		gbSizer91.SetFlexibleDirection( wx.BOTH )
		gbSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3011 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Separator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3011.Wrap( -1 )
		gbSizer91.Add( self.m_staticText3011, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		bSizer4611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.output_sep_tab_radio = wx.RadioButton( self.m_panel30, wx.ID_ANY, u"[tab]  '\\t'", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4611.Add( self.output_sep_tab_radio, 0, wx.ALL, 5 )
		
		self.output_sep_space_radio = wx.RadioButton( self.m_panel30, wx.ID_ANY, u"[space]", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4611.Add( self.output_sep_space_radio, 0, wx.ALL, 5 )
		
		bSizer4711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.output_sep_custom_radio = wx.RadioButton( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4711.Add( self.output_sep_custom_radio, 0, wx.ALL|wx.LEFT|wx.RIGHT, 5 )
		
		self.output_sep_custom_text = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer4711.Add( self.output_sep_custom_text, 0, wx.ALL|wx.RIGHT, 5 )
		
		bSizer4611.Add( bSizer4711, 1, wx.EXPAND, 5 )
		
		gbSizer91.Add( bSizer4611, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer2911.Add( gbSizer91, 1, wx.EXPAND, 5 )
		
		bSizer321.Add( sbSizer2911, 1, wx.EXPAND, 5 )
		
		bSizer94.Add( bSizer321, 1, wx.EXPAND, 5 )
		
		self.m_panel30.SetSizer( bSizer94 )
		self.m_panel30.Layout()
		bSizer94.Fit( self.m_panel30 )
		self.output_to_box.AddPage( self.m_panel30, u"File", True )
		sbSizer52.Add( self.output_to_box, 0, wx.EXPAND |wx.ALL, 5 )
		
		sbSizer511.Add( sbSizer52, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer93.Add( sbSizer511, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.output_ctrl_panel.SetSizer( bSizer93 )
		self.output_ctrl_panel.Layout()
		bSizer93.Fit( self.output_ctrl_panel )
#


class OutputPanel(wx.Panel):
	pass
#

class ControlsPanel(wx.Panel):
	def __init__( self, parent, id, pos, size, style):
		wx.Panel.__init__ ( self, parent, id, pos, size, style)
		self.controls_panel = self # temporary workaround
		
		bSizer62 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer35 = wx.StaticBoxSizer( wx.StaticBox( self.controls_panel, wx.ID_ANY, u"Log" ), wx.VERTICAL )
		
		self.controls_log_text = wx.TextCtrl( self.controls_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,300 ), wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer35.Add( self.controls_log_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer62.Add( sbSizer35, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer63 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.controls_start_button = wx.Button( self.controls_panel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer63.Add( self.controls_start_button, 0, wx.ALL, 5 )
		
		self.controls_stop_button = wx.Button( self.controls_panel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer63.Add( self.controls_stop_button, 0, wx.ALL, 5 )
		
		bSizer62.Add( bSizer63, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.controls_panel.SetSizer( bSizer62 )
		self.controls_panel.Layout()
		bSizer62.Fit( self.controls_panel )
	#

#

################################################################################################
####################################################################################
################################################################################################
####################################################################################
################################################################################################
####################################################################################
################################################################################################
####################################################################################
################################################################################################
####################################################################################
################################################################################################
####################################################################################

#### Old code




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


#################################
#'''
#Following routines start/stop ss computation
#'''


#################################

#'''
#Following routines handle communications with other processes 
#'''



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


##################################################################################
#### start the main gui. Should be called from outside. Why? ####
##################################################################################

def _start():
	multiprocessing.freeze_support()
	app = wx.App()
	window = fastSemSimGui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()
#

if __name__=='__main__':
	_start()
#
