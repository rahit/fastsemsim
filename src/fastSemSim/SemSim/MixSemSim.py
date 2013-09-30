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
This class provides the prototype for a generic mixing strategy for pairwise Terms Protein Semantic Similarity measures (mixSS)
"""

import sys
import os
import math

class MixSemSim(object):

	def __init__(self, ontology, ac, util = None):
		self.ontology = ontology
		self.annotation_corpus = ac
		self.util = util
		#if self.util == None:
			#self.util = SemSimUtils(ac, go)
			#self.ssu.det_IC_table()

	def int_format_data(self, term1):
		if type(term1) is list or type(term1) is dict or type(term1) is set:
			return term1
		else:
			return [term1,]
		
	def SemSim(self, set1, set2, TSS):
		lset1 = self.int_format_data(set1)
		lset2 = self.int_format_data(set2)
		#### translate into id format & check data
		if lset1 is None or lset2 is None or len(lset1) == 0 or len(lset2) == 0:
			return None
		temp_scores = []
		for i in lset1:
			for j in lset2:
				temp_scores.append((i, j, TSS.SemSim(i,j)))
		return self.int_SemSim(temp_scores)

	def int_SemSim(self, scores):
		raise "No mixing strategy selected."
		return None
