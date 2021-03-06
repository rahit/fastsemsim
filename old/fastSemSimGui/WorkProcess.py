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

'''
WorkProcess is the background process that handles data and evaluates the semantic similarity.
'''
import multiprocessing
import time 
import copy
import os
from fastSemSim.SemSim import SemSimMeasures
from fastSemSim.SemSim import ObjSemSim
from fastSemSim.SemSim import SemSimUtils
from fastSemSim.GO import GeneOntology
from fastSemSim.GO import AnnotationCorpus
import gzip

# WorkProcess is designed as a state machine. Here are the possible status
STATUS_BASE = 0
STATUS_INIT = STATUS_BASE + 0 # before reset. Reset in progress. Not available for communication
STATUS_WAIT = STATUS_BASE + 1 # waiting. Ready to communicate with other processes. No computation in progress
STATUS_RUN = STATUS_BASE + 2 # computation in progress. Messages from other processes are delayed.
STATUS_PAUSE = STATUS_BASE + 3 # Pause status. Computation has been suspended. Receptive to external messages
STATUS_LOAD_GO = STATUS_BASE + 4 # Loading the GO. Not receptive to external messages
STATUS_LOAD_AC = STATUS_BASE + 5 # Loading the Annotation Corpus. Not receptive to external messages
STATUS_LOAD_SS = STATUS_BASE + 6 # Inizializing SemSim Object. Not receptive to external messages
STATUS_LOAD_QUERY = STATUS_BASE + 7 # Loading query.  Not receptive to external messages
STATUS_LOAD_OUTPUT = STATUS_BASE + 8 # Loading output parameters. Not receptive to external messages

# Commands handled by WorkProcess
CMD_BASE = 100
CMD_NONE = CMD_BASE
CMD_START = CMD_BASE + 1 # Start the computation
CMD_STOP = CMD_BASE + 2 # Stop the computation. Semantic similarity scores are cleared, but all the other data and settings are mantained
CMD_PAUSE = CMD_BASE + 3 # Pause the computation.
CMD_RESET = CMD_BASE + 4 # Reinizialize the class. Clear all the variables!
CMD_STATUS = CMD_BASE + 5 # Return status information
CMD_LOAD_AC = CMD_BASE + 6 # Load an Annotation Corpus
CMD_LOAD_GO = CMD_BASE + 7 # Load a Gene Ontology
CMD_LOAD_QUERY = CMD_BASE + 8 # Load a Query
CMD_LOAD_SS = CMD_BASE + 9 # Initialize Semantic Similarity Engine
CMD_LOAD_OUTPUT = CMD_BASE + 10 # Load Output parameters
CMD_DESTROY =  CMD_BASE + 11 # Kill the process

# Codes used in outgoing messages
ANSWER_BASE = 100
ANSWER_IGNORED =  ANSWER_BASE + 1 # Previous message has been ignored 
ANSWER_PROCESSED =  ANSWER_BASE + 2 # Previous message has been accepted and completely processed
ANSWER_PROCESSING =  ANSWER_BASE + 3 # Previous message has been accepted but is still being process

# Constants
LOAD_AC_BASE = 200
LOAD_AC_END = LOAD_AC_BASE + 1
LOAD_AC_STATUS = LOAD_AC_BASE + 2

LOAD_GO_BASE = 300 
LOAD_GO_END = LOAD_GO_BASE + 1
LOAD_GO_STATUS = LOAD_GO_BASE + 2


OUTPUT_TO_GUI = 0
OUTPUT_TO_FILE = 1

QUERY_FROM_GUI = 0
QUERY_FROM_AC = 2
QUERY_FROM_FILE = 1

QUERY_PAIRS = 0
QUERY_LIST = 1





	#-#-#-#-#-#-#-#-#-#-#-#
	# Class WorkProcess   #
	#-#-#-#-#-#-#-#-#-#-#-#

