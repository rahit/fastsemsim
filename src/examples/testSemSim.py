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
This is an example program. It loads a Gene Ontology, an annotation corpus (GOA format) and a list of proteins.
It returns a list of protein pairs and their semantic similarity (Resnik BMA).
"""

from GO import AnnotationCorpus
from GO import GeneOntology
from SemSim import ObjSemSim
from SemSim import SemSimUtils
import sys
import os

if __name__ == "__main__":
	#### load ontology
	tree = GeneOntology.load_GO_XML(open(sys.argv[1]))
	print "Ontology infos: file name: " + str(sys.argv[1]) + ". Nodes: " + str(tree.node_num()) + ". Edges: " + str(tree.edge_num())
	
	#### load annotations
	gp = AnnotationCorpus.AnnotationCorpus(tree)
	gp.parse(sys.argv[2], 'GOA')
	
	#gp.check_consistency()
	print "Annotated proteins: " + str(len(gp.annotations))
	print "Annotated terms: " + str(len(gp.reverse_annotations))
	
	# check if everything is ok...
	gp.check_consistency()
	gp.sanitize()
	
	# create a SemSimUtils object. It provides basic functionalities required by almost every SS measure.
	ssu = SemSimUtils.SemSimUtils(gp, tree)
	ssu.det_offspring_table()
	ssu.det_ancestors_table()
	ssu.det_freq_table()
	ssu.det_GO_division()
	ssu.det_ICs_table()

	# create SemSim object. It is not mandatory to supply a SemSimUtils object. ObjSemSim builds his own SemSimUtils object in this case.
	SS_Resnik_BMA = ObjSemSim.ObjSemSim(gp, tree, "Resnik", "BMA", ssu)

	# load a list of proteins
	inf = open(sys.argv[3],'r')
	human_pairs = []
	for line in inf:
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		human_pairs.append(line)
	test_set = human_pairs
	inf.close()
	
	# determine pairwise semantic similarity and print it on console. Molecular Function (MF) ontology is used
	for i in range(len(test_set)):
		for j in range(i+1, len(test_set)):
			test = SS_Resnik_BMA.SemSim(test_set[i],test_set[i],"MF")
			print(str(test_set[i]) + "\t" + str(test_set[j]) + "\t" + str(test))
	print("-----------------------------------------------------------------")