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

class ResnikSemSim(TermSemSim) :
	SS_type = TermSemSim.P_TSS
	IC_based = True

	def int_SemSim(self, term1, term2):
		termid = self.util.det_MICA(term1, term2)
		return self.util.IC[termid]

if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.get_go_graph(open(sys.argv[1]))
	print("Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__()))
	
	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp.parse(sys.argv[2])

	#### create SemSimUtils class
	ssu = SemSimUtils(gp, tree)
	ssu.det_offspring_table()
	ssu.det_ancestors_table()
	ssu.det_freq_table()
	ssu.det_GO_division()
	ssu.det_ICs_table()

	TSS = ResnikSemSim(gp, tree, ssu)
	test = TSS.SemSim("GO:0008150","GO:0008150")
	print(test)
	test = TSS.SemSim("GO:0000001","GO:0009987")
	print(test)
	test = TSS.SemSim("GO:0000001","GO:0032189")
	print(test)