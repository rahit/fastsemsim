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
This class provides the prototype for a generic Protein (or more in general, an Object) Semantic Similarity measure (PSS)
"""

from fastSemSim.GO import AnnotationCorpus
from fastSemSim.GO import GeneOntology
from SemSimUtils import *
from TermSemSim import *
from MixSemSim import *
from SemSimMeasures import *

import sys
import os
import math

class ObjSemSim:
	def pick_TSS(self):
		if not self.TSS in SemSimMeasures:
			raise "Semantic Similarity Measure not available."
			return TermSemSim(self.ac, self.go, self.util)
		else:
			return SemSimMeasures[self.TSS][0](self.ac, self.go, self.util)

	def pick_mixSS(self):
		if not self.mixSS in MixingStrategies:
			raise "Mixing Strategy not available."
			return MixSemSim(self.ac, self.go)
		else:
			return MixingStrategies[self.mixSS](self.ac, self.go)

	def __init__(self, ac, go, TSS = None, MSS = None, util = None):
		self.go = go
		self.ac = ac
		self.util = util
		self.TSS = TSS
		self.mixSS = MSS
		if self.util == None:
			self.util = SemSimUtils(self.ac, self.go)
			self.util.det_IC_table()
		if self.TSS is None:
			self.TSS = TermSemSim(self.ac, self.go, self.util)
		elif type(self.TSS) is str or unicode:
			self.TSS = str(self.TSS)
			self.TSS = self.pick_TSS()
		else:
			raise Exception
		if self.mixSS is None:
			self.mixSS = MixSemSim(self.ac, self.go)
		elif type(self.mixSS) is str or unicode:
			self.mixSS = str(self.mixSS)
			self.mixSS = self.pick_mixSS()
		else:
			raise Exception

	def int_format_data(self, obj, onto):
		# assume ac is sanitized
		if not obj in self.ac.annotations:
			#print(str(obj) + " not found in Annotation Corpus.")
			return None
		terms = []
		for i in self.ac.annotations[obj]:
			#if i in self.go.obsolete_ids: # not present in GO_root
				#continue
			if i in self.util.GO_root and self.util.GO_root[i] == onto:
				terms.append(i)
		return terms

	def int_SemSim(self, term1, term2):
		if term1 is None or term2 is None or len(term1) == 0 or len(term2) == 0:
			return None
		if self.TSS.SS_type == self.TSS.P_TSS:
			sscore = self.mixSS.SemSim(term1, term2, self.TSS)
		elif self.TSS.SS_type == self.TSS.G_TSS:
			sscore = self.TSS.SemSim(term1, term2)
		else:
			raise "Semantic Similarity measure not properly configured."
		return sscore

	def SemSim(self, obj1, obj2, ontology):
		if str(ontology) == self.util.BP_ontology:
			onto = self.util.go.BP_root
		elif str(ontology) == self.util.MF_ontology:
			onto = self.util.go.MF_root
		elif str(ontology) == self.util.CC_ontology:
			onto = self.util.go.CC_root
		else:
			raise "No valid ontology selected: " + str(ontology)
			return None
		t1 = self.int_format_data(obj1, onto)
		t2 = self.int_format_data(obj2, onto)
		# print t1
		# print t2
		return self.int_SemSim(t1, t2)
