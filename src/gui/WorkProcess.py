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
from GO import GeneOntology

class WorkProcess(multiprocessing.Process):
	store_all = False
	use_main_ss_object = True
	#interprocess communication data
	gui2ssprocess_commands_queue = None
	MAX_CACHE_SIZE = 5000
	KEEP_MODE = True


	def __init__(self, gui2ssprocess_queue, ssprocess2gui_queue, in_pipe, out_pipe):
		multiprocessing.Process.__init__(self)
		self.gui2ssprocess_queue = gui2ssprocess_queue
		self.ssprocess2gui_queue = ssprocess2gui_queue
		self.in_pipe = in_pipe
		self.out_pipe = out_pipe
		self.reset()
		self.commands = {
			'reset':self.reset,
			'init':self.initialize,
			'run':self.calculate,
			'go':self.go,
			'ac':self.ac,
			'query':self.query,
			'outputctrl':self.outputctrl,
			'ss':self.ss,
			'abort':self.abort
			}

	def run(self):
		while True:
			data = self.gui2ssprocess_queue.get() # every packet should be in the form ('command', params)
			print "Received " + str(data)
			if data in self.commands:
				self.commands[data]()
			#elif data[0] in self.commands:
				#self.commands[data[0]](data)
		return True

	def reset(self):
		print "Reset"
		#self.in_pipe.flush()
		#self.out_pipe.flush()
		return True

	def initialize(self):
		print "Initialization..."
		return True

	def calculate(self):
		pass
	def go(self):
		print "Go"
		if not self.in_pipe.poll():
			return False
		data = self.in_pipe.recv()
		print type(data)
		if type(data) is str:
			self.go_filename = data
		elif type(data) is list or type(data) is tuple:
			self.go_filename = data[0]
		self.go = GeneOntology.load_GO_XML(open(self.go_filename,'r'))
		if not self.go == None:
			self.go_ok = True
			self.out_pipe.send(('go', 'ok'))
		else:
			self.go_ok = False
			self.out_pipe.send(('go', 'fail'))
		pass
	def ac(self):
		pass
	def query(self):
		pass
	def outputctrl(self):
		pass
	def ss(self):
		pass
	def abort(self):
		pass
	
	def buildSSobject(self):
		ssu = SemSimUtils.SemSimUtils(self.ac, self.go)
		ssu.det_offspring_table()
		ssu.det_ancestors_table()
		ssu.det_freq_table()
		ssu.det_GO_division()
		ssu.det_ICs_table()
		self.ssobject = ObjSemSim.ObjSemSim(self.ac, self.go, self.ssmeasure, self.mixingstrategy, ssu)
		#print "ssmeasure: " + str(self.ssmeasure)
		#print "mixing: " + str(self.mixingstrategy)
		#print "real ss: " + str(self.ssobject.TSS)
		#print "real mixing: " + str(self.ssobject.mixSS)
		return True
	

	def set_completed(self):
		self.sscompleted.value = 1
	
	def parse_data(self):
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
		self.query = data[5]
		self.query_type = data[6]
		self.selectedGO = data[7]
		self.output_type = data[8]
		self.output_file = data[9]
		#print "query: " + str(self.query)
		#self.ssobject = self.original_ssobject
		#print "AC:" + str(self.ac.annotations)
		#print "GO nodes: " + str(self.go.node_num())
		#print "GO edges: " + str(self.go.edge_num())
		#print "AC nodes: " + str(len(self.ac.annotations))
		#print "AC terms: " + str(len(self.ac.reverse_annotations))
		#print "query nodes: " + str(len(self.query))
		if not self.use_main_ss_object:
			self.buildSSobject()
		else:
			self.ssobject = data[4]
		return True

	def init_structures(self):
		self.buffer = None # data will be stored here
		if self.output_type==1:
			self.output_file_handle = open(self.output_file, 'w')
		self.counter = 0
		self.last_percentual = -1
		self.last_sent = -1
		self.last_added = -1
		if self.query_type == 1: # list
			self.total_number = len(self.query) * (len(self.query)-1) / 2
		elif self.query_type == 0: # pairs
			self.total_number = len(self.query)
		if self.output_type==0:
			if self.store_all:
				self.buffer_size = self.total_number
			else:
				self.buffer_size = self.MAX_CACHE_SIZE
			self.buffer = [None]*self.buffer_size
			#self.buffer = [(None, None, None)]*self.buffer_size
		self.sstodo.value = self.total_number
		return True

	def flush_data(self):
		if self.output_type == 0:
			self.flushOutput()
		if self.output_type==1:
			self.output_file_handle.close()
		return True

	def abort(self):
		self.set_completed()
		return True

	def orun(self):
		if not self.parse_data():
			return self.abort()
		if not self.init_structures():
			return self.abort()
		print "Total pairs to process: " + str(self.total_number)
		if self.query_type == 1: # list
			for i in range(0,len(self.query)):
				for j in range(i+1, len(self.query)):
					test = self.ssobject.SemSim(self.query[i],self.query[j], self.selectedGO)
					self.counter += 1
					if not int(self.counter*100/self.total_number) == self.last_percentual:
						self.last_percentual = int(self.counter*100/self.total_number)
						self.sspdone.value = float(self.counter)/self.total_number
					if type(test) is float:
						test = str('%.4f' %test)
					if self.output_type == 0:
						#if not test == None:
						self.sendOutput(str(self.query[i]), str(self.query[j]), str(test))
					else:
						self.writeOutput(str(self.query[i]), str(self.query[j]), str(test))

		elif self.query_type == 0: # pairs
			for i in self.query:
				test = self.ssobject.SemSim(i[0],i[1], self.selectedGO)
				self.counter += 1
				if not int(self.counter*100/self.total_number) == self.last_percentual:
					self.last_percentual = int(self.counter*100/self.total_number)
					self.sspdone.value = float(self.counter)/self.total_number
				if type(test) is float:
					test = str('%.4f' %test)
				if self.output_type == 0:
					self.sendOutput(str(i[0]), str(i[1]), str(test))
				else:
					self.writeOutput(str(i[0]), str(i[1]), str(test))
		if not self.flush_data():
			return self.abort()
		if not self.counter == self.total_number:
			print "Count error. Total pairs to process: " + str(self.total_number) + ". Total pairs processed: " + str(self.counter)
			return self.abort()
		return self.set_completed()

	def sendOutput(self, a, b, c):
		if self.store_all:
			self.last_added += 1
			self.buffer[self.last_added] = ((str(a),str(b),str(c)))
			if self.last_added - (self.last_sent + 1) > self.MAX_CACHE_SIZE:
				self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added+1])
				self.last_sent = self.last_added
		else:
			self.last_added += 1
			if self.last_added == self.buffer_size:
				self.ssprocess2gui_pipe.send(self.buffer[0: self.last_added])
				self.last_added = -1
			self.buffer[self.last_added] = ((str(a),str(b),str(c)))

	def flushOutput(self):
		if self.store_all:
			if self.last_sent == self.last_added:
				return
			self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added+1])
			self.last_sent = self.last_added
		else:
			if self.last_added == -1:
				return
			self.ssprocess2gui_pipe.send(self.buffer[0: self.last_added+1])
			self.last_added = -1

	def writeOutput(self, a, b, c):
		self.output_file_handle.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\n")
		return True
	
