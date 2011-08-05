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