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

class JiangConrathSemSim(TermSemSim) :
	SS_type = TermSemSim.P_TSS
	IC_based = True

	def int_SemSim(self, term1, term2):
		termid = self.util.det_MICA(term1, term2)
		sim = 1/(-2.0 * self.util.IC[termid] + self.util.IC[term1] + self.util.IC[term2] + 1)
		return sim