class WorkProcess(multiprocessing.Process):

	# some static settings
	print_output = False
	MAX_BUFFER_SIZE = 5000
	CHECK_INTERVAL = 5000

	#### __init__ receives in input the 4 channels used for bidirectional communication with gui process
	# WorkProcess communicates through 4 channels: 2 ingoing and 2 outgoing. In each direction a pipe and a queue are available.#
	def __init__(self, gui2ssprocess_queue, ssprocess2gui_queue, gui2ssprocess_pipe, ssprocess2gui_pipe):
		multiprocessing.Process.__init__(self)
		self.ssprocess2gui_queue = ssprocess2gui_queue
		self.gui2ssprocess_queue = gui2ssprocess_queue
		self.gui2ssprocess_pipe = gui2ssprocess_pipe
		self.ssprocess2gui_pipe = ssprocess2gui_pipe
		self.status = STATUS_INIT

	#### inizialize structures and flags
	def reset(self):
		# ok flags. True if the corresponding component is correctly and completely configured
		self.ok_ss = False
		self.ok_ac = False
		self.ok_go = False
		self.ok_query = False
		self.ok_output = False

		self.go = None # Gene Ontology
		self.ac = None # Annotation Corpus
		self.query = None # Query
		self.ss = None # ss object implementing the desired semantic similarity measure
		self.output = None # 
		self.results = None # 
		
		self.ss_update = True
		self.ac_update = True
		self.go_update = True
		self.query_update = True
		self.output_update = True
		
		self.output_file = None
		self.output_buffer = None

		self.status = STATUS_WAIT






#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

	#-#-#-#-#-#-#-#-#-#-#-#
	# main loop function  #
	#-#-#-#-#-#-#-#-#-#-#-#

	def run(self):
		while self.control():
			pass
		return 0
#




	def control(self):

		# in RUN status only STOP, PAUSE, RESET or STATUS commands are accepted. The other are ignored.
		# If no messages have been received the computation continues
		if self.status == STATUS_RUN:
			#print "STATUS: Run"
			try:
				if not self.gui2ssprocess_queue.empty():
					data = self.gui2ssprocess_queue.get(False)
					if data[0] == CMD_DESTROY:
						return False
					if data[0] == CMD_STOP:
						self._stop()
					elif data[0] == CMD_PAUSE:
						self.pause()
					elif data[0] == CMD_RESET:
						self.reset()
					elif data[0] == CMD_STATUS:
						self._status()
						self._calculate()
					elif data[0] == CMD_START:
						self._calculate()
					else:
						print "Unhandled message in RUN status: " + str(data[0])
						# send ignored message?
						self._calculate()
				else:
					# send ignored message?
					self._calculate()
			except Exception:
				pass

		# in PAUSE status only STOP, PAUSE, RESET, STATUS and START commands are accepted. The other are ignored.
		# get is casted in blocking mode since no computation has to be performed
		# If no messages have been received the computation continues
		elif self.status == STATUS_PAUSE:
			#print "STATUS: Pause"
			data = self.gui2ssprocess_queue.get()
			if data[0] == CMD_DESTROY:
				return False
			if data[0] == CMD_STOP:
				self.stop()
			elif data[0] == CMD_RESET:
				self.status = STATUS_INIT
			elif data[0] == CMD_STATUS:
				self._status()
			elif data[0] == CMD_START:
				self._restart()
			elif data[0] == CMD_PAUSE:
				pass
			else:
				print "Unhandled message in PAUSE status: " + str(data[0])
				# send ignored message?
				pass


		# (re)initialize object
		elif self.status == STATUS_INIT:
			self.reset()

		# in WAIT status WorkProcess handles LOAD_* messages
		# Get is casted in blocking mode since no computation is performed meanwhile
		elif self.status == STATUS_WAIT:
			#print "STATUS: Wait"
			data = self.gui2ssprocess_queue.get()
			if data[0] == CMD_DESTROY:
				return False
			if data[0] == CMD_STOP or data[0] == CMD_PAUSE: # No effect here
				pass
			elif data[0] == CMD_RESET:
				self.status = STATUS_INIT
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
			elif data[0] == CMD_NONE: # useless statement
				pass
			else: # any other message does not have any effect
				# send ignored message?
				pass
			
		# if other status are revealed (possibly due to aborted operations) WorkProcess is reinitialized
		else:
			print "Invalid status. Reinitializing..."
			self.status = STATUS_INIT
		return True

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-




	#-#-#-#-#-#-#-#-#-#-#-#
	# main loop function  #
	#-#-#-#-#-#-#-#-#-#-#-#

	def send(message):
		self.ssprocess2gui_queue.put((message, True))

		
	def _status(self):
		if self.print_output:
			print "----------GO----------"
			if self.ok_go:
				print "GO is ok"
				print "GO loaded: " + str(self.go_filename)
				print "Nodes: " + str(self.go.node_num()) + ". Edges: " + str(self.go.edge_num())
			else:
				print "GO is not ok"
			print "----------AC----------"
			if self.ok_ac:
				print "AC is ok"
				print "AC loaded: " + str(self.ac_filename)
				print "Nodes: " + str(len(self.ac.annotations))
			else:
				print "AC is not ok"
			print "----------Query----------"
			if self.ok_query:
				print "Query is ok"
				if self.query_from == QUERY_FROM_GUI:
					print "Query loaded from gui"
				elif self.query_from == QUERY_FROM_FILE:
					print "Query loaded from file " + str(self.query_filename)
				elif  self.query_from == QUERY_FROM_AC:
					print "Query loaded from ac"
			else:
				print "Query is not ok"
			print "----------Output----------"
			if self.ok_output:
				print "Output is ok"
				if self.query_from == OUTPUT_TO_GUI:
					print "Output to gui"
				elif self.query_from == OUTPUT_TO_FILE:
					print "Output to file " + str(self.output_filename)
			else:
				print "Output is not ok"
			print "----------SS----------"
			if self.ok_ss:
				print "SS is ok"
				print "SS: " + str(self.ss_name)
				print "MS: " + str(self.ms_name)
				print "Ontology selected: " + str(self.ss_ontology)
			else:
				print "SS is not ok"
			print "--------------------"
			print "Current status"
		self.ssprocess2gui_queue.put((CMD_STATUS, self.status))
