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
This class provides the prototype for a generic Term Semantic Similarity measure (TSS)

"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSimUtils import *
import sys
import os
import math

class TermSemSim(object):
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
	format_and_check_data = True
# variables
	P_TSS = "Pairwise"
	G_TSS = "Groupwise"
	SS_type = None
	IC_based = False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# private functions

	def __init__(self, ac, go, util = None):
		self.go = go
		self.annotation_corpus = ac
		self.util = util
		if self.util == None:
			self.util = SemSimUtils(ac, go)
		if self.IC_based and self.util.IC == None:
			self.util.det_IC_table()

	def int_validate_single_term(self, term):
		if not type(term) is int:
			#print "Invalid term format: " + str(type(term))
			return False
		if term not in self.go.nodes_edges:
			#print(str(term) + " is not a valid term.")
			return False
		#if (not ignore_IC) and self.IC_based:
		if self.IC_based:
			if not term in self.util.IC:
				print("Term " + str(term) + " does not have an IC.")
				return False
			if self.util.IC[term] == None:
				print("Term " + str(term) + " does not have an IC.")
				return False
		return True

	def int_format_data(self, term1):
		id1 = self.util.go.name2id(term1)
		if self.SS_type == self.P_TSS:
			if self.int_validate_single_term(id1):
				return id1
			return None
		elif self.SS_type == self.G_TSS:
			if type(id1) is int:
				temp_id1 = []
				temp_id1.append(id1)
			else:
				temp_id1 = id1
			current_onto = None
			for i in temp_id1:
				if not self.int_validate_single_term(i):
					return None
				if current_onto is None:
					current_onto = self.util.GO_root[i]
				elif not current_onto == self.util.GO_root[i]:
					#print("Terms are not from the same ontology")
					return None
			return temp_id1

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
# public function
	def int_SemSim(self, term1, term2):
		print "Input data is ok, but no term sem sim specified."
		return None

	def SemSim(self, term1, term2):
		if self.format_and_check_data:
			if term1 is None or term2 is None:
				return None
			id1 = self.int_format_data(term1)
			id2 = self.int_format_data(term2)
			if id1 is None or id2 is None or (self.SS_type == self.G_TSS and len(id1) == 0) or (self.SS_type == self.G_TSS and len(id2) == 0):
				#print(str(term1) + " or " + str(term2) + "   not valid.")
				return None
			if self.SS_type == self.P_TSS:
				if not self.util.GO_root[id1] == self.util.GO_root[id2]:
					raise "Terms are not from the same ontology"
					return None
			elif self.SS_type == self.G_TSS:
				for i in id1:
					t1 = i
					break
				for i in id2:
					t2 = i
					break
				if not self.util.GO_root[t1] == self.util.GO_root[t2]:
					raise "Terms are not from the same ontology"
					return None
		else:
			id1 = term1
			id2 = term2
		return self.int_SemSim(id1, id2)
