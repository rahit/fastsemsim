# -*- coding: iso-8859-1 -*-
"""
This class implements Resnik Term Semantic Similarity Measure
"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSimUtils import *
from TermSemSim import * 
import sys
import os
import math

class SimGICSemSim(TermSemSim) :
	SS_type = TermSemSim.G_TSS
	IC_based = True

	def int_SemSim(self, term1, term2):
		#print term1
		#print term2
		inters = self.util.det_common_ancestors(term1, term2)
		union = self.util.det_ancestors_union(term1, term2)
		#print inters
		#print union
		intIC = 0
		for i in inters:
			intIC += self.util.IC[i]
		uniIC = 0
		for i in union:
			uniIC += self.util.IC[i]
		if uniIC == 0 and intIC == 0:
			return 0
		return intIC/uniIC