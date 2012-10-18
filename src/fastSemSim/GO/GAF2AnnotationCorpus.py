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
#@desc
Class to parse Annotation Corporus files in GAF-2.0 format [i.e. Gene Ontology Annotation files]
'''

import sys
import os
import gzip
import GeneOntology

SIMPLIFY = 'simplify'

class GAF2AnnotationCorpus():

#------------------------------------------------------
# Inizialization routines
#------------------------------------------------------

	int_separator = '\t'
	int_comment = '!'

	def __init__(self, ac, parameters=None):
		self.ac = ac
		if self.ac == None:
			raise Exception
		self.parameters = parameters
		self.int_interpretParameters()

	def int_interpretParameters(self):
		self.int_simplify = False
		if self.parameters == None:
			return
		if len(self.parameters) > 0:
			if SIMPLIFY in self.parameters:
				self.int_simplify = self.parameters[SIMPLIFY]
#

#------------------------------------------------------
# Parsing routine
#------------------------------------------------------

	def setFields(self):
		if self.int_simplify:
			return
		self.ac.obj_fields = ['taxonomy']
		self.ac.term_fields = []
		self.ac.annotations_fields = ['EC'] # put also references? Not for now
		self.ac.reverse_annotations_fields = ['EC']
		self.ac.obj_field2pos= {'taxonomy':0}
		self.ac.term_field2pos= {}
		self.ac.annotations_field2pos= {'EC':0}
		self.ac.reverse_annotations_field2pos= {'EC':0}

	def isOk(self):
		if not self.ac.isOk('taxonomy', self.temp_taxonomy): return False
		if not self.ac.isOk('EC', self.temp_EC): return False

		if self.ac.int_exclude_GO_root:
			if self.temp_term == GeneOntology.BP_root or self.temp_term == GeneOntology.CC_root or self.temp_term == GeneOntology.MF_root:
				return False
		temp_term = int(self.temp_term[3:])
		if not self.ac.go == None and not self.ac.go.alt_ids == None:
			if not temp_term in self.ac.go.alt_ids:
				#print(str(self.temp_term) + " not found in GO.")
				return False
			if not temp_term in self.ac.go.nodes_edges:
				#print(str(self.temp_term) + " is obsolete.")
				return False
		return True
#






	def parse(self, fname):
		#print "GAF2AnnotationCorpus: parse()"
		self.setFields()
		if type(fname) == unicode:
			fname = str(fname)
		if type(fname) is str:
			fn,fe = os.path.splitext(fname)
			if fe == '.gz':
				stream = gzip.open(fname, 'rb')
			else:
				stream = open(fname, 'r')
		else:
			stream = fname
		lines_counter = 0
		#ignored = 0
		for line in stream:
			lines_counter += 1
			line = line.rstrip('\n')
			line = line.rstrip('\r')
			if lines_counter == 1:
				pass # to implement
			if line[0] == self.int_comment:
				continue
			line = line.split(self.int_separator)
			if len(line) < 14:
				print("GAF2AnnotationCorpus loader. Incomplete line: " + str(line))
				continue
			self.temp_taxonomy = line[12][6:]
			temp = self.temp_taxonomy.rsplit('|')
			if len(temp) > 1:
				self.temp_taxonomy = temp[0]
			self.temp_obj = line[1]
			self.temp_term = line[4]
			self.temp_EC = line[6]
			self.temp_reference = line[5]
			self.temp_GO = line[8]

			if not self.isOk():
				#ignored+=1
				continue

			self.temp_term = int(self.temp_term[3:])
			if not self.ac.go == None and not self.temp_term == self.ac.go.alt_ids[self.temp_term]:
				print("Remapping " + str(self.temp_term) + " to " + str(self.ac.go.alt_ids[self.temp_term]))
				self.temp_term = self.ac.go.alt_ids[self.temp_term]

			#### Build up genes set
			if self.temp_obj not in self.ac.obj_set:
				if self.int_simplify:
					self.ac.obj_set[self.temp_obj] = None
				else:
					self.ac.obj_set[self.temp_obj] = (self.temp_taxonomy,)
			if self.temp_term not in self.ac.term_set:
				self.ac.term_set[self.temp_term] = None
			#### Build up annotations set
			if self.temp_obj not in self.ac.annotations:
				self.ac.annotations[self.temp_obj] = {}
			if self.temp_term not in self.ac.annotations[self.temp_obj]:
				self.ac.annotations[self.temp_obj][self.temp_term] = []
			if self.int_simplify:
				self.ac.annotations[self.temp_obj][self.temp_term] = None
			else:
				self.ac.annotations[self.temp_obj][self.temp_term].append((self.temp_EC, self.temp_reference))
			#### Build up reverse annotations set
			if self.temp_term not in self.ac.reverse_annotations:
				self.ac.reverse_annotations[self.temp_term] = {}
			if self.temp_obj not in self.ac.reverse_annotations[self.temp_term]:
				self.ac.reverse_annotations[self.temp_term][self.temp_obj] = []
			if self.int_simplify:
				self.ac.reverse_annotations[self.temp_term][self.temp_obj] = None
			else:
				self.ac.reverse_annotations[self.temp_term][self.temp_obj].append((self.temp_EC, self.temp_reference))

			#if self.ac.SHOW_PROCESS and (lines_counter%(filenum/20)==0):
				#print("Lines processed: " + str(lines_counter) + " on " + str(filenum) + " (" + str(int(100*float(lines_counter)/float(filenum))) + "%)")
		if type(fname) is str:
			stream.close()
		return True
