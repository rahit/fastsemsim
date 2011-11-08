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
import os
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

LOAD_AC_BASE = 200 
LOAD_AC_END = LOAD_AC_BASE + 1
LOAD_AC_STATUS = LOAD_AC_BASE + 2

LOAD_GO_BASE = 300 
LOAD_GO_END = LOAD_GO_BASE + 1
LOAD_GO_STATUS = LOAD_GO_BASE + 2


OUTPUT2GUI = 0
OUTPUT2FILE = 1
QUERYFROMGUI = 0
QUERYFROMAC = 2
QUERYFROMFILE = 1

QUERY_PAIRS = 0
QUERY_LIST = 1

class WorkProcess(multiprocessing.Process):
	status = STATUS_INIT
	MAX_BUFFER_SIZE = 5000
	CHECK_INTERVAL = 5000
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
					print "Stop received"
					self.stop()
					return False
				elif data[0] == CMD_PAUSE:
					self.pause()
					return True
				elif data[0] == CMD_RESET:
					self.reset()
					return False
				elif data[0] == CMD_STATUS:
					self._status()
				else:
					pass # ignore any other command!
			except Exception:
				pass
			return True
		elif self.status == STATUS_PAUSE:
			#print "check in status PAUSE"
			data = self.gui2ssprocess_queue.get()
			if data[0] == CMD_STOP:
				self.stop()
				return False
			elif data[0] == CMD_RESET:
				self.reset()
				return False
			elif data[0] == CMD_STATUS:
				self._status()
			elif data[0] == CMD_START:
				pass
			else:
				pass # ignore any other command!
			return True
		elif self.status == STATUS_INIT:
			#print "check in status INIT"
			self.reset()
		elif self.status == STATUS_WAIT:
			#print "check in status WAIT"
			data = self.gui2ssprocess_queue.get()
			#print str(data)
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
			#print "check in other status."
			# something went wrong. Inconsistent state. Reset!
			self.reset()
		return True

	#def check_commands(self):
		
		
		#return True

	def reset(self):
		#print "func reset"
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
		
		self.ss_update = True
		self.ac_update = True
		self.go_update = True
		self.query_update = True
		self.output_update = True
		
		self.output_file = None
		self.output_buffer = None
		# reinitialize structures
		self.status = STATUS_WAIT

	def stop(self):
		print "func stop"
		#self.results = None
		# clear data
		if self.output_to == OUTPUT2FILE and not self.output_file == None:
			self.output_file.close()
		self.output_file = None
		self.output_buffer = None
		self.ssprocess2gui_queue.put((CMD_STOP, True))
		self.status = STATUS_WAIT

	def pause(self):
		#print "func pause"
		# do not clear data
		self.ssprocess2gui_queue.put((CMD_PAUSE, True))
		self.status = STATUS_PAUSE
		
	def _status(self):
		print "----------GO----------"
		if self.go_ok:
			print "GO is ok"
			print "GO loaded: " + str(self.go_filename)
			print "Nodes: " + str(self.go.node_num()) + ". Edges: " + str(self.go.edge_num())
		else:
			print "GO is not ok"
		print "----------AC----------"
		if self.ac_ok:
			print "AC is ok"
			print "AC loaded: " + str(self.ac_filename)
			print "Nodes: " + str(len(self.ac.annotations))
		else:
			print "AC is not ok"
		print "----------Query----------"
		if self.query_ok:
			print "Query is ok"
			if self.query_from == QUERYFROMGUI:
				print "Query loaded from gui"
			elif self.query_from == QUERYFROMFILE:
				print "Query loaded from file " + str(self.query_filename)
			elif  self.query_from == QUERYFROMAC:
				print "Query loaded from ac"
		else:
			print "Query is not ok"
		print "----------Output----------"
		if self.output_ok:
			print "Output is ok"
			if self.query_from == OUTPUT2GUI:
				print "Output to gui"
			elif self.query_from == OUTPUT2FILE:
				print "Output to file " + str(self.output_filename)
		else:
			print "Output is not ok"
		print "----------SS----------"
		if self.ss_ok:
			print "SS is ok"
			print "SS: " + str(self.ss_name)
			print "MS: " + str(self.ms_name)
			print "Ontology selected: " + str(self.ss_ontology)
		else:
			print "SS is not ok"
		print "--------------------"
		print "Current status"
		self.ssprocess2gui_queue.put((CMD_STATUS, self.status))

	def load_AC(self, data): #### data format: (filename, other) other = (file format, file format params)
		self.status = STATUS_LOAD_AC
		#print "func Load AC"
		self.ac_ok = False
		self.ss_update = True
		self.query_update = True
		#try:
		self.ac = AnnotationCorpus.AnnotationCorpus(self.go) #### what if go is missing?
		self.ac_filename = data[0]
		self.ac_filetype = data[1]
		self.ac_filetypeparams = data[2]
		if self.ac.parse(str(self.ac_filename), self.ac_filetype, self.ac_filetypeparams):
			if self.go == None or self.ac.sanitize():
				self.ac_ok = True
				self.ac_update = False
				self.communicate_AC(True)
			else:
				self.communicate_AC(False)
		else:
			self.communicate_AC(False)
		#except Exception:
			#print("Exception while loading annotation corpus.")
			self.communicate_AC(False)
		self.status = STATUS_WAIT

	def communicate_AC(self, result):
		if result:
			self.ssprocess2gui_queue.put((CMD_LOAD_AC, LOAD_AC_END, True, len(self.ac.annotations), len(self.ac.reverse_annotations)))
		else:
			self.ssprocess2gui_queue.put((CMD_LOAD_AC, LOAD_AC_END, False))

					
	def load_GO(self, data): #### data format: (filename)
		self.status = STATUS_LOAD_GO
		#print "func Load GO"
		self.go_ok = False
		self.ss_update = True
		self.ac_update = True
		self.query_update = True
		if len(data[0]) == 0:
			return
		self.go_filename = data[0]
		self.go = GeneOntology.load_GO_XML(open(self.go_filename,'r'))
		if not self.go == None:
			self.go_ok = True
			self.go_update = False
			self.ssprocess2gui_queue.put((CMD_LOAD_GO, LOAD_GO_END, True, self.go.node_num(), self.go.edge_num()))
		else:
			self.ssprocess2gui_queue.put((CMD_LOAD_GO, LOAD_GO_END, False))
		self.status = STATUS_WAIT

	def load_query(self, data): #### data format: (query from, query_params) query_params: none (fom ac), (type, filename) (from file), type (from gui)
		self.status = STATUS_LOAD_QUERY
		#print "func Load query"
		self.query_ok = False
		self.query_from = data[0]
		if self.query_from == QUERYFROMAC:
			#print "Query from AC selected."
			self.query_ok = True
			self.query_update = True
			self.query_type = 1
		elif self.query_from == QUERYFROMFILE:
			#print "Query from FILE selected."
			self.query_type = data[1]
			self.query_filename = data[2]
			#self.query_filetype = data[3]
			#self.query_filetypeparams = data[4]
			self.query_ok = True
			self.query_update = True
		elif self.query_from == QUERYFROMGUI: # expect to find query as input parameter of start messages
			#print "Query from GUI selected."
			#self.query = data[2]
			self.query_type = data[1]
			self.query_ok = True
			self.query_update = True
		else:
			pass
		#if self.query_ok: #### DANGER! If I enable this, I should read data back from pipe in gui process, otherwise application hangs!
			#self.ssprocess2gui_queue.put((CMD_LOAD_QUERY, True))
		#else:
			#self.ssprocess2gui_queue.put((CMD_LOAD_QUERY, False))
		self.status = STATUS_WAIT

	def load_SS(self, data): #### data format: (ss measure, ss measure params, mixing strat., mixing strat. params, ontology)
		self.status = STATUS_LOAD_SS
		#print "func Load SS"
		self.ss_ok = False
		self.ss_name = data[0]
		self.ss_params = data[1]
		self.ms_name = data[2]
		self.ms_params = data[3]
		self.ss_ontology = data[4]
		self.ss = False
		self.ss_ok = True
		self.ss_update = True
		if self.ss_ok:
			self.ssprocess2gui_queue.put((CMD_LOAD_SS, True))
			#print "load SS answer"
		else:
			self.ssprocess2gui_queue.put((CMD_LOAD_SS, False))
			#print "load SS answer"
		self.status = STATUS_WAIT

	def load_output(self, data): #### data format: (output_to, output_params) output_params: for file: (filename, type, params), for gui: (how many scores)
		self.status = STATUS_LOAD_OUTPUT
		#print "func Load output"
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
		self.output_update = True
		if self.query_ok:
			self.ssprocess2gui_queue.put((CMD_LOAD_OUTPUT, True))
		else:
			self.ssprocess2gui_queue.put((CMD_LOAD_OUTPUT, False))
		self.status = STATUS_WAIT

	def _start(self, data):
		self.status = STATUS_RUN
		self.start_data = data
		#print "func start"
		if not self.init_structures():
			self.ssprocess2gui_queue.put((CMD_START, False))
			self.status = STATUS_WAIT
		else:
			self.ssprocess2gui_queue.put((CMD_START, True, self.query_pairs_number))
			self._calculate()
			pass

	def init_go(self):
		if self.go_update:
			temp = []
			temp.append(self.go_filename)
			self.load_GO(temp)

	def init_ac(self):
		if self.ac_update:
			self.load_AC((self.ac_filename,self.ac_filetype,self.ac_filetypeparams))

	def init_ss(self):
		if self.ss_update:
			self.build_ss()

	def init_query(self):
		if self.query_update:
			if self.query_from == QUERYFROMGUI:
				self.query_update = False
				self.query = []
				self.query = self.start_data[0];
			elif self.query_from == QUERYFROMFILE:
				self.build_query_from_file()
			elif self.query_from == QUERYFROMAC:
				self.build_query_from_ac()
			else:
				return
		if self.query_type == 0:
			self.query_pairs_number = len(self.query) 
		elif self.query_type == 1:
			self.query_pairs_number = len(self.query) * (len(self.query)-1) / 2

	def build_query_from_file(self):
		h = open(self.query_filename,'r')
		self.query = []
		for line in h:
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			if self.query_type == 0: #pairs
				line = line.rsplit('\t')
				self.query.append((line[0], line[1]))
			else: # list
				self.query.append(line)
		h.close()
		self.query_update = False

	def build_query_from_ac(self):
		self.query = []
		if self.ac == None:
			return
		for line in self.ac.annotations:
			self.query.append(line)
		self.query_update = False

	def init_output(self):
		#print "init_output"
		if self.output_update:
			if self.output_to == OUTPUT2FILE:
				#print "output to file"
				self.output_file = open(self.output_filename, 'w')
			elif self.output_to == OUTPUT2GUI:
				#print "output to gui"
				self.output_buffer = [[]] * self.MAX_BUFFER_SIZE
				self.query_pairs_saved = 0
			else: 
				#print "else"
				return
			self.output_update = False

	def init_structures(self):
		#self.buffer = None # data will be stored here
		if not self.go_ok or not self.ac_ok or not self.ss_ok or not self.query_ok or not self.output_ok:
			#print "Something is not ready."
			return False
		self.init_go()
		self.init_ac()
		self.init_ss()
		self.init_query()
		self.init_output()
		if self.go_update or self.ac_update or self.ss_update or self.query_update or self.output_update:
			#print "Something is not updated."
			return False
		return True

		##self.counter = 0
		##self.last_percentual = -1
		##self.last_sent = -1
		##self.last_added = -1
	
		#if self.output_type==0:
			#if self.store_all:
				#self.buffer_size = self.total_number
			#else:
				#self.buffer_size = self.MAX_CACHE_SIZE
			#self.buffer = [None]*self.buffer_size
			##self.buffer = [(None, None, None)]*self.buffer_size
		#self.sstodo.value = self.total_number

	def build_ss(self):
		ssu = SemSimUtils.SemSimUtils(self.ac, self.go)
		ssu.det_offspring_table()
		ssu.det_ancestors_table()
		ssu.det_freq_table()
		ssu.det_GO_division()
		ssu.det_ICs_table()
		self.ss = ObjSemSim.ObjSemSim(self.ac, self.go, self.ss_name, self.ms_name, ssu)
		self.ss_update = False

	def _calculate(self):
		self.query_pairs_done = 0
		self.last_percentual = 0
		#print "Total pairs to process: " + str(self.query_pairs_number)
		if self.query_type == QUERY_LIST:
			for self.C_i in range(0,len(self.query)):
				for self.C_j in range(self.C_i + 1, len(self.query)):
					if self.query_pairs_done%self.CHECK_INTERVAL == 0:
						if not self.control():
							return
					test = self.ss.SemSim(self.query[self.C_i],self.query[self.C_j], self.ss_ontology)
					self.query_pairs_done += 1
					#if not int(self.query_pairs_done*100/self.query_pairs_number) == self.last_percentual:
						#self.last_percentual = int(self.query_pairs_done*100/self.query_pairs_number)
						#self.ssprocess2gui_queue.put((float(self.query_pairs_done)/self.query_pairs_number))
					if type(test) is float:
						test = str('%.4f' %test)
					if self.output_to == OUTPUT2GUI:
						#if not test == None:
						self.sendOutput(str(self.query[self.C_i]), str(self.query[self.C_j]), str(test))
					else:
						self.writeOutput(str(self.query[self.C_i]), str(self.query[self.C_j]), str(test))


		elif self.query_type == QUERY_PAIRS:
			for self.C_i in self.query:
				if self.query_pairs_done%20 == 0:
					if not self.control():
						return
				test = self.ss.SemSim(self.C_i[0],self.C_i[1], self.ss_ontology)
				self.query_pairs_done += 1
					#if not int(self.query_pairs_done*100/self.query_pairs_number) == self.last_percentual:
						#self.last_percentual = int(self.query_pairs_done*100/self.query_pairs_number)
						#self.ssprocess2gui_queue.put((float(self.query_pairs_done)/self.query_pairs_number))
				if type(test) is float:
					test = str('%.4f' %test)
				if self.output_to == OUTPUT2GUI:
					self.sendOutput(str(self.C_i[0]), str(self.C_i[1]), str(test))
				else:
					self.writeOutput(str(self.C_i[0]), str(self.C_i[1]), str(test))

		if self.output_to == OUTPUT2GUI:
			self.flushOutput()
		#if not self.counter == self.total_number:
			#print "Count error. Total pairs to process: " + str(self.total_number) + ". Total pairs processed: " + str(self.counter)
			#return self.abort()
		self.stop()
		#return self.set_completed()

	#def set_completed(self):
		#self.sscompleted.value = 1

	#def flush_data(self):
		#if self.output_type == 0:
			#self.flushOutput()
		#if self.output_type==1:
			#self.output_file_handle.close()
		#return True

	#def abort(self):
		#self.set_completed()
		#return True



	def sendOutput(self, a, b, c):
		#print (str(a),str(b),str(c))
		#if self.store_all:
			#self.last_added += 1
			#self.buffer[self.last_added] = ((str(a),str(b),str(c)))
			#if self.last_added - (self.last_sent + 1) > self.MAX_CACHE_SIZE:
				#self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added+1])
				#self.last_sent = self.last_added
		#else:
		self.output_buffer[self.query_pairs_saved] = (a,b,c)
		self.query_pairs_saved += 1
		if self.query_pairs_saved == len(self.output_buffer):
			self.ssprocess2gui_pipe.send(self.output_buffer)
			self.query_pairs_saved = 0

	def flushOutput(self):
		#if self.store_all:
			#if self.last_sent == self.last_added:
				#return
			#self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added+1])
			#self.last_sent = self.last_added
		#else:
		if self.query_pairs_saved == 0:
			return
		self.ssprocess2gui_pipe.send(self.output_buffer[0: self.query_pairs_saved])
		self.query_pairs_saved = 0

	def writeOutput(self, a, b, c):
		self.output_file.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\n")
		return True

