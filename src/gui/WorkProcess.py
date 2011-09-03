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

import multiprocessing
import time 
import copy
from SemSim import SemSimMeasures
from SemSim import ObjSemSim
from SemSim import SemSimUtils

#def f(n, a):
    #n.value = 3.1415927
    #for i in range(len(a)):
        #a[i] = -a[i]

class WorkProcess(multiprocessing.Process):
	
	#interprocess communication data
	gui2ssprocess_commands_queue = None
	MAX_CACHE_SIZE = 5000
	KEEP_MODE = True

	#def __init__(self, gui2ssprocess_commands_queue):
	def __init__(self, gui2ssprocess_queue, gui2ssprocess_pipe, ssprocess2gui_pipe, sspdone, sstodo):
		multiprocessing.Process.__init__(self)
		#self.gui2ssprocess_commands_queue = gui2ssprocess_commands_queue
		self.gui2ssprocess_queue = gui2ssprocess_queue
		self.gui2ssprocess_pipe = gui2ssprocess_pipe
		self.ssprocess2gui_pipe = ssprocess2gui_pipe
		self.sspdone = sspdone
		self.sstodo = sstodo

	def buildSSobject(self):
		ssu = SemSimUtils.SemSimUtils(self.ac, self.go)
		ssu.det_offspring_table()
		ssu.det_ancestors_table()
		ssu.det_freq_table()
		ssu.det_GO_division()
		ssu.det_ICs_table()
		print ssu.IC
		self.ssobject = ObjSemSim.ObjSemSim(self.ac, self.go, self.ssmeasure, self.mixingstrategy, ssu)
		print "ssmeasure: " + str(self.ssmeasure)
		print "mixing: " + str(self.mixingstrategy)
		print "real ss: " + str(self.ssobject.TSS)
		print "real mixing: " + str(self.ssobject.mixSS)
		return True
	
	#def run(self):
		#while True:
			#self.gui2ssprocess_commands_queue.get()
		
	def run(self):
		'''
		0 self.go, 
		1 self.ac, 
		2 self.ssmeasure, 
		3 self.mixingstrategy, 
		4 self.ssobject, 
		5 self.query, 
		6 self.query_type, 
		7 self.selectedGO, 
		8 self.output_type, 
		9 self.output_file
		'''
		data = self.gui2ssprocess_queue.get()
		self.go = data[0]
		self.ac = data[1]
		self.ssmeasure = data[2]
		self.mixingstrategy = data[3]
		self.ssobject = data[4]
		self.query = data[5]
		self.query_type = data[6]
		self.selectedGO = data[7]
		self.output_type = data[8]
		self.output_file = data[9]
		self.buildSSobject()
		#print "AC:" + str(self.ac.annotations)
		#print "GO nodes: " + str(self.go.node_num())
		#print "GO edges: " + str(self.go.edge_num())
		#print "AC nodes: " + str(len(self.ac.annotations))
		#print "AC terms: " + str(len(self.ac.reverse_annotations))
		#print "query nodes: " + str(len(self.query))
		self.buffer = None # data will be stored here
		if self.output_type==1:
			self.output_file_handle = open(self.output_file, 'w')
		counter = 0
		last_percentual = -1
		self.last_sent = -1
		self.last_added = -1
		if self.query_type == 1: # list
			self.total_number = len(self.query) * (len(self.query)-1) / 2
			self.sstodo = self.total_number
			if self.output_type==0:
				#self.buffer = [(None, None, None)]*self.total_number
				self.buffer = [None]*self.total_number
			for i in range(0,len(self.query)):
				for j in range(i+1, len(self.query)):
					#print self.selectedGO
					test = self.ssobject.SemSim(self.query[i],self.query[j], self.selectedGO)
					counter += 1
					if not int(counter*100/self.total_number) == last_percentual:
						last_percentual = int(counter*100/self.total_number)
						self.sspdone.value = float(counter)/self.total_number
						#wx.PostEvent(self.gui, ProgressEvent(float(counter)/self.total_number))
						#self.gui.update_event.wait()
						#self.gui.update_event.clear()
					if type(test) is float:
						pass
						#test = str('%.4f' %test)
					if self.output_type == 0:
						#if not test == None:
						#print str((str(self.query[i]), str(self.query[j]), str(test)))
						self.sendOutput(str(self.query[i]), str(self.query[j]), str(test))
					else:
						pass
						#self.writeOutput(str(self.query[i]), str(self.query[j]), str(test))
			if self.output_type == 0:
				self.flushOutput()
		elif self.query_type == 0: # pairs
			self.total_number = len(self.query)
			self.sstodo = self.total_number
			if self.output_type==0:
				#self.buffer = [(None, None, None)]*self.total_number
				self.buffer = [None]*self.total_number
			for i in self.query:
				test = self.ssobject.SemSim(i[0],i[1], self.selectedGO)
				counter += 1
				if not int(counter*100/self.total_number) == last_percentual:
					last_percentual = int(counter*100/self.total_number)
					self.sspdone.value = float(counter)/self.total_number
					#wx.PostEvent(self.gui, ProgressEvent(float(counter)/self.total_number))
				if self.output_type == 0:
					pass
					#self.sendOutput(str(i[0]), str(i[1]), str(test))
				else:
					pass
					#self.writeOutput(str(i[0]), str(i[1]), str(test))
			if self.output_type == 0:
				self.flushOutput()
		if self.output_type==1:
			self.output_file_handle.close()
		#wx.PostEvent(self.gui, CompletedEvent("Completed"))
		return True
		

	def sendOutput(self, a, b, c):
		#if self.KEEP_MODE:
		self.last_added += 1
		self.buffer[self.last_added] = ((str(a),str(b),str(c)))
		if self.last_added - (self.last_sent + 1) > self.MAX_CACHE_SIZE:
			self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added])
			#print "Before waiting in post event"
			#self.gui.update_event.wait()
			#self.gui.update_event.clear()
			#print "after waiting in post event"
			self.last_sent = self.last_added

	def flushOutput(self):
		if self.last_sent == self.last_added:
			return
		self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added])
		self.last_sent = self.last_added

	def writeOutput(self, a, b, c):
		self.output_file_handle.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\n")
		return True
	
