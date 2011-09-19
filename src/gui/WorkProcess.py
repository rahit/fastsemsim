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
from GO import AnnotationCorpus

STATUS_BASE = 0
STATUS_INIT = STATUS_BASE + 0
STATUS_WAIT = STATUS_BASE + 1
STATUS_RUN = STATUS_BASE + 2
STATUS_PAUSE = STATUS_BASE + 3
STATUS_LOAD_GO = STATUS_BASE + 4
STATUS_LOAD_AC = STATUS_BASE + 5
STATUS_LOAD_SS = STATUS_BASE + 6
STATUS_LOAD_QUERY = STATUS_BASE + 7
STATUS_LOAD_OUTPUT = STATUS_BASE + 8

CMD_BASE = 100
CMD_NONE = CMD_BASE
CMD_START = CMD_BASE + 1
CMD_STOP = CMD_BASE + 2
CMD_PAUSE = CMD_BASE + 3
CMD_RESET = CMD_BASE + 4
CMD_STATUS = CMD_BASE + 5
CMD_LOAD_AC = CMD_BASE + 6
CMD_LOAD_GO = CMD_BASE + 7
CMD_LOAD_QUERY = CMD_BASE + 8
CMD_LOAD_SS = CMD_BASE + 9
CMD_LOAD_OUTPUT = CMD_BASE + 10
CMD_DESTROY =  CMD_BASE + 11

OUTPUT2GUI = 0
OUTPUT2FILE = 1