#




#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


	#-#-#-#-#-#-#-#-#-#-#-#-#
	# data parsing routines #
	#-#-#-#-#-#-#-#-#-#-#-#-#
	
	
	
	def load_AC(self, data): #### data format: (filename, other) other = (file format, file format params)
		self.status = STATUS_LOAD_AC

		self.ok_ac = False
		self.ss_update = True
		self.query_update = True
		try:
			self.ac = AnnotationCorpus.AnnotationCorpus(self.go)
			self.ac_filename = data[0]
			self.ac_filetype = data[1]
			self.ac_filetypeparams = data[2]
			if self.ac.parse(str(self.ac_filename), self.ac_filetype, self.ac_filetypeparams):
				self.ok_ac = True
				if self.go == None:
					self.ac_update = True
				elif self.ac.sanitize():
					self.ac_update = False
		except Exception:
			pass
		self.communicate_AC(self.ok_ac)
		self.status = STATUS_WAIT

	def communicate_AC(self, result):
		if result:
			self.ssprocess2gui_queue.put((CMD_LOAD_AC, LOAD_AC_END, True, len(self.ac.annotations), len(self.ac.reverse_annotations)))
		else:
			self.ssprocess2gui_queue.put((CMD_LOAD_AC, LOAD_AC_END, False))
#






	def load_GO(self, data): #### data format: (filename)
		self.status = STATUS_LOAD_GO
		self.ok_go = False
		self.ss_update = True
		self.ac_update = True
		self.query_update = True
		if data[0] == None or len(data[0]) == 0:
			self.go = None
		else:
			self.go_filename = data[0]
			try:
				fn,fe = os.path.splitext(self.go_filename)
				if fe == '.gz':
					go_handle = gzip.open(self.go_filename, 'rb')
				else:
					go_handle = open(self.go_filename,'r')
				self.go = GeneOntology.load_GO_XML(go_handle)
				go_handle.close()
			except Exception:
				self.go = None

		if not self.go == None:
			self.ok_go = True
			self.go_update = False
			self.ssprocess2gui_queue.put((CMD_LOAD_GO, LOAD_GO_END, True, self.go.node_num(), self.go.edge_num()))
		else:
			self.go_filename = None
			self.ssprocess2gui_queue.put((CMD_LOAD_GO, LOAD_GO_END, False))

		self.status = STATUS_WAIT
