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

"""
GENERAL INFO

This class provides the prototype for a generic Term Semantic Similarity measure (TSS)

There are two types of Term Sem Sim: those which evaluate the semantic similarity between two sets of terms (groupwise - G_TSS), and those which can only evaluate the similarity between pairs of GO terms (pairwise - P_TSS). Each class extending TermSemSim should declare whether it is groupwise or pairwise.

TermSemSim relies on SemSimUtils to perform a lot of tasks (such as evaluating Term IC or common ancestors)
a SemSimUtils object can be passed to the constructor as input data. Otherwise, a new instance will be created. Using only one copy of SemSimUtils helps reducing time and spece requirements and is strongly adviced.
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
from SemSimUtils import *
import sys
import os
import math




	#-#-#-#-#-#-#-#-#-#-#
	# class TermSemSim  #
	#-#-#-#-#-#-#-#-#-#-#

class MissingAcException(Exception):
	def __init__(self, message):
		self.message = message
#

class TermSemSim(object):
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	format_and_check_data = True
	P_TSS = "Pairwise"
	G_TSS = "Groupwise"
	SS_type = None # Type of Term Sem Sim: Can be P_TSS or G_TSS
	IC_based = False # Tells whether te Term Sem Sim is based on Information Content

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#### internal functions

	def __init__(self, ac, go, util = None):
		self.go = go
		self.annotation_corpus = ac
		self.util = util
		if self.IC_based and self.annotation_corpus == None:
			raise MissingAcException("The selected semantic measure is based on IC and requires an annotation corpus.")
		if self.util == None:
			self.util = SemSimUtils(ac, go)
		if self.IC_based and self.util.IC == None:
			self.util.det_IC_table()


	def int_validate_single_term(self, term):
	# verifies whether a single GO terms is valid. It means it has not to be obsolete.
	# In addition, if the Term SS measure is based on IC, the GO Term should also possess an IC [which means it has to be annotated for at least one protein]
	# ONLY NUMERIC INPUT IS ACCEPTED HERE
		if not type(term) is int:
			#print "Invalid term format: " + str(type(term))
			return None
		if term not in self.go.nodes_edges:
			if term not in self.go.alt_ids:
				return None
			if self.go.alt_ids[term] == term:
					#print("Term " + str(term) + " is an obsolete id.")
				return None
			else:
				term = self.go.alt_ids[term]
			return None
		if self.IC_based:
			if not term in self.util.IC:
				#print("Term " + str(term) + " does not have an IC.")
				return None
			if self.util.IC[term] == None:
				#print("Term " + str(term) + " does not have an IC.")
				return None
		return term


	def int_format_data(self, term1):
	# convert query data in the proper format
	# verify query data are consistent with current GO
	# verify query data come from the same GO. Overload this function for cross-ontological Term Sem Sim measures or they won't work.

		id1 = self.util.go.name2id(term1) # convert GO Term ids to internal format. See name2id function in GeneOntology class
		if self.SS_type == self.P_TSS:
			nid = self.int_validate_single_term(id1)
			#print str(id1) + " --> " + str(nid) 
			if not nid==None:
				return nid
			return None
		elif self.SS_type == self.G_TSS:
			if type(id1) is int:
				temp_id1 = {}
				temp_id1[id1] = None
			elif type(id1) is dict:
				temp_id1 = id1
				temp_id1 = temp_id1.keys()
			elif type(id1) is list:
				temp_id1 = id1
			else:
				raise Exception
			current_onto = None
			n_temp_id1 = {}
			for i in temp_id1:
				nid = self.int_validate_single_term(i)
				# print str(i) + " --> " + str(nid) 
				if nid == None:
					return None
				n_temp_id1[nid] = None
				if current_onto is None:
					current_onto = self.util.GO_root[nid]
				elif not current_onto == self.util.GO_root[nid]:
					#print("Terms are not from the same ontology")
					return None
			return n_temp_id1.keys()

	def int_SemSim(self, term1, term2):
		# Return None, since this class is just a prototype
		return None

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#### public function

	def setSanityCheck(self, en):
	# This enables or disables sanity checks and conversion on query data.
	# If speeds up computation, but if input data are not correct expect exceptions to be raised
		self.format_and_check_data = en


	def SemSim(self, term1, term2):
	# This is the main function that should be called to evaluate the Term Sem Sim
	# It takes care of verifying data, format them, and evaluate the Sem Sim.
	# It might be necessary to Overload this function for cross-ontological Term Sem Sim measures 
		if self.format_and_check_data:
			if term1 is None or term2 is None:
				return None
			id1 = self.int_format_data(term1)
			id2 = self.int_format_data(term2)
			#print "\""+term1+"\""
			#print "\""+term2+"\""
			#print id1
			#print id2
			if id1 is None or id2 is None or (self.SS_type == self.G_TSS and len(id1) == 0) or (self.SS_type == self.G_TSS and len(id2) == 0):
				#print(str(term1) + " or " + str(term2) + "   not valid.")
				return None
			if self.SS_type == self.P_TSS:
				if not self.util.GO_root[id1] == self.util.GO_root[id2]:
					#raise "Terms are not from the same ontology"
					return None
			elif self.SS_type == self.G_TSS:
				for i in id1:
					t1 = i
					break
				for i in id2:
					t2 = i
					break
				if not self.util.GO_root[t1] == self.util.GO_root[t2]:
					#raise "Terms are not from the same ontology"
					return None
		else:
			id1 = term1
			id2 = term2
		return self.int_SemSim(id1, id2)
