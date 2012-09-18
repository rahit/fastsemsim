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
import copy

#### Import fastSemSim modules
from fastSemSim.GO import GeneOntology
from fastSemSim.GO import AnnotationCorpus
from fastSemSim.SemSim import SemSimMeasures
from fastSemSim.SemSim import ObjSemSim

#### Include this to work with threads. Not really good for GUI
#from gui import WorkThread
import threading

#### Include this to work with processes
import WorkProcess
import multiprocessing 

#### Import wxWidgets
#from wx.Python.wx import * # old definition
import wx
import wx.lib.newevent

#### Import modules
from GOGui import *
from ACGui import *
from QueryGui import *
from SSGui import *
from OutputGui import *
from ControlsGui import *
#from ConfigGui import *
#from ControlGui import ControlGui
#from QueryGui import QueryGui
#from StatusGui import StatusGui

#################################################################################

DEBUG_LEVEL = 2



# WorkProcess is designed as a state machine. Here are the possible status
STATUS_BASE = 55
STATUS_INIT = STATUS_BASE + 0 # performing reset.
STATUS_WAIT = STATUS_BASE + 1 # waiting for requests.
STATUS_RUN = STATUS_BASE + 2 # computation in progress.
#







class fastSemSimGui(wx.Frame):

	status = STATUS_INIT # current status. Possible values: STATUS_INIT = uninitialized / to init, STATUS_WAIT = not running, STATUS_RUN = running, STATUS_FATAL = fatal error

	## variables to control exclusive communication between gui and background process
	#process_busy = False
	#process_busy_lock = None
	#process_busy_event = None
	#UPDATE_INTERVAL = 500
	
	##data structures
	#config_file = None
	param_go = None
	param_ac = None
	param_mixing_strategy = None
	param_ss_measure = None
	param_selected_GO = None
	param_query = None
	#output_type = None # 0 = field, 1 = file
	#output_file = None
	#query_type = None # 0 = pairs, 1 = list
	##query_from_ac = False # True if load from ac <-- obsolete!
	#query_from = None # 0 = field, 1 = file, 2 = ac
	#query_file = None
	
	##objects required for ss calculation
	#query = None # list of pairs or list of objects, depending on query_type variable
	#ssobject = None # semantic similarity measure

	running = False
	
	GO_status = False
	AC_status = False
	ss_status = False
	query_status = False
	output_status = False

	#start_cmd = None # main command to start execution
	
	##flags signaling whether some structures should be updated
	#update_query = True
	#update_ssobject = True
	#update_ac = True

	# multiprocessing data
	ssprocess = None