class WorkProcess(multiprocessing.Process):
	status = STATUS_INIT

	def __init__(self, gui2ssprocess_queue, ssprocess2gui_queue, gui2ssprocess_pipe, ssprocess2gui_pipe):
		multiprocessing.Process.__init__(self)
		self.ssprocess2gui_queue = ssprocess2gui_queue
		self.gui2ssprocess_queue = gui2ssprocess_queue
		self.gui2ssprocess_pipe = gui2ssprocess_pipe
		self.ssprocess2gui_pipe = ssprocess2gui_pipe

	def run(self):
		while self.control():
			pass
		return 0

	def control(self):
		if self.status == STATUS_RUN:
			print "check in status RUN"
			#if not self.gui2ssprocess_queue.empty(): #way 1
				#data = self.gui2ssprocess_queue.get(False)
			try: #way 2
				data = self.gui2ssprocess_queue.get(False)
				# check if data is stop or pause. In this case make actions. Otherwise don't do anything
				if data[0] == CMD_STOP:
					self.stop()
				elif data[0] == CMD_PAUSE:
					self.pause()
				elif data[0] == CMD_RESET:
					self.reset()
				elif data[0] == CMD_STATUS:
					self.status()
				else:
					pass # ignore any other command!
			except Exception:
				pass
		elif self.status == STATUS_PAUSE:
			print "check in status PAUSE"
			data = self.gui2ssprocess_queue.get()
			if data[0] == CMD_STOP:
				self.stop()
			elif data[0] == CMD_RESET:
				self.reset()
			elif data[0] == CMD_STATUS:
				self._status()
			elif data[0] == CMD_START:
				self._start(data[1:len(data)])
			else:
				pass # ignore any other command!
		elif self.status == STATUS_INIT:
			print "check in status INIT"
			self.reset()
		elif self.status == STATUS_WAIT:
			print "check in status WAIT"
			data = self.gui2ssprocess_queue.get()
			print str(data)
			if data[0] == CMD_STOP or data[0] == CMD_PAUSE:
				pass
			elif data[0] == CMD_RESET:
				self.reset()
			elif data[0] == CMD_LOAD_GO:
				self.load_GO(data[1:len(data)])
			elif data[0] == CMD_LOAD_AC:
				self.load_AC(data[1:len(data)])
			elif data[0] == CMD_LOAD_QUERY:
				self.load_query(data[1:len(data)])
			elif data[0] == CMD_LOAD_OUTPUT:
				self.load_output(data[1:len(data)])
			elif data[0] == CMD_LOAD_SS:
				self.load_SS(data[1:len(data)])
			elif data[0] == CMD_START:
				self._start(data[1:len(data)])
			elif data[0] == CMD_STATUS:
				self._status()
			elif data[0] == CMD_NONE:
				pass
			else:
				pass
		else:
			print "check in other status."
			# something went wrong. Inconsistent state. Reset!
			self.reset()
		return True

	def reset(self):
		print "func reset"
		self.ss_ok = False
		self.ac_ok = False
		self.go_ok = False
		self.query_ok = False
		self.output_ok = False
		self.go = None
		self.ac = None
		self.query = None
		self.ss = None
		self.output = None
		self.results = None
		# reinitialize structures
		self.status = STATUS_WAIT

	def stop(self):
		print "func stop"
		self.results = None
		# clear data
		self.status = STATUS_WAIT

	def pause(self):
		print "func pause"
		# do not clear data
		self.status = STATUS_PAUSE
		
	def _status(self):
		print "func status"
		
	def _start(self, data):
		self.status = STATUS_RUN
		print "func start"

	def load_AC(self, data): #### data format: (filename, other) other = (file format, file format params)
		self.status = STATUS_LOAD_AC
		print "func Load AC"
		self.ac_ok = False
		#self.query_ok = False
		try:
			self.ac = AnnotationCorpus.AnnotationCorpus(self.go) #### what if go is missing?
			self.ac_filename = data[0]
			self.ac_filetype = data[1]
			self.ac_filetypeparams = data[2]
			if self.ac.parse(str(self.ac_filename), self.ac_filetype, self.ac_filetypeparams):
				if self.ac.sanitize():
					self.ac_ok = True
					#self.parentobj.update_ac = False
		except:
			print("Failed to load Annotation Corpus.")
		self.status = STATUS_WAIT

	def load_GO(self, data): #### data format: (filename)
		self.status = STATUS_LOAD_GO
		print "func Load GO"
		self.go_ok = False
		#self.parentobj.update_ac = True
		#self.parentobj.update_ssobject = True
		if len(data[0]) == 0:
			return
		self.go_filename = data[0]
		self.go = GeneOntology.load_GO_XML(open(self.go_filename,'r'))
		if not self.go == None:
			self.go_ok = True
		self.status = STATUS_WAIT

	def load_query(self, data): #### data format: (query from, query_params) query_params: none (fom ac), filename (from file), data (from gui)
		self.status = STATUS_LOAD_QUERY
		print "func Load query"
		self.status = STATUS_WAIT

	def load_SS(self, data): #### data format: (ss measure, ss measure params, mixing strat., mixing strat. params, ontology)
		self.status = STATUS_LOAD_SS
		print "func Load SS"
		self.ss_ok = False
		self.ss_name = data[0]
		self.ss_params = data[1]
		self.ms_name = data[2]
		self.ms_params = data[3]
		self.ss_ontology = data[4]
		self.ss = False
		self.ss_ok = True
		self.status = STATUS_WAIT

	def load_output(self, data): #### data format: (output_to, output_params) output_params: for file: (filename, type, params), for gui: (how many scores)
		self.status = STATUS_LOAD_OUTPUT
		print "func Load output"
		self.output_ok = False
		self.output_to = data[0]
		if self.output_to == OUTPUT2FILE:
			self.output_filename = data[1]
			self.output_filetype = data[2]
			self.output_filetypeparams = data[3]
		elif  self.output_to == OUTPUT2GUI:
			self.output_filename = None
			self.output_params = data[1]
		self.output_ok = True
		self.status = STATUS_WAIT


	#def buildSSobject(self):
		#ssu = SemSimUtils.SemSimUtils(self.ac, self.go)
		#ssu.det_offspring_table()
		#ssu.det_ancestors_table()
		#ssu.det_freq_table()
		#ssu.det_GO_division()
		#ssu.det_ICs_table()
		#self.ssobject = ObjSemSim.ObjSemSim(self.ac, self.go, self.ssmeasure, self.mixingstrategy, ssu)
		##print "ssmeasure: " + str(self.ssmeasure)
		##print "mixing: " + str(self.mixingstrategy)
		##print "real ss: " + str(self.ssobject.TSS)
		##print "real mixing: " + str(self.ssobject.mixSS)
		#return True
	

	##def run(self):
		##while True:
			##self.gui2ssprocess_commands_queue.get()
	#def set_completed(self):
		#self.sscompleted.value = 1

	
	#def parse_data(self):
		#'''
		#0 self.go, 
		#1 self.ac, 
		#2 self.ssmeasure, 
		#3 self.mixingstrategy, 
		#4 self.ssobject, 
		#5 self.query, 
		#6 self.query_type, 
		#7 self.selectedGO, 
		#8 self.output_type, 
		#9 self.output_file
		#'''
		#data = self.gui2ssprocess_queue.get()
		#self.go = data[0]
		#self.ac = data[1]
		#self.ssmeasure = data[2]
		#self.mixingstrategy = data[3]
		#self.query = data[5]
		#self.query_type = data[6]
		#self.selectedGO = data[7]
		#self.output_type = data[8]
		#self.output_file = data[9]
		##print "query: " + str(self.query)
		##self.ssobject = self.original_ssobject
		##print "AC:" + str(self.ac.annotations)
		##print "GO nodes: " + str(self.go.node_num())
		##print "GO edges: " + str(self.go.edge_num())
		##print "AC nodes: " + str(len(self.ac.annotations))
		##print "AC terms: " + str(len(self.ac.reverse_annotations))
		##print "query nodes: " + str(len(self.query))
		#if not self.use_main_ss_object:
			#self.buildSSobject()
		#else:
			#self.ssobject = data[4]
		#return True

	#def init_structures(self):
		#self.buffer = None # data will be stored here
		#if self.output_type==1:
			#self.output_file_handle = open(self.output_file, 'w')
		#self.counter = 0
		#self.last_percentual = -1
		#self.last_sent = -1
		#self.last_added = -1
		#if self.query_type == 1: # list
			#self.total_number = len(self.query) * (len(self.query)-1) / 2
		#elif self.query_type == 0: # pairs
			#self.total_number = len(self.query)
		#if self.output_type==0:
			#if self.store_all:
				#self.buffer_size = self.total_number
			#else:
				#self.buffer_size = self.MAX_CACHE_SIZE
			#self.buffer = [None]*self.buffer_size
			##self.buffer = [(None, None, None)]*self.buffer_size
		#self.sstodo.value = self.total_number
		#return True

	#def flush_data(self):
		#if self.output_type == 0:
			#self.flushOutput()
		#if self.output_type==1:
			#self.output_file_handle.close()
		#return True

	#def abort(self):
		#self.set_completed()
		#return True

	#def run(self):
		#if not self.parse_data():
			#return self.abort()
		#if not self.init_structures():
			#return self.abort()
		#print "Total pairs to process: " + str(self.total_number)
		#if self.query_type == 1: # list
			#for i in range(0,len(self.query)):
				#for j in range(i+1, len(self.query)):
					#test = self.ssobject.SemSim(self.query[i],self.query[j], self.selectedGO)
					#self.counter += 1
					#if not int(self.counter*100/self.total_number) == self.last_percentual:
						#self.last_percentual = int(self.counter*100/self.total_number)
						#self.sspdone.value = float(self.counter)/self.total_number
					#if type(test) is float:
						#test = str('%.4f' %test)
					#if self.output_type == 0:
						##if not test == None:
						#self.sendOutput(str(self.query[i]), str(self.query[j]), str(test))
					#else:
						#self.writeOutput(str(self.query[i]), str(self.query[j]), str(test))


		#elif self.query_type == 0: # pairs
			#for i in self.query:
				#test = self.ssobject.SemSim(i[0],i[1], self.selectedGO)
				#self.counter += 1
				#if not int(self.counter*100/self.total_number) == self.last_percentual:
					#self.last_percentual = int(self.counter*100/self.total_number)
					#self.sspdone.value = float(self.counter)/self.total_number
				#if type(test) is float:
					#test = str('%.4f' %test)
				#if self.output_type == 0:
					#self.sendOutput(str(i[0]), str(i[1]), str(test))
				#else:
					#self.writeOutput(str(i[0]), str(i[1]), str(test))
		#if not self.flush_data():
			#return self.abort()
		#if not self.counter == self.total_number:
			#print "Count error. Total pairs to process: " + str(self.total_number) + ". Total pairs processed: " + str(self.counter)
			#return self.abort()
		#return self.set_completed()

	#def sendOutput(self, a, b, c):
		#if self.store_all:
			#self.last_added += 1
			#self.buffer[self.last_added] = ((str(a),str(b),str(c)))
			#if self.last_added - (self.last_sent + 1) > self.MAX_CACHE_SIZE:
				#self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added+1])
				#self.last_sent = self.last_added
		#else:
			#self.last_added += 1
			#if self.last_added == self.buffer_size:
				#self.ssprocess2gui_pipe.send(self.buffer[0: self.last_added])
				#self.last_added = -1
			#self.buffer[self.last_added] = ((str(a),str(b),str(c)))

	#def flushOutput(self):
		#if self.store_all:
			#if self.last_sent == self.last_added:
				#return
			#self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added+1])
			#self.last_sent = self.last_added
		#else:
			#if self.last_added == -1:
				#return
			#self.ssprocess2gui_pipe.send(self.buffer[0: self.last_added+1])
			#self.last_added = -1

	#def writeOutput(self, a, b, c):
		#self.output_file_handle.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\n")
		#return True
	
