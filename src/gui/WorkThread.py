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

import wx
import threading
import time 


# events
EVT_PROGRESS_ID = wx.NewId()
EVT_COMPLETED_ID = wx.NewId()
EVT_OUTPUTDATA_ID = wx.NewId()
EVT_LOGDATA_ID = wx.NewId()

class ProgressEvent(wx.PyEvent):
	def __init__(self, data):
		wx.PyEvent.__init__(self)
		self.SetEventType(EVT_PROGRESS_ID)
		self.data = data

class CompletedEvent(wx.PyEvent):
	def __init__(self, data):
		wx.PyEvent.__init__(self)
		self.SetEventType(EVT_COMPLETED_ID)
		self.data = data

class OutputDataEvent(wx.PyEvent):
	def __init__(self, data):
		wx.PyEvent.__init__(self)
		self.SetEventType(EVT_OUTPUTDATA_ID)
		self.data = data

class LogDataEvent(wx.PyEvent):
	def __init__(self, data):
		wx.PyEvent.__init__(self)
		self.SetEventType(EVT_LOGDATA_ID)
		self.data = data

# Thread

class WorkThread(threading.Thread):

	def __init__(self, gui):
		threading.Thread.__init__(self)
		self.gui = gui
		self.output_type = self.gui.output_type
		self.output_file = self.gui.output_file
		self.query_type = self.gui.query_type 
		self.query = self.gui.query
		self.ssobject = self.gui.ssobject
		self.selectedGO = self.gui.selectedGO

	def run(self):
		total_number = 9
		for i in range(1,total_number + 1):
			time.sleep(1)
			wx.PostEvent(self.gui, OutputDataEvent(str(i)))
			wx.PostEvent(self.gui, LogDataEvent(str(i)))
		return

	def sendOutput(self, a, b, c):
		#self.gui.OutputGui.output_field.AppendText("Preview text. Complete output can be found here: "+str(self.gui.output_file)+".\n")
		self.buffer = self.buffer + str(a) + "\t" + str(b) + "\t" + str(c) + "\n"
		if len(self.buffer) > 1000:
			wx.PostEvent(self.gui, OutputDataEvent(self.buffer))
			self.buffer = ""
		#wx.PostEvent(self.gui, LogDataEvent(str(i)))

	def writeOutput(self, a, b, c):
		self.output_file_handle.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\n")
		return True
	
	def run(self):
		self.buffer = ""
		if self.output_type==1:
			self.output_file_handle = open(self.output_file, 'w')
		counter = 0
		last_percentual = -1
		if self.query_type == 1: # list
			self.total_number = len(self.query) * (len(self.query)-1) / 2
			for i in range(0,len(self.query)):
				for j in range(i+1, len(self.query)):
					test = self.ssobject.SemSim(self.query[i],self.query[j], self.selectedGO)
					counter += 1
					if not int(counter*100/self.total_number) == last_percentual:
						last_percentual = int(counter*100/self.total_number)
						wx.PostEvent(self.gui, ProgressEvent(float(counter)/self.total_number))
					if type(test) is float:
						test = str('%.4f' %test)
					if self.output_type == 0:
						self.sendOutput(str(self.query[i]), str(self.query[j]), str(test))
					else:
						self.writeOutput(str(self.query[i]), str(self.query[j]), str(test))
						self.sendOutput(str(self.query[i]), str(self.query[j]), str(test))
		elif self.query_type == 0: # pairs
			self.total_number = len(self.query)
			for i in self.query:
				test = self.ssobject.SemSim(i[0],i[1], self.selectedGO)
				counter += 1
				if not int(counter*100/self.total_number) == last_percentual:
					last_percentual = int(counter*100/self.total_number)
					wx.PostEvent(self.gui, ProgressEvent(float(counter)/self.total_number))
				if self.output_type == 0:
					self.sendOutput(str(i[0]), str(i[1]), str(test))
				else:
					self.writeOutput(str(i[0]), str(i[1]), str(test))
					self.sendOutput(str(i[0]), str(i[1]), str(test))
		if self.output_type==1:
			self.output_file_handle.close()
		wx.PostEvent(self.gui, CompletedEvent("Completed"))
		return True