#










	# This method initialized the main GUI, the variables and the processes. When ready, status is set to 0
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "fastSemSimGui v.2 - Marco Mina", pos = wx.DefaultPosition, size = wx.Size( 652,471 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: init()"

# Set constants. Load images
		self.programdirectory = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
		#self.programdirectory = 'images' # use this with py2exe to build a working binary
		
		self.Ok_pic = self.programdirectory + '/V_30.png'
		self.Warning_pic = self.programdirectory + '/W_30.png'
		self.Advanced_pic = self.programdirectory + '/advanced_30.png'
		self.work_pic = self.programdirectory + '/work_30.png'
		self.query_pic = self.programdirectory + '/query_30.png'
		self.GO_ok_pic = self.programdirectory + '/GO_ok.png'
		self.GO_warn_pic = self.programdirectory + '/GO_warn.png'
		self.output_pic = self.programdirectory + '/output_30.png'
		self.SS_pic = self.programdirectory + '/tweak_30.png'
	
		self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(9)

		self.status_images = wx.ImageList(100,50)
		self.status_images.Add(wx.Bitmap(self.Ok_pic)) # 0
		self.status_images.Add(wx.Bitmap(self.Warning_pic)) # 1
		self.status_images.Add(wx.Bitmap(self.Advanced_pic)) # 2
		self.status_images.Add(wx.Bitmap(self.work_pic)) # 3
		self.status_images.Add(wx.Bitmap(self.query_pic)) # 4
		self.status_images.Add(wx.Bitmap(self.output_pic)) # 5
		self.status_images.Add(wx.Bitmap(self.SS_pic)) # 6
		self.status_images.Add(wx.Bitmap(self.GO_ok_pic)) # 7
		self.status_images.Add(wx.Bitmap(self.GO_warn_pic)) # 8

# Init modules
		self.status_handle = None
		self._init_process()
		
		self.Bind(wx.EVT_CLOSE, self.OnQuit, id=self.GetId())
		#self.activateGoCmd()
		#self.OnAnyUpdate()
		####

# Build main GUI
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		fastSemSim_sizer_1 = wx.BoxSizer( wx.VERTICAL )
		self.fastSemSim_listbook = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.fastSemSim_listbook.SetImageList(self.status_images)
		
		fastSemSim_sizer_1.Add( self.fastSemSim_listbook, 1, wx.EXPAND |wx.ALL, 5 ) #### This section was in the end
		self.SetSizer( fastSemSim_sizer_1 )
		self.Layout()
		self.fastSemSim_statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.Centre( wx.BOTH )

		#### Panel Controls
		self.controls_panel = ControlsPanel(self, self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.controls_panel, u"Controls", True )
		self.fastSemSim_listbook.SetPageImage(0, 3)
		
		#### Panel GO
		self.GO_panel = GOPanel(self, self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.GO_panel, u"Gene Ontology", False )
		self.fastSemSim_listbook.SetPageImage(1, 8)
		#### Panel AC
		self.AC_panel = ACPanel(self, self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.AC_panel, u"Annotation Corpus", False )
		self.fastSemSim_listbook.SetPageImage(2, 8)

		#### Panel SS
		self.SS_panel = SSPanel(self, self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.SS_panel, u"Semantic Similarity", False )
		self.fastSemSim_listbook.SetPageImage(3, 6)
		#### Panel Query
		self.query_panel = QueryPanel(self, self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.query_panel, u"Query", False )
		self.fastSemSim_listbook.SetPageImage(4, 4)
		#### Panel Output Ctrl
		self.output_ctrl_panel = OutputCtrlPanel(self, self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.fastSemSim_listbook.AddPage( self.output_ctrl_panel, u"Output Settings", False )
		self.fastSemSim_listbook.SetPageImage(5, 5)
		#### Panel Output
		#self.output_window = OutputPanel(self, self.fastSemSim_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		#self.fastSemSim_listbook.AddPage( self.output_window, u"Output", False )
		##self.fastSemSim_listbook.SetPageImage(5, 5)

		self.output_window = OutputWindow(self, wx.DefaultPosition, wx.DefaultSize, 0)
		#self.fastSemSim_listbook.SetPageImage(5, 5)
		
		self.reset()
		self._update()
		self.SetStatus(STATUS_WAIT)
		
#











#############################################################################################
#############################################################################################
#################           PROCESS HANDLING AND COMMUNICATION     ##########################
#############################################################################################
#############################################################################################

	def OnCheckProcessData(self,event):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: OnCheckProcessData()"
		#print "timer elapsed"
		data = event.data
		if data[0] == WorkProcess.CMD_OUTPUT:
			if DEBUG_LEVEL>0:
				print "fastSemSimGui: OnCheckProcessData(). CMD_OUTPUT received"
			#if self.ssprocess2gui_pipe.poll():
				#incoming_data = self.ssprocess2gui_pipe.recv()
			incoming_data = data[1]
			self.OnPipeData(incoming_data)
#


	#def OnCheckPipes(self,event):
		##print "timer elapsed"
		#if self.ssprocess2gui_pipe.poll():
			##print "data!"
			#tmp = self.ssprocess2gui_pipe.recv()
			#self.OnOutputData(tmp)
			#gaugerange = self.progress.GetRange()
			#self.progress.SetValue((float(self.superconta)/self.pairs_to_process)*gaugerange)
			
		#if self.lock(wait = False):
			##print "THIS CHECK"
			#if not self.ssprocess2gui_queue.empty():
				#data = self.ssprocess2gui_queue.get()
				##print data
				#if data[0] == WorkProcess.CMD_STOP:
					#if data[1]:
						#self.completed()
					#else:
						#self.completed()
			#self.unlock()
		#else:
			#pass

##






	def lock(self, wait = True):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: lock()"
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
#










	def unlock(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: unlock()"
		self.process_busy_lock.acquire()
		self.process_busy = False
		self.process_busy_event.clear()
		self.process_busy_event.set()
		self.process_busy_lock.release()
		return True
#







	def _init_communication(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: _init_communication()"
		self.process_busy = False
		self.process_busy_lock = multiprocessing.Lock()
		self.process_busy_event = multiprocessing.Event()
		self.gui2ssprocess_queue = multiprocessing.Queue()
		self.ssprocess2gui_queue = multiprocessing.Queue()
		self.gui2ssprocess_pipe, self.ssprocess2gui_pipe = multiprocessing.Pipe()

		#self.TIMER_ID = 100
		#self.timer = wx.Timer(self, self.TIMER_ID)
		#wx.EVT_TIMER(self, self.TIMER_ID, self.OnCheckProcessData)

		self._init_thread()
#







	def _init_thread(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: _init_thread()"
		self.communication_thread = CommunicationThread(self)
		self.communication_thread.start()
#









	def _init_process(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: _init_process()"
		if not self.running:
			if DEBUG_LEVEL>1:
				print "Starting process"
			self.ssprocess = []
			self.ssprocess.append(None)
			self._init_communication()
			self.ssprocess[0] = WorkProcess.WorkProcess(self.gui2ssprocess_queue, self.ssprocess2gui_queue, self.ssprocess2gui_pipe, self.gui2ssprocess_pipe)
			self.running = True
			self.ssprocess[0].start()
			return True
		else:
			if DEBUG_LEVEL>1:
				print "Process already in execution"
			return False
#







	def _kill_process(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: _kill_process()"

		if not self.ssprocess[0] == None:
			self.ssprocess[0].terminate() # DANGER abruptly terminates computation process. Should not use this
			self.ssprocess[0] = None
		self.running = False

		if not self.communication_thread == None:
			self.lock()
			self.ssprocess2gui_queue.put((-1,))
			self.unlock()
			self.communication_thread.join()
			self.communication_thread = None

		self.gui2ssprocess_queue = None
		self.ssprocess2gui_queue = None
		self.ssprocess2gui_pipe = None
		self.gui2ssprocess_pipe = None

		self.SetStatus(-1)
#






	#def _start_process(self):
		#if DEBUG_LEVEL>0:
			#print "fastSemSimGui: _start_process()"
		##self.progress.SetValue(float(0))
		#if self.status == 1:
			#if DEBUG_LEVEL>1:
				#print "Job already running."
			#return False
		#if self.status == -1:
			#if DEBUG_LEVEL>1:
				#print "Process not initialized."
			#return False

		##self.lock()
		#self.gui2ssprocess_queue.put((WorkProcess.CMD_LOAD_SS, self.param_ss_measure, None, self.param_mixing_strategy, None, self.param_selected_GO))
		##data = self.ssprocess2gui_queue.get()
		#self.gui2ssprocess_queue.put((WorkProcess.CMD_STATUS, None))
		##data = self.ssprocess2gui_queue.get()
		##if self.query_from == WorkProcess.QUERY_FROM_GUI:
			##self.loadFromField()
		#self.start_outcome_handle = self.communication_thread.register_callback(self.start_outcome)
		#self.gui2ssprocess_queue.put((WorkProcess.CMD_START, self.param_query))

		##data = self.ssprocess2gui_queue.get()
		##self.unlock()
		##if data[0] == WorkProcess.CMD_START and data[1]:
			##self.pairs_to_process = data[2]
			##self.SetStatus(1)
		##else:
			##return False
		#return True
##








	def _stop_process(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: _stop_process()"
		#self.lock()
		self.stop_outcome_handle = self.communication_thread.register_callback(self.stop_outcome)
		self.gui2ssprocess_queue.put((WorkProcess.CMD_STOP, None))
		#data = self.ssprocess2gui_queue.get()
		#self.unlock()
#














#############################################################################################
#############################################################################################
#################           LOGIC          ##################################################
#############################################################################################
#############################################################################################



	def reset(self):
		self.start_check_handle = None
	
#





	def OnPipeData(self, t):
		if DEBUG_LEVEL>1:
			print "fastSemSimGui: OnPipeData()"
		#print t
		
		frase = ""
		for i in t: #range(t[0], t[1] + 1):
			##frase = self.ssprocess[0].buffer[i][0] + "\t" + self.ssprocess[0].buffer[i][1] + "\t" + self.ssprocess[0].buffer[i][2] + "\n"
			#self.superconta += 1
			frase += str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n"
			#self.OutputGui.output_field.AppendText(frase)
		self.output_window.output_text.AppendText(frase)
		#frase = ""
		#for i in t: #range(t[0], t[1] + 1):
			#frase = self.ssprocess[0].buffer[i][0] + "\t" + self.ssprocess[0].buffer[i][1] + "\t" + self.ssprocess[0].buffer[i][2] + "\n"
			#self.superconta += 1
			#frase = frase + str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n"
		#self.OutputGui.output_field.AppendText(frase)
		#print "Output data printed"
		#self.OnUpdateDone()
#














	def OnQueueData(self, data):
		if DEBUG_LEVEL>1:
			print "fastSemSimGui: OnQueueData()"
		if data[0] == WorkProcess.CMD_STOP:
			if data[1]:
				def stop(self):
					self.completed()
					self.stop_process()
			else:
				self.SetStatus(1)
				self.completed()
		return True
#








	def SetStatus(self, status):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: SetStatus()"
		prev = self.status
		self.status = status
		if DEBUG_LEVEL>1:
			print "Status switched from " + str(prev) + " to " + str(self.status)
		
		if prev==-1 and not self.status==-1:
			#self.timer.Start(1000)
			pass
		
		#if self.show_pics:
			#if self.status == -1: # Fatal error
				#if not self.start_cmd is None:
					#self.start_cmd.Disable()
					#self.start_cmd.SetLabel("Start")
			#if self.status == 0: # Not running. Not Ready
				#if not self.start_cmd is None:
					#self.start_cmd.Disable()
					#self.start_cmd.SetLabel("Start")
			#if self.status == 1: # Not Running. Ready
				#if not self.start_cmd is None:
					#self.start_cmd.SetLabel("Start")
					#self.start_cmd.Enable()
			#if self.status == 2: # Running. (Completed)
				#if not self.start_cmd is None:
					#self.start_cmd.SetLabel("Stop")
					##self.statuspicture.SetBitmap(wx.Bitmap(self.s0_pic))
					#self.start_cmd.Enable()
#







	def _quit(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: _quit()"
		self._kill_process()
		sys.exit()
#







	def start_outcome(self, event):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: start_outcome()"
		data = event.data
		if data[0] == WorkProcess.CMD_START:
			if data[1] == WorkProcess.ANSWER_PROCESSED:
				if data[2] == WorkProcess. RESULT_OK:
					if DEBUG_LEVEL>0:
						print "start_outcome: Computation start."
					#self.SetStatus(1)
					
				else:
					if DEBUG_LEVEL>0:
						print "start_outcome: Computation not started."
					#self.SetStatus(0)
				self.communication_thread.unregister_callback(self.start_outcome_handle)
				self.communication_thread.unregister_callback(self.start_output_handle)
			elif data[1] == WorkProcess.ANSWER_PROCESSING:
				if DEBUG_LEVEL>0:
					print "start_outcome: Start request is being processed."
			elif data[1] == WorkProcess.ANSWER_IGNORED:
				if DEBUG_LEVEL>0:
					print "start_outcome: Start request ignored."
				self.communication_thread.unregister_callback(self.start_outcome_handle)
				self.communication_thread.unregister_callback(self.start_output_handle)
			else:
				if DEBUG_LEVEL>0:
					print "start_outcome: Unknown answer."
				self.communication_thread.unregister_callback(self.start_outcome_handle)
				self.communication_thread.unregister_callback(self.start_output_handle)
			return True
		return False
#








	def stop_outcome(self, data):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: stop_outcome()"
		if data[0] == WorkProcess.CMD_STOP:
			if data[1] == WorkProcess.ANSWER_PROCESSED:
				if data[2] == WorkProcess. RESULT_OK:
					if debug:
						print "stop_outcome: Computation stopped."
					self.SetStatus(0)
				else:
					if debug:
						print "stop_outcome: Computation not stopped."
					self.SetStatus(1)
				self.communication_thread.unregister_callback(self.stop_outcome_handle)
			elif data[1] == WorkProcess.ANSWER_PROCESSING:
				if debug:
					print "stop_outcome: Stop request is being processed."
			elif data[1] == WorkProcess.ANSWER_IGNORED:
				if debug:
					print "stop_outcome: Stop request ignored."
				self.communication_thread.unregister_callback(self.stop_outcome_handle)
			else:
				if debug:
					print "stop_outcome: Unknown answer."
				self.communication_thread.unregister_callback(self.stop_outcome_handle)
			return True
		return False
#








###################################################################################

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
#








	def completed(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: completed()"
		self.progress.SetValue(self.progress.GetRange())
		self.running = False
		self.log_field.AppendText("Task completed.\n")
		self.SetStatus(1)
#






	def OnStartCheck(self, event):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: OnStartCheck()"
		data = event.data
		if data[0] == WorkProcess.CMD_STATUS:
			if DEBUG_LEVEL>1:
				print "fastSemSimGui: OnStartCheck(). Infos:"
				print str(data)
			self.communication_thread.unregister_callback(self.start_check_handle)
			self.start_check_handle = None

			self.GO_status = data[1]['GO']['ok']
			self.AC_status = data[1]['AC']['ok']
			self.ss_status = data[1]['SS']['ok_params']
			self.query_status = data[1]['query']['ok_params']
			self.output_status = data[1]['output']['ok_params']

			if not self.GO_status:
				self.controls_panel.controls_log_text.AppendText("Check Gene Ontology.\nAborted\n")
				return False
			if not self.AC_status:
				self.controls_panel.controls_log_text.AppendText("Check Annotation Corpus.\nAborted.\n")
				return False
			if not self.query_status:
				self.controls_panel.controls_log_text.AppendText("Check query.\nAborted.\n")
				return False
			if not self.output_status:
				self.controls_panel.controls_log_text.AppendText("Check output parameters.\nAborted.\n")
				return False
			if not self.ss_status:
				self.controls_panel.controls_log_text.AppendText("Check operation parameters.\nAborted.\n")
				return False

			self.controls_panel.controls_log_text.AppendText("Starting computation...\n")
			#self.log_field.AppendText("Evaluating semantic similarity...\n")
			#if self.output_type == 0:
				#self.OutputGui.output_field.Clear()
				#self.OutputGui.Show()
				
				#if self.parentobj.status == 1: # Ready. Not Running
					#self.parentobj.start()
				#elif self.parentobj.status == 2: # running
					#self.parentobj.stop() # set to not running and stops thread
				#elif self.parentobj.status == 0: # Not ready. Should not be active.
					#self.parentobj.activateGoCmd()
			self.start_outcome_handle = self.communication_thread.register_callback(self, self.start_outcome)
			self.start_output_handle = self.communication_thread.register_callback(self, self.OnCheckProcessData)
			self.gui2ssprocess_queue.put((WorkProcess.CMD_START, self.param_query))
			#return self._start_process()
			return True
		return False
#





	def start(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: start()"
		self.controls_panel.controls_log_text.Clear()
		print self.SS_measure
		self.gui2ssprocess_queue.put((WorkProcess.CMD_SET, WorkProcess.CMD_SET_SS, self.SS_measure, None, self.SS_mixing_strategy, None, self.SS_ontology))
		self.gui2ssprocess_queue.put((WorkProcess.CMD_SET, WorkProcess.CMD_SET_OUTPUT, self.output_to, None))
		self.gui2ssprocess_queue.put((WorkProcess.CMD_SET, WorkProcess.CMD_SET_QUERY, self.query_from, None))

		if self.start_check_handle == None:
			self.start_check_handle = self.communication_thread.register_callback(self, self.OnStartCheck)
		self.gui2ssprocess_queue.put((WorkProcess.CMD_STATUS, None))
		
		#data = self.ssprocess2gui_queue.get()
		#if self.query_from == WorkProcess.QUERY_FROM_GUI:
			#self.loadFromField()
#









	def stop(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: stop()"
		return self._stop_process()
#










#############################################################################################
#############################################################################################
#################           GUI EVENTS HANDLERS          ####################################
#############################################################################################
#############################################################################################


	def _update(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: _update()"

		if self.status_handle == None:
			self.status_handle = self.communication_thread.register_callback(self, self.OnProcessInfoUpdate)
		self.gui2ssprocess_queue.put((WorkProcess.CMD_STATUS, None))
#


	def OnProcessInfoUpdate(self, event):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: OnProcessInfoUpdate()"
		data = event.data
		if data[0] == WorkProcess.CMD_STATUS:
			if DEBUG_LEVEL>1:
				print "fastSemSimGui: OnProcessInfoUpdate(). Infos:"
				print str(data)
			self.communication_thread.unregister_callback(self.status_handle)
			self.status_handle = None


			self.GO_status = data[1]['GO']['ok']
			self.AC_status = data[1]['AC']['ok']
			self.ss_status = data[1]['SS']['ok_params']
			self.query_status = data[1]['query']['ok_params']
			self.output_status = data[1]['output']['ok_params']
			
			if self.GO_status:
				self.fastSemSim_listbook.SetPageImage(1, 7)
				self.AC_panel.Enable( True )
			else:
				self.fastSemSim_listbook.SetPageImage(1, 8)
				self.AC_panel.Enable( False )
			if self.AC_status:
				self.fastSemSim_listbook.SetPageImage(2, 7)
			else:
				self.fastSemSim_listbook.SetPageImage(2, 8)
				
			self.controls_panel.SetSSCtrlStatus(self.ss_status)
			self.controls_panel.SetGOStatus(self.GO_status)
			self.controls_panel.SetAcStatus(self.AC_status)
			self.controls_panel.SetQueryStatus(self.query_status)
			self.controls_panel.SetOutputCtrlStatus(self.output_status)
			
			self.GO_panel._update()
			self.AC_panel._update()
			self.SS_panel._update()
			#self.query_panel._update()
			#self.output_window._update()
			#self.controls_panel._update()

			return True
		return False
#





	def OnQuit(self, event):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: OnQuit()"
		self._quit()
#







	def activateGoCmd(self): # should not be called if status is 2
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: activateGoCmd()"
		if self.status == -1:
			return
		if self.debug or (self.GO_status and self.AC_status and self.query_status and self.outputctrl_ok and self.operation_ok):
			self.SetStatus(1) # set to 0
		else:
			self.SetStatus(0)
			
	#def SetStatus(self, status):
		#self.status = status
		#return None ## To remove when complete
		#if self.show_pics:
			#if self.status == -1: # Fatal error
				#if not self.start_cmd is None:
					#self.start_cmd.Disable()
					#self.start_cmd.SetLabel("Start")
			#if self.status == 0: # Not running. Not Ready
				#if not self.start_cmd is None:
					#self.start_cmd.Disable()
					#self.start_cmd.SetLabel("Start")
			#if self.status == 1: # Not Running. Ready
				#if not self.start_cmd is None:
					#self.start_cmd.SetLabel("Start")
					#self.start_cmd.Enable()
			#if self.status == 2: # Running. (Completed)
				#if not self.start_cmd is None:
					#self.start_cmd.SetLabel("Stop")
					##self.statuspicture.SetBitmap(wx.Bitmap(self.s0_pic))
					#self.start_cmd.Enable()
#





	def OnAnyUpdate(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: OnAnyUpdate()"
		#self.statusgridbox.Fit(self)
		#self.gostatsbox.Fit(self)
		#self.commandbox.Fit(self)
		self.mainbox.Fit(self)
		#w,h = self.commandbox.GetSizeTuple()
		#self.mainbox.SetItemMinSize(self.commandbox, w,h)
		#self.GetBestSize()
		self.mainbox.Layout()
		




##----------------------------------------------------------------------------------------------------------------------------------
	##'''
	##Menubar
	##'''
	#def InitMenu(self):
		#self.ID_NEW=wx.NewId()
		#self.ID_OPEN=wx.NewId()
		#self.ID_QUIT=wx.NewId()
		#self.ID_SAVE=wx.NewId()
		#self.ID_SAVE_AS=wx.NewId()
		#self.MenuBar = wx.MenuBar()
		#self.FileMenu = wx.Menu()
		#self.FileMenu.Append(self.ID_NEW, 'New', 'New')
		#self.FileMenu.Append(self.ID_OPEN, 'Open Configuration...', 'Open Configuration')
		#self.FileMenu.Append(self.ID_SAVE, 'Save Configuration', 'Save Configuration')
		#self.FileMenu.Append(self.ID_SAVE_AS, 'Save Configuration As...', 'Save Configuration As')
		#self.FileMenu.Append(self.ID_QUIT, 'Quit', 'Quit application')
		#self.MenuBar.Append(self.FileMenu,'&File')
		#self.SetMenuBar(self.MenuBar)
		#self.Bind(wx.EVT_MENU, self.OnMenuQuit, id=self.ID_QUIT)
		#self.Bind(wx.EVT_MENU, self.OnMenuOpen, id=self.ID_OPEN)
		#self.Bind(wx.EVT_MENU, self.OnMenuSave, id=self.ID_SAVE)
		#self.Bind(wx.EVT_MENU, self.OnMenuSaveAs, id=self.ID_SAVE_AS)
		#self.Bind(wx.EVT_MENU, self.OnMenuNew, id=self.ID_NEW)
		#return True
	
	#def OnMenuNew(self, event):
		#print "OnMenuNew still to be implemented."

	#def OnMenuQuit(self, event):
		#print "OnMenuQuit still to be implemented correctly."
		#sys.exit()

	#def OnMenuOpen(self, event):
		#print "OnMenuOpen still to be implemented."
		#dialog = wx.FileDialog(None, style = wx.OPEN)
		#if dialog.ShowModal() == wx.ID_OK:
			#print 'Loading: ', dialog.GetPath()
			#if not self.config_file == None:
				#self.OnMenuNew(None)
			#self.config_file = dialog.GetPath()
			#self.loadConfigGui = LoadConfigGui(self)

	#def OnMenuSave(self, event):
		#if self.config_file == None:
			#return self.OnMenuSaveAs(event)
		#self.saveConfigGui = SaveConfigGui(self)

	#def OnMenuSaveAs(self, event):
		#dialog = wx.FileDialog(None, style = wx.SAVE|wx.OVERWRITE_PROMPT)
		#if dialog.ShowModal() == wx.ID_OK:
			#self.config_file = dialog.GetPath()
			#self.OnMenuSave(event)
#






# routines to manage flags, status, and variables in general

	def SetGoOk(self, status):
		self.GO_status = status
		if self.show_pics:
			if self.GO_status:
				self.StatusGui.GO_status_pic.SetBitmap(wx.Bitmap(self.Ok_pic))
			else:
				self.StatusGui.GO_status_pic.SetBitmap(wx.Bitmap(self.Warning_pic))
		self.activateGoCmd()
		
	def SetAcOk(self, status):
		self.AC_status = status
		if self.show_pics:
			if self.AC_status:
				self.StatusGui.AC_status_pic.SetBitmap(wx.Bitmap(self.Ok_pic))
			else:
				self.StatusGui.AC_status_pic.SetBitmap(wx.Bitmap(self.Warning_pic))
		self.activateGoCmd()
		
	def SetQueryOk(self, status):
		self.query_status = status
		if self.show_pics:
			if self.query_status:
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
#





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


	def OnLogData(self, msg):
		t = msg.data
		self.log_field.AppendText(t)
		#self.OnUpdateDone()
#









	def OnUpdateDone(self):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: OnUpdateDone()"
		pass
		#print "Update done"
		#self.update_event.set()
#






	def OnDefaultAction(self, event):
		if DEBUG_LEVEL>0:
			print "fastSemSimGui: OnDefaultAction()"
#



##################################################################################################################
##################################################################################################################
#################           END fastSemSimGui class                         ######################################
##################################################################################################################
##################################################################################################################
#----------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#
##################################################################################################################
##################################################################################################################
#################          COMMUNICATION CLASS - THREAD                    #######################################
##################################################################################################################
##################################################################################################################






class CommunicationThread(threading.Thread):
	def __init__(self, gui):
		threading.Thread.__init__ ( self)
		if DEBUG_LEVEL>0:
			print "CommunicationThread: init()"
		self.gui = gui
		self.uc = 0
		self.callbacks = {}
		self.lock = multiprocessing.Lock()
		#self.register_callback(self.gui, self.gui.OnDefaultAction)
#




	def _lock(self):
		self.lock.acquire()
#





	def _unlock(self):
		self.lock.release()
#





	def run(self):
		if DEBUG_LEVEL>0:
			print "CommunicationThread: run(). (Should appear once.)"
		while True:
			data = self.gui.ssprocess2gui_queue.get(True)
			if DEBUG_LEVEL>1:
				print "CommunicationThread: run(). message received from computation process"
			if data[0]==-1:
				return
			#processed = False
			# Way 2 - Use Events. Cannot establish here if event has been processed
			self._lock()
			current_callbacks = copy.copy(self.callbacks)
			for i in current_callbacks:
				print wx.PostEvent(current_callbacks[i][0].GetEventHandler(), DataEvent(data=data))
			self._unlock()
#





	def register_callback(self, who, func):
		if DEBUG_LEVEL>1:
			print "CommunicationThread: register_callback()"
		
		self._lock()
		print who.Bind(EVT_DATA, func)
		self.callbacks[self.uc] = (who, func)
		self.uc += 1
		self._unlock()
		return self.uc - 1
#





	def unregister_callback(self, func_id):
		if func_id not in self.callbacks:
			if DEBUG_LEVEL>1:
				print "CommunicationThread: unregister_callback() error"
		else:
			self._lock()
			self.gui.Unbind(EVT_DATA, self.callbacks[func_id][0], self.callbacks[func_id][1])
			del self.callbacks[func_id]
			self._unlock()
#
##################################################################################
##################################################################################
##################################################################################










##################################################################################
#### start the main gui. Should be called from outside. Why? ####
##################################################################################

DataEvent, EVT_DATA = wx.lib.newevent.NewEvent()

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