#





	def load_query(self, data): #### data format: (query from, query_params) query_params: none (fom ac), (type, filename) (from file), type (from gui)
		self.status = STATUS_LOAD_QUERY
		#print "func Load query"
		self.ok_query = False
		self.query_from = data[0]
		if self.query_from == QUERY_FROM_AC:
			#print "Query from AC selected."
			self.ok_query = True
			self.query_update = True
			self.query_type = 1
		elif self.query_from == QUERY_FROM_FILE:
			#print "Query from FILE selected."
			self.query_type = data[1]
			self.query_filename = data[2]
			#self.query_filetype = data[3]
			#self.query_filetypeparams = data[4]
			self.ok_query = True
			self.query_update = True
		elif self.query_from == QUERY_FROM_GUI: # expect to find query as input parameter of start messages
			#print "Query from GUI selected."
			#self.query = data[2]
			self.query_type = data[1]
			self.ok_query = True
			self.query_update = True
		else:
			pass
		#if self.ok_query: #### DANGER! If I enable this, I should read data back from pipe in gui process, otherwise application hangs!
			#self.ssprocess2gui_queue.put((CMD_LOAD_QUERY, True))
		#else:
			#self.ssprocess2gui_queue.put((CMD_LOAD_QUERY, False))
		self.status = STATUS_WAIT
#





	def load_SS(self, data): #### data format: (ss measure, ss measure params, mixing strat., mixing strat. params, ontology)
		self.status = STATUS_LOAD_SS
		#print "func Load SS"
		self.ok_ss = False
		self.ss_name = data[0]
		self.ss_params = data[1]
		self.ms_name = data[2]
		self.ms_params = data[3]
		self.ss_ontology = data[4]
		self.ss = False
		self.ok_ss = True
		self.ss_update = True
		if self.ok_ss:
			self.ssprocess2gui_queue.put((CMD_LOAD_SS, True))
			#print "load SS answer"
		else:
			self.ssprocess2gui_queue.put((CMD_LOAD_SS, False))
			#print "load SS answer"
		self.status = STATUS_WAIT
#






	def load_output(self, data): #### data format: (output_to, output_params) output_params: for file: (filename, type, params), for gui: (how many scores)
		self.status = STATUS_LOAD_OUTPUT
		#print "load_output" + str(data)
		self.ok_output = False
		self.output_to = data[0]
		if self.output_to == OUTPUT_TO_FILE:
			self.output_filename = data[1]
			self.output_filetype = data[2]
			self.output_filetypeparams = data[3]
		elif  self.output_to == OUTPUT_TO_GUI:
			self.output_filename = None
			self.output_params = data[1]
		self.ok_output = True
		self.output_update = True
		if self.ok_query:
			self.ssprocess2gui_queue.put((CMD_LOAD_OUTPUT, True))
		else:
			self.ssprocess2gui_queue.put((CMD_LOAD_OUTPUT, False))
		self.status = STATUS_WAIT
#



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


	#-#-#-#-#-#-#-#-#-#-#-#
	# utility functions   #
	#-#-#-#-#-#-#-#-#-#-#-#
	
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
#




	def build_query_from_ac(self):
		self.query = []
		if self.ac == None:
			return
		for line in self.ac.annotations:
			self.query.append(line)
		self.query_update = False
#




	def build_ss(self):
		ssu = SemSimUtils.SemSimUtils(self.ac, self.go)
		ssu.det_IC_table()
		self.ss = ObjSemSim.ObjSemSim(self.ac, self.go, self.ss_name, self.ms_name, ssu)
		self.ss.TSS.format_and_check_data = False
		self.ss_update = False

