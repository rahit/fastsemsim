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

#from GO import AnnotationCorpus
#from GO import GeneOntology
#from SemSimUtils import *
from MixSemSim import *
import sys
import os
import math

class maxSemSim(MixSemSim):

	def int_SemSim(self, scores):
		if len(scores) == 0:
			return 0
		finale = 0
		for i in scores:
			#print scores[i]
			if i[2] == -1:
				print("Errore in avgSemSim")
			if i[2] >= finale:
				finale = i[2]
		return finale

#if __name__ == "__main__":
	##### load annotations
	#gp = AnnotationCorpus.AnnotationCorpus()
	#gp.parse(sys.argv[2])

	##### load ontology
	#tree = GeneOntology.get_go_graph(open(sys.argv[1]))
	#print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.V.__len__()) + ". Edges: " + str(tree.E.__len__())
	
	##### create SemSimUtils class
	#ssu = SemSimUtils(gp, tree)
	#ssu.det_offspring_table()
	#ssu.det_ancestors_table()
	#ssu.det_freq_table()
	#ssu.det_GO_division()
	#ssu.det_ICs_table()

	#TSS = TermSemSim(gp, tree, ssu)
	#test = TSS.SemSim("GO:0030682","GO:0030683")
	#print test
	#test = TSS.SemSim("GO:0008150","GO:0008150")
	#print test