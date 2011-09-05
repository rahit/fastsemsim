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

class WorkThread(threading.Thread):

	def __init__(self, gui):
		super(WorkThread, self).__init__(self)
		self.gui = gui

	def run(self):
		self.skip_checks = False
		self.outputfield.Clear()
		self.logfield.AppendText('--------------------------------------\n')
#----------------------------------------------------------------------------------------------------
		#check if everything is configured
		if not self.skip_checks:
			if not self.go_ok:
				self.logfield.AppendText("Check Gene Ontology. Aborted\n")
				#self.logfield.AppendText("Aborted.\n")
				return False
			if not self.ac_ok:
				self.logfield.AppendText("Check Annotation Corpus. Aborted.\n")
				return False
			if not self.query_ok:
				self.logfield.AppendText("Check query. Aborted.\n")
				#self.logfield.AppendText("Aborted.\n")
				return False
			if not self.outputctrl_ok:
				self.logfield.AppendText("Check output parameters. Aborted.\n")
				#self.logfield.AppendText("Aborted.\n")
				return False
			if not self.operation_ok:
				self.logfield.AppendText("Check operation parameters. Aborted.\n")
			#self.logfield.AppendText("Aborted.\n")
				return False
#----------------------------------------------------------------------------------------------------
		self.logfield.AppendText("Data seems to be ok. Inizializing structures.\n")
		#Prepare sem sim object
		self.logfield.AppendText("-> Setting up semantic similarity...\n")
		if not self.buildSSobject():
			return False
#----------------------------------------------------------------------------------------------------
		# Prepare query
		self.logfield.AppendText("-> Setting up query...\n")
		if not self.buildQuery():
			self.logfield.AppendText("Failed to load query. Aborted.\n")
		else:
			if self.query_type == 0:
				self.logfield.AppendText("\tQuery loaded:" + (str(len(self.query))) + " pairs\n")
			elif self.query_type == 1:
				self.logfield.AppendText("Query loaded: " + str(len(self.query)) + " items.\n")
				print self.query
#----------------------------------------------------------------------------------------------------
		# Calculate SS scores
		self.logfield.AppendText("Evaluating semantic similarity...\n")
		self.sample_threshold = 100
		little_sample = 0
		if self.output_type==1:
			self.output_file_handle = open(self.output_file, 'w')
			self.outputfield.AppendText("Preview text. Complete output can be found here: "+str(self.output_file)+".\n")
		if self.query_type == 1: # list
			for i in range(0,len(self.query)):
				for j in range(i+1, len(self.query)):
					#print self.ssobject
					test = self.ssobject.SemSim(self.query[i],self.query[j], self.selectedGO)
					if type(test) is float:
						test = str('%.4f' %test)
					if self.output_type == 0:
						self.outputfield.AppendText(str(self.query[i]) + "\t" + str(self.query[j]) + "\t" + str(test) + "\n")
					else:
						self.output_file_handle.write(str(self.query[i]) + "\t" + str(self.query[j]) + "\t" + str(test) + "\n")
						if little_sample < self.sample_threshold:
							self.outputfield.AppendText(str(self.query[i]) + "\t" + str(self.query[j]) + "\t" + str(test) + "\n")
					little_sample+=1
		elif self.query_type == 0: # pairs
			for i in self.query:
				test = self.ssobject.SemSim(i[0],i[1], self.selectedGO)
				if self.output_type == 0:
					self.outputfield.AppendText(str(i[0]) + "\t" + str(i[1]) + "\t" + str(test) + "\n")
				else:
					self.output_file_handle.write(str(i[0]) + "\t" + str(i[1]) + "\t" + str(test) + "\n")
					if little_sample < self.sample_threshold:
						self.outputfield.AppendText(str(i[0]) + "\t" + str(i[1]) + "\t" + str(test) + "\n")
				little_sample+=1
		if self.output_type==1:
			self.outputfield.AppendText("Preview text. Complete output can be found here: "+str(self.output_file)+".\n")
			self.output_file_handle.close()
#----------------------------------------------------------------------------------------------------
		self.logfield.AppendText("Task correctly completed.\n")
		return False

	def buildQuery(self):
		self.SetQueryOk(False)
		result = True
		if self.query_from == 0: # from field
			result = False
			self.logfield.AppendText("\tLoading query from text field...\n")
			result = self.loadFromField()
			self.update_query = False
			result = True
		elif self.update_query: 
			self.query = None
			if self.query_from == 1: # from file
				self.logfield.AppendText("\tLoading query from file " + str(self.query_file) +"...\n")
				result = self.loadFromFile()
			elif self.query_from == 2: # from ac
				if self.query_type == 0:
					self.logfield.AppendText("Cannot get pairs from Annotation Corpus.\n")
				elif self.query_type == 1:
					self.logfield.AppendText("\tLoading query list from Annotation Corpus...\n")
					result = self.loadFromAC()
		else:
			self.logfield.AppendText("Using previous query...\n")
			result = True
		if result:
			self.update_query = False
		else:
			self.update_query = True
			self.query = None
		self.SetQueryOk(result)
		return result


	def buildSSobject(self):
		if self.update_ssobject or self.ssobject == None:
			self.ssobject = None
			if self.ssmeasure is None:
				return False
			#if SemSimMeasures.SemSimMeasures[self.Operationgui.ssmeasure][1]:
				#if self.mixingstrategy is None:
					#return False 
			if self.go is None or self.ac is None:
				return False
			##print self.ssmeasure
			#print self.mixingstrategy
			self.ssobject = ObjSemSim.ObjSemSim(self.ac, self.go, self.ssmeasure, self.mixingstrategy, None)
			if not self.ssobject is None:
				self.update_ssobject = False
				if not self.mixingstrategy is None:
					self.logfield.AppendText("Semantic similarity object created: " + str(self.ssmeasure) + " " + str(self.mixingstrategy) + ".\n")
				else:
					self.logfield.AppendText("Semantic similarity object created: " + str(self.ssmeasure) + ".\n")
			else:
				self.logfield.AppendText("Unable to create semantic similarity of type " + str(self.ssmeasure) + " " + str(self.mixingstrategy) + ".\n")
				return False
		else:
			self.logfield.AppendText("Using previous semantic similarity object.\n")
		return True

	def activateGoCmd(self):
		#print "activateGoCmd"
		if self.go_ok and self.ac_ok and self.query_ok and self.outputctrl_ok and self.operation_ok:
			self.SetStatus(1)
		else:
			self.SetStatus(0)