#



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	# initialization function #
	#-#-#-#-#-#-#-#-#-#-#-#-#-#
	

	def init_go(self):
		if self.go_update:
			temp = [self.go_filename,]
			if self.load_GO(temp):
				self.go_update = False
		return True
#



	def init_ac(self):
		if self.ac_update:
			#if self.load_AC((self.ac_filename,self.ac_filetype,self.ac_filetypeparams)):
			if self.ac.sanitize():
				self.ac_update = False
		return True
#



	def init_ss(self):
		if self.ss_update:
			if self.build_ss():
				self.ss_update = False
		return True
#




	def init_query(self):
		if self.query_update:
			if self.query_from == QUERY_FROM_GUI:
				self.query = self.start_data[0]; #### expecting query as start parameters!
			elif self.query_from == QUERY_FROM_FILE:
				self.build_query_from_file()
			elif self.query_from == QUERY_FROM_AC:
				self.build_query_from_ac()
			else:
				raise Exception
		if self.query_type == QUERY_PAIRS:
			self.query_pairs_number = len(self.query) 
		elif self.query_type == QUERY_LIST:
			self.query_pairs_number = len(self.query) * (len(self.query)-1) / 2
		self.query_update = False
		return True
#




	def init_output(self):
		if self.output_update:
			if self.output_to == OUTPUT_TO_FILE:
				self.output_file = open(self.output_filename, 'w')
			elif self.output_to == OUTPUT_TO_GUI:
				self.output_buffer = [[]] * self.MAX_BUFFER_SIZE
				self.query_pairs_saved = 0
			else: 
				raise Exception
			self.output_update = False
		return True
#





	def _init_structures(self):
		if not self.ok_go or not self.ok_ac or not self.ok_ss or not self.ok_query or not self.ok_output:
			# Send message to other process?
			return False

		# initialize components
		if not self.init_go():
			#print "self.ok_go"
			return False
		if not self.init_ac():
			#print "self.ok_ac"
			return False
		if not self.init_ss():
			#print "self.ok_ss"
			return False
		if not self.init_query():
			#print "self.ok_query"
			return False
		if not self.init_output():
			#print "self.ok_output"
			return False

		# last check
		if self.go_update or self.ac_update or self.ss_update or self.query_update or self.output_update:
			return False

		return True
#







#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#	MAIN ROUTINES	MAIN ROUTINES	MAIN ROUTINES	MAIN ROUTINES	MAIN ROUTINES	MAIN ROUTINES	MAIN ROUTINES


	#-#-#-#-#-#-#-#-#-#-#
	# _start function   #
	#-#-#-#-#-#-#-#-#-#-#

	def _start(self, data):
		#print "_start"
		self.start_data = data
		
		# initialize modules
		if not self._init_structures():
			#print "_init_structures returned FALSE"
			# send error message?
			return self._stop()


		self.status = STATUS_RUN
		self.ssprocess2gui_queue.put((CMD_START, True, self.query_pairs_number))
		self.obj1_pos = 0
		self.obj2_pos = 1
		self.obj_pos = 0
		self.pairs_done = 0
		self._calculate()
#







	#-#-#-#-#-#-#-#-#-#-#-#
	# _restart function   #
	#-#-#-#-#-#-#-#-#-#-#-#
	
	def _restart(self):
		self.status = STATUS_RUN
		self.ssprocess2gui_queue.put((CMD_START, True, self.query_pairs_number))
		self._calculate()
#







	#-#-#-#-#-#-#-#-#-#-#
	# _stop function    #
	#-#-#-#-#-#-#-#-#-#-#
	
	# go, ac, query, output parameters and ss should be mantained as valid
	# output data should be flushed, as well as temporary variables.
	# output_update should be set to true to reinitialize output structures
	def _stop(self):
		if self.output_to == OUTPUT_TO_FILE and not self.output_file == None:
			self.output_file.close()
		self.output_file = None
		self.output_buffer = None
		self.output_update = True
		self.ssprocess2gui_queue.put((CMD_STOP, True))
		self.status = STATUS_WAIT
