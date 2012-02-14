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
import multiprocessing


class fastSemSimGui(wx.Frame):
	
#
	def __init__(self, parent):
		super(fastSemSimGui, self).__init__(parent, title="fastSemSim - Copyright 2011, Marco Mina - beta version", style = wx.RESIZE_BORDER | wx.DEFAULT_FRAME_STYLE)
		self.process_busy = False
		self.process_busy_lock = multiprocessing.Lock()
		self.process_busy_event = multiprocessing.Event()
		
		self.programdirectory = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
		self.Ok_pic = self.programdirectory + '/V_30.png'
		self.Warning_pic = self.programdirectory + '/W_30.png'
		self.Advanced_pic = self.programdirectory + '/advanced.png'
	
		self.GOGui = GeneOntologyGui(self)

	def InitWorkProcess(self):
		self.running = False
		self.ssprocess.append(None)
		
		self.TIMER_ID = 100
		self.timer = wx.Timer(self.panel, self.TIMER_ID)
		wx.EVT_TIMER(self.panel, self.TIMER_ID, self.OnCheckPipes)
   
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
#


def go():
	app = wx.App()
	window = fastSemSimGui(None)
	window.Centre()
	window.Show()  
	app.MainLoop()


if __name__ == "__main__":
	multiprocessing.freeze_support()
	go()