#








	#-#-#-#-#-#-#-#-#-#-#
	# _pause function   #
	#-#-#-#-#-#-#-#-#-#-#
	
	def pause(self):
		self.ssprocess2gui_queue.put((CMD_PAUSE, True))
		self.status = STATUS_PAUSE
#









	#-#-#-#-#-#-#-#-#-#-#-#
	# _calculate function #
	#-#-#-#-#-#-#-#-#-#-#-#

	def _calculate(self):
		#print(self.obj1_pos)
		#print(self.obj2_pos)
		#print(self.obj_pos)

		if self.query_type == QUERY_LIST:
			for self.obj1_pos in range(self.obj1_pos, len(self.query)):
				for self.obj2_pos in range(self.obj2_pos, len(self.query)):
					self._temp_ss = self.ss.SemSim(self.query[self.obj1_pos],self.query[self.obj2_pos], self.ss_ontology)
					self._dispatch_output()
					self.pairs_done += 1
					#print self.pairs_done
					if self.obj2_pos == len(self.query) - 1:
						self.obj2_pos = self.obj1_pos + 2
						break
					if self.pairs_done%self.CHECK_INTERVAL == 0:
						self.obj2_pos = self.obj2_pos + 1
						return

		elif self.query_type == QUERY_PAIRS:
			for self.obj_pos in range(self.obj_pos,len(self.query)):
				self._temp_ss = self.ss.SemSim(self.query[self.obj_pos][0], self.query[self.obj_pos][1], self.ss_ontology)
				self._dispatch_output()
				self.pairs_done += 1
				#print self.pairs_done
				if self.pairs_done%self.CHECK_INTERVAL == 0:
					return


		self._flush_output()
		self._stop()
#








	#-#-#-#-#-#-#-#-#-#-#-#
	# _dispatch_output f. #
	#-#-#-#-#-#-#-#-#-#-#-#
	
	def _dispatch_output(self):
		# add here switch to ignore None if required
		if type(self._temp_ss) is float:
			self._temp_ss = str('%.4f' %self._temp_ss)

		if self.query_type == QUERY_LIST:
			if self.output_to == OUTPUT_TO_GUI:
				self._send_output(str(self.query[self.obj1_pos]), str(self.query[self.obj2_pos]), str(self._temp_ss))
			else:
				self._write_output(str(self.query[self.obj1_pos]), str(self.query[self.obj2_pos]), str(self._temp_ss))

		elif self.query_type == QUERY_PAIRS:
			if self.output_to == OUTPUT_TO_GUI:
				self._send_output(str(self.query[self.obj_pos][0]), str(self.query[self.obj_pos][1]), str(self._temp_ss))
			else:
				self._write_output(str(self.query[self.obj_pos][0]), str(self.query[self.obj_pos][1]), str(self._temp_ss))
#








	#-#-#-#-#-#-#-#-#-#-#-#
	# _send_output func.  #
	#-#-#-#-#-#-#-#-#-#-#-#
	
	def _send_output(self, a, b, c):
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
#







	#-#-#-#-#-#-#-#-#-#-#-#
	# _flush_output func. #
	#-#-#-#-#-#-#-#-#-#-#-#
	
	def _flush_output(self):
		#if self.store_all:
			#if self.last_sent == self.last_added:
				#return
			#self.ssprocess2gui_pipe.send(self.buffer[self.last_sent+1: self.last_added+1])
			#self.last_sent = self.last_added
		#else:
		if not self.output_to == OUTPUT_TO_GUI:
			return
		if self.query_pairs_saved == 0:
			return
		self.ssprocess2gui_pipe.send(self.output_buffer[0: self.query_pairs_saved])
		self.query_pairs_saved = 0
#




	#-#-#-#-#-#-#-#-#-#-#-#
	# _write_output func. #
	#-#-#-#-#-#-#-#-#-#-#-#
	
	def _write_output(self, a, b, c):
		self.output_file.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\n")
		return True